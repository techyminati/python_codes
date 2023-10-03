import openai
import requests
import random
import subprocess
import os
from gtts import gTTS
import cv2
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip

# Constants
PIXABAY_API_KEY = ""  # Your Pixabay API key
OPENAI_API_KEY = ""   # Your OpenAI API key

def generate_script():
    openai.api_key = OPENAI_API_KEY
    topic = input("Enter the topic for your video: ")
    prompt = (
        f"Please generate a video script for a 5-minute presentation on {topic}.The script should cover the key points, ideas, and explanations you would like to include in the video."
    )
    model = "text-davinci-003"
    temperature = 0.5
    max_tokens = 50

    try:
        response = openai.Completion.create(
            engine=model, prompt=prompt, temperature=temperature, max_tokens=max_tokens
        )
        script = response.choices[0].text.strip().replace('"', '')
        with open("script.txt", "w") as f:
            f.write(script)
    except Exception as e:
        print(f"OpenAI API request failed: {e}")

def fetch_pixabay_video():
    print("fetching video")
    query_params = {
        "key": PIXABAY_API_KEY,
        "q": "nature",
        "orientation": "vertical",
        "video_type": "film"
    }

    try:
        response = requests.get("https://pixabay.com/api/videos/", params=query_params)
        response.raise_for_status()
        video_data = random.choice(response.json()["hits"])
        video_url = video_data["videos"]["large"]["url"]
        video_response = requests.get(video_url)

        with open("video.mp4", "wb") as f:
            f.write(video_response.content)
    except Exception as e:
        print(f"Pixabay API request failed: {e}")

def generate_audio():
    print("generating audio")
    try:
        with open("script.txt", "r") as file:
            text = file.read()
        language = 'en-in'
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("output.mp3")
    except Exception as e:
        print(f"Audio generation failed: {e}")

def cut_video():
    print("cutting vid to proper legnth")
    audio_path = 'output.mp3'
    video_path = 'video.mp4'
    output_path = 'cutvideo.mp4'

    try:
        audio = AudioSegment.from_file(audio_path)
        audio_duration = audio.duration_seconds * 1000

        cap = cv2.VideoCapture(video_path)
        video_duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS) * 1000)

        # Calculate the number of times the video needs to be repeated
        repeat_count = int(audio_duration / video_duration) + 1

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

        for _ in range(repeat_count):
            cap.set(cv2.CAP_PROP_POS_MSEC, 0)  # Reset video to start
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                else:
                    break

        cap.release()
        out.release()
    except Exception as e:
        print(f"Video repeating failed: {e}")

def combine_video_and_audio():
    print("combining audio and video")
    input_video_file = 'cutvideo.mp4'
    input_audio_file = 'output.mp3'
    output_video_file = 'final.mp4'

    command = [
        "ffmpeg",
        "-i", input_video_file,
        "-i", input_audio_file,
        "-c:v", "copy",
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        output_video_file
    ]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("Video and audio combined successfully!")
        else:
            print("Error combining video and audio.")
            print(result.stderr.decode("utf-8"))
    except Exception as e:
        print(f"Video and audio combination failed: {e}")

if __name__ == "__main__":
    generate_script()
    fetch_pixabay_video()
    generate_audio()
    cut_video()
    combine_video_and_audio()
