import subprocess
import time
import random

# Set the duration for the script to run (5 minutes)
end_time = time.time() + 5 * 60

while time.time() < end_time:
    # Randomly decide whether to open the calculator (e.g., 10% chance each second)
    if random.random() < 0.1:
        # Open the calculator application
        # subprocess.Popen('calc.exe')  # For Windows
        # subprocess.Popen(['gnome-calculator'])  # For Linux with GNOME
        subprocess.Popen(['open', '-na', 'Calculator'])  # For macOS

    # Wait for 1 second before checking again
    time.sleep(1)

print("Done running the calculator opener script.")
