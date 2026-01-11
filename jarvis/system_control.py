import os
import subprocess
import webbrowser
import pyautogui
import time

def open_chrome():
    """Opens Google Chrome."""
    try:
        # Works if Chrome is in PATH or registered
        os.startfile("chrome") 
    except FileNotFoundError:
        # Fallback for common Windows path if generic fails
        try:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen(chrome_path)
        except:
            return False
    return True

def close_chrome():
    """Force closes Chrome."""
    os.system("taskkill /f /im chrome.exe")

def google_search(query):
    """Searches Google for the query."""
    webbrowser.open(f"https://www.google.com/search?q={query}")

def type_text(text):
    """Types the given text using keyboard simulation."""
    # Add a small delay to switch focus if needed
    time.sleep(0.5) 
    pyautogui.write(text, interval=0.05)

def play_pause_music():
    """Toggles media play/pause using system keys."""
    pyautogui.press("playpause")

def volume_control(action):
    """Controls volume: 'increase', 'decrease', or 'mute'."""
    if action == "increase":
        for _ in range(5):
            pyautogui.press("volumeup")
    elif action == "decrease":
        for _ in range(5):
            pyautogui.press("volumedown")
    elif action == "mute":
        pyautogui.press("volumemute")

def system_power(action):
    """Handles 'shutdown' or 'restart'."""
    if action == "shutdown":
        os.system("shutdown /s /t 10")
    elif action == "restart":
        os.system("shutdown /r /t 10")
