import speedtest as st

# Define Speed
speed = st.Speedtest()

# Also define Download and upload speed

download_speed = speed.download()
upload_speed = speed.upload()

# Print the speed now!

print(f'Your Download speed is {download_speed}')
print(f'Your Upload speed is {upload_speed}')

