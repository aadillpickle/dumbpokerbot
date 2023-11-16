import pytesseract
import pyautogui

import re

#use mss if speed is an issue
def capture_and_ocr(screen_region):
    # screen_region = (top, left, width, height)
    img = pyautogui.screenshot(imageFilename="./screencap.png", region=screen_region)
    img.save('screencap.png')
    return pytesseract.image_to_string(img).strip()

def contains_digits(text):
    return bool(re.search(r'\d', text))