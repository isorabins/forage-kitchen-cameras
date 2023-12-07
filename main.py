import subprocess
import time
from PIL import ImageGrab
import os
import schedule

def open_yi_home_app():
    subprocess.run(["osascript", "-e", 'tell application "YI Home" to activate'])
    time.sleep(10)

def close_yi_home_app():
    subprocess.run(["osascript", "-e", 'tell application "YI Home" to quit'])

def capture_image(image_path):
    screen = ImageGrab.grab()
    screen.save(image_path)

def create_image_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def main():
    desktop_path = os.path.join(os.path.expanduser("~/Desktop"), "forage_images")
    create_image_folder(desktop_path)

    # Format the image name with a timestamp to avoid overwriting previous images
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    image_name = f"captured_image_{timestamp}.jpg"
    image_path = os.path.join(desktop_path, image_name)

    open_yi_home_app()
    capture_image(image_path)
    close_yi_home_app()

# Schedule the main function to run every 30 minutes
schedule.every(30).minutes.do(main)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
