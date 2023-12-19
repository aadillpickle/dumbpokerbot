import time
import pyautogui

import mss
from PIL import Image
from constants import SCALE_FACTOR, HAND_CARD_SUIT_REGIONS, SUITS_RGB_VALUES, CARD_SUIT_REGIONS

def locate_button_on_screen(button_image):
    try:
        element = pyautogui.locateCenterOnScreen(button_image, grayscale=True)
        element_x = element.x / SCALE_FACTOR
        element_y = element.y / SCALE_FACTOR

        return (element_x, element_y)
    except pyautogui.ImageNotFoundException as e:
        return None

def detect_suit(screen_region): # detects a suit in a given region using color
    with mss.mss() as sct:
        img = sct.grab(screen_region)
        rgb_values = img.pixel(0,0)
        print(rgb_values)
        for key, value in SUITS_RGB_VALUES.items():
            if value == rgb_values:
                    return key[0]
        return None
