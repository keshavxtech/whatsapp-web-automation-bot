import pyautogui
import pyperclip
import time
from reply_engine import generate_reply

print("Bot starting in 5 seconds...")
time.sleep(5)

while True:
    # Select last message
    pyautogui.moveTo(800, 900)   # <-- Adjust according to your screen
    pyautogui.click()
    pyautogui.hotkey("ctrl", "c")

    time.sleep(1)

    message = pyperclip.paste()

    reply = generate_reply(message)

    pyperclip.copy(reply)

    pyautogui.typewrite(reply)
    pyautogui.press("enter")

    time.sleep(5)

   
