import time
import pyautogui

from constants import SCALE_FACTOR, BUTTONS_REGION

def locate_button_on_screen(button_image):
    try:
        element = pyautogui.locateCenterOnScreen(button_image, grayscale=True)
        element_x = element.x / SCALE_FACTOR
        element_y = element.y / SCALE_FACTOR

        return (element_x, element_y)
    except pyautogui.ImageNotFoundException as e:
        return None
def locate_hand_on_screen():
    time.sleep(2)

