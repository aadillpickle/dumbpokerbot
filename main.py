import time
import csv
from constants import BUTTON_PICS, POT_SIZE_REGION, CHIP_AMOUNT_POSITIONS
from locate import locate_button_on_screen
from strats import take_random_action
from ocr import capture_and_ocr, contains_digits
import threading

last_chips = None
round_in_progress = False
round_number = 0
actions = []
chip_changes = []
pot_disappeared = False
pot_check_thread_started = False
chip_amount_position = 4 #set this manually this when u get into game


pot_disappeared_event = threading.Event()

def check_pot():
    global pot_disappeared
    while round_in_progress:
        detected_pot = capture_and_ocr(POT_SIZE_REGION)
        if len(detected_pot) == 0:
            pot_disappeared = True
            pot_disappeared_event.set()
            return  # End the thread
        time.sleep(0.5) 


with open('poker_bot_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Round Number', 'Actions', 'Chip Changes', 'Win?'])

    while round_number < 100:
        time.sleep(1)
        if round_in_progress:
            if not pot_check_thread_started:
                pot_check_thread = threading.Thread(target=check_pot)
                pot_check_thread.start()
                pot_check_thread_started = True

            detected_chips = capture_and_ocr(CHIP_AMOUNT_POSITIONS[chip_amount_position])

            if detected_chips != last_chips and contains_digits(detected_chips):
                chip_changes.append(f"{detected_chips}")
                print(f"Chip change: {detected_chips}")
                last_chips = detected_chips

            if pot_disappeared_event.is_set():
                round_in_progress = False
                result = 'loss'
                print("Round ended, pot disappeared")
                chip_changes = list(filter(lambda item: item is not None, chip_changes))
                if chip_changes[-1] > chip_changes[0]:
                    result = 'win'
                actions = list(filter(lambda item: item is not None, actions))
                writer.writerow([round_number, '\n'.join(actions), '\n'.join(chip_changes), result])
                print(f"Round ended, result: {result}")
                pot_disappeared_event.clear()  # Reset the event flag
                pot_check_thread_started = False


        locations = {action: locate_button_on_screen(button_pic) for action, button_pic in BUTTON_PICS.items()}
        available_actions = [action for action, loc in locations.items() if loc is not None]

        if available_actions:
            if not round_in_progress:
                round_number += 1 
                print(f'round number: {round_number}')
                round_in_progress = True
                actions = []
                chip_changes = []
                pot_dissapeared = False

            selected_action = take_random_action(available_actions, locations)
            actions.append(selected_action)

            if selected_action == 'fold':
                round_in_progress = False
                writer.writerow([round_number, '\n'.join(actions), '\n'.join(chip_changes), 'fold'])
                continue

        elif not available_actions:
            print("No available actions")

    print('done 100 rounds!')