import pyautogui
import time
import tkinter as tk
from tkinter import filedialog


def take_screenshot(save_path):
    # Get the current time
    current_time = time.strftime("%Y%m%d-%H%M%S")

    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Save the screenshot with a timestamp at the specified location
    screenshot.save(f"{save_path}/screenshot_{current_time}.png")


def print_screenshot_count(screenshot_count):
    # Print the screenshot count in the shell
    print(f"Screenshot taken: {screenshot_count}")


def increment_screenshot_count(screenshot_count):
    screenshot_count += 1
    return screenshot_count


def run_screenshot_tool(save_path):
    screenshot_count = 0

    while True:
        screenshot_count = increment_screenshot_count(screenshot_count)
        take_screenshot(save_path)
        print_screenshot_count(screenshot_count)
        time.sleep(60)


def main():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user to select the save location using a file dialog
    save_path = filedialog.askdirectory()

    # Validate the save location
    if not save_path:
        print("No save location selected. Exiting...")
        return

    run_screenshot_tool(save_path)


if __name__ == "__main__":
    main()
