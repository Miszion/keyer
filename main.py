import time
import keyboard

while True:
    keyboard.press_and_release('esc') # Press the ESC key
    print('Session refreshed... waiting 10 minutes') # Output refresh log
    time.sleep(600) # Sleep for 10 minutes (60 * 10 seconds)