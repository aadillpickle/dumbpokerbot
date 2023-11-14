import random
import pyautogui
from constants import RAISE_AMOUNT_PICS
from locate import locate_button_on_screen

def take_random_action(available_actions, locations):
    # Now choose a random action and perform it
    action = random.choice(available_actions)
    bet_action = None
    print(action)
    if action == 'raise' or action == 'bet':
        #check if raise amount is available
        raise_amount_locations = {action: locate_button_on_screen(button_pic) for action, button_pic in RAISE_AMOUNT_PICS.items()}
        available_raise_amounts = [action for action, loc in raise_amount_locations.items() if loc is not None]
        if available_raise_amounts:
            bet_action = random.choice(available_raise_amounts)
            print(bet_action)
            pyautogui.moveTo(*raise_amount_locations[bet_action])
            pyautogui.click(*raise_amount_locations[bet_action])
            print(f"took action: {bet_action}")
            pyautogui.sleep(0.2)
        
    if locations.get(action):  # Check if the action button is available
        pyautogui.moveTo(*locations[action])
        pyautogui.click(*locations[action])
        print(f"took action: {action}")
        if bet_action:
            return f"{action}: {bet_action}"
        return action