import os
import random
import time

def close_zed_process():
    # Time in seconds
    wait_time = random.randint(600, 1800)  # Random time between 10 and 30 minutes
    # print(f"The 'zed' process will close in {wait_time / 60} minutes.")
    time.sleep(wait_time)
    # Command to close the 'zed' process on macOS
    # os.system('pkill zed')
    os.system('pkill Code')

if __name__ == "__main__":
    close_zed_process()
