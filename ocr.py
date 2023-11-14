import pytesseract
import mss
from PIL import Image
import re

def capture_and_ocr(region):
    with mss.mss() as sct:
        region = {'top': region['top'], 'left': region['left'], 'width': region['width'], 'height': region['height']}
        img = sct.grab(region)
        image = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        #save image to file
        image.save("screencap.png")
        return pytesseract.image_to_string(image).strip()

def contains_digits(text):
    return bool(re.search(r'\d', text))