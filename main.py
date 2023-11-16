import time
import csv
from constants import BUTTON_PICS, RAISE_AMOUNT_COORDINATES, CHIPS_REGION, HAND_NUMBER_REGION
from locate import locate_button_on_screen
from strats import take_action
from ocr import capture_and_ocr, contains_digits
import threading

last_chips = None
last_round_number = 1

round_number = 1
actions = []
chip_changes = []

time.sleep(2)
with open('poker_bot_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Round Number', 'Actions', 'Chip Changes', 'Win?'])
    print('starting 100 rounds')
    while round_number < 100:
        time.sleep(1)
        round_number = capture_and_ocr(HAND_NUMBER_REGION)
        round_number = int(round_number.replace('Hand:', '').replace('#', '').strip())
        print(f"Round number: {round_number}")
        print("-----------------------------")
        print(f"Last round number: {last_round_number}")
        if round_number != last_round_number and contains_digits(round_number):
            print(f"Round ended")

            delta_chips = chip_changes[-1] - chip_changes[0]
            result = None
            
            chip_changes = list(filter(lambda item: item is not None, chip_changes))
            if delta_chips > 0:
                result = f"win: {delta_chips}"
            elif delta_chips == 0:
                result = 'no_change'
            elif delta_chips < 0:
                result = f"loss: {delta_chips}"

                
            actions = list(filter(lambda item: item is not None, actions))

            writer.writerow([round_number, '\n'.join(actions), '\n'.join(chip_changes), result])
            print(f"Round ended, result: {result}")
            
            chip_changes = []
            actions = []
            result = None
            last_round_number = round_number

        detected_chips = capture_and_ocr(CHIPS_REGION)
        
        locations = {action: locate_button_on_screen(button_pic) for action, button_pic in BUTTON_PICS.items()}
        available_actions = [action for action, loc in locations.items() if loc is not None]

       
        if available_actions:
            selected_action = take_action(available_actions, locations)
            actions.append(selected_action)

        elif not available_actions:
            print("No available actions")


        if detected_chips != last_chips and contains_digits(detected_chips):
            chip_changes.append(f"{detected_chips-last_chips}")
            print(f"Chip change: {detected_chips-last_chips}")
            last_chips = detected_chips


    print('done 100 rounds!')