import random
import pyautogui
from constants import RAISE_AMOUNT_COORDINATES
from locate import locate_button_on_screen

def take_action(available_actions, locations, position, center_cards, hand_cards):
    # strategy goes here
    action = "raise" if "raise" in available_actions else "bet"

    bet_action = None
    sus_moves = ['raise', 'bet']
    if action in sus_moves:
        #betting strat here
        bet_action = "all_in"
        
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
    
def click_next_hand(next_hand_button):
    pyautogui.moveTo(*next_hand_button)
    pyautogui.click(*next_hand_button)
    print("clicked next hand")