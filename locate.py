
import cv2 as cv
from PIL import Image
import numpy as np
import mss

from constants import ENTIRE_SCREEN_REGION, X_SCALE_FACTOR, Y_SCALE_FACTOR, X_ADJUSTMENT_FACTOR, Y_ADJUSTMENT_FACTOR

def locate_button_on_screen(picture_to_match):
    with mss.mss() as sct:
        img = sct.grab(ENTIRE_SCREEN_REGION)
        img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")
        
        img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        res = cv.matchTemplate(img_cv, picture_to_match, 5)
        loc = np.where(res >= 0.7)
        for pt in zip(*loc[::-1]):
            print(round(pt[0] * X_SCALE_FACTOR + X_ADJUSTMENT_FACTOR), round(pt[1] * Y_SCALE_FACTOR + Y_ADJUSTMENT_FACTOR))
            return (round(pt[0] * X_SCALE_FACTOR + X_ADJUSTMENT_FACTOR), round(pt[1] * Y_SCALE_FACTOR + Y_ADJUSTMENT_FACTOR))
        return None