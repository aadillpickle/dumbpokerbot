import pytesseract
import mss
import re
from PIL import Image


def capture_and_ocr(screen_region):
    # screen_region = (top, left, width, height)
   with mss.mss() as sct:
        img = sct.grab(screen_region)
        img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        print(pytesseract.image_to_string(img, config='--psm 7').strip())
        return pytesseract.image_to_string(img, config='--psm 7').strip()

def contains_digits(text):
    return bool(re.search(r'\d', text))
