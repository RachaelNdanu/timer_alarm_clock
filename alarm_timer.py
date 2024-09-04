import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    # Initialize pygame mixer
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d} : {seconds_left:02d}")

    # Play the alarm sound immediately when time is up
    pygame.mixer.music.play()
    # Ensure the sound starts playing immediately
    time.sleep(1)  # Optional: give a brief pause to ensure the sound starts

# Example usage
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
