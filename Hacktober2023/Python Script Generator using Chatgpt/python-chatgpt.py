import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt" , help="The prompt to send to the OpenAI API")
parser.add_argument("file_name" , help="Name of the file to save python script")
args = parser.parse_args()

api_endpoint= "https://api.openai.com/v1/chat/completions"

api_key= os.getenv("OPENAI_API_KEY")  #YOU HAVE TO SET THIS API IN TERMINAL TO USE IT : $env:OPENAI_API_KEY="sk-your api key"

request_headers= {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key 
}

request_data = {
    "model": "text-davinci-002",
    "prompt": f"write python script for {args.prompt}.Write code only without text",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text= print(response.json()["choices"][0]["text"])
    with open(args.file_name, "w") as file:
        file.write(str(response_text))
else:
    print(f"Request failed with status code {str(response.status_code)}")
