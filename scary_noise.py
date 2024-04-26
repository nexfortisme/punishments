import time
import random
from playsound import playsound

# List of sound files
sound_files = [
    'scream.mp3',
    'sheesh.mp3'  # Add paths to your sound files here
]

def play_random_sound():
    # Choose a random sound file
    sound_file = random.choice(sound_files)
    print(f"Playing: {sound_file}")
    playsound(sound_file)

def main():

    end_time = time.time() + 10 * 60

    while time.time() < end_time:
        # Generate a random delay between 5 to 10 minutes (300 to 600 seconds)
        delay = random.randint(5, 10) * 60
        time.sleep(delay)
        play_random_sound()

if __name__ == "__main__":
    main()
