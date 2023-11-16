import random
import pyautogui
from constants import RAISE_AMOUNT_COORDINATES
from locate import locate_button_on_screen

def take_action(available_actions, locations):
    # strategy goes here
    action = random.choice(available_actions) 

    bet_action = None

    if action == 'raise' or action == 'bet':
        bet_action = random.choice(RAISE_AMOUNT_COORDINATES.keys())
        
        raise_button_coordinates = RAISE_AMOUNT_COORDINATES[bet_action]['x'], RAISE_AMOUNT_COORDINATES[bet_action]['y']
        pyautogui.moveTo(*raise_button_coordinates)
        pyautogui.click(*raise_button_coordinates)
        print(f"took action: {bet_action}")
        pyautogui.sleep(0.2)
        
    if locations.get(action):  # Check if the action button is available
        pyautogui.moveTo(*locations[action])
        pyautogui.click(*locations[action])
        print(f"took action: {action}")
        if bet_action:
            return f"{action}: {bet_action}"
        return action