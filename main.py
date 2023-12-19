import time
import csv
from constants import BUTTON_PICS, CHIPS_REGION, HAND_NUMBER_REGION, POSITION_REGION, CARD_SUIT_REGIONS, CARD_RANK_REGIONS, HAND_CARD_RANK_REGIONS, HAND_CARD_SUIT_REGIONS
from locate import locate_button_on_screen, detect_suit
from strats import take_action, click_next_hand
from ocr import capture_and_ocr, contains_digits


last_chips = 100.0
last_round_number = 1

round_number = 1
actions = []
chip_changes = []
center_cards = [""] * 5
hand_cards = [""] * 2
# todo: see cards in center, see cards in hand

def set_middle_cards_helper(card_suit_region, card_rank_region, card_index):
    print(f"Checking center card {card_index+1}")
    card_suit = detect_suit(card_suit_region) #need to get the right regions for the center cards and check if any variation in rbg vals
    if card_suit:
        card_rank = capture_and_ocr(card_rank_region)
        center_cards[card_index] = card_suit + card_rank
        print(f"Card {card_index+1}: {center_cards[card_index]}")
        return True
    return None

def set_hand_cards_helper(card_suit_region, card_rank_region, card_index):
    print(f"Checking card {card_index+1}")
    card_suit = detect_suit(card_suit_region)
    if card_suit:
        card_rank = capture_and_ocr(card_rank_region)
        hand_cards[card_index] = card_suit + card_rank
        print(f"Card {card_index+1}: {hand_cards[card_index]}")
        return True
    return None

time.sleep(2)
with open('poker_bot_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Round Number', 'Actions', 'Chip Changes', 'Win?'])
    print('starting 100 rounds')
    while round_number < 100:
        time.sleep(1)
        next_hand = locate_button_on_screen('./buttons/next_hand.png')
        if next_hand:
            click_next_hand(next_hand)
            time.sleep(1)
            
        round_number = capture_and_ocr(HAND_NUMBER_REGION)
        round_number = int(round_number.replace('Hand:', '').replace('#', '').strip())

        if round_number != last_round_number:
            print(f"Round ended")

            delta_chips = float(chip_changes[-1]) - float(chip_changes[0]) if len(chip_changes) > 1 else 0
            result = None
            
            chip_changes = list(filter(lambda item: item is not None, chip_changes)) if chip_changes else []
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
            center_cards = [""] * 5
            hand_cards = [""] * 2

        detected_chips = float(capture_and_ocr(CHIPS_REGION))
        
        if detected_chips != last_chips:
            chip_changes.append(f"{detected_chips-last_chips}")
            last_chips = detected_chips
        
        button_locations = {action: locate_button_on_screen(button_pic) for action, button_pic in BUTTON_PICS.items()}
        available_actions = [action for action, loc in button_locations.items() if loc is not None]

       
        if available_actions:
            position = capture_and_ocr(POSITION_REGION)

            if not hand_cards[0]:
                set_hand_cards_helper(HAND_CARD_SUIT_REGIONS['card_1'], HAND_CARD_RANK_REGIONS['card_1'], 0)
            if not hand_cards[1]:
                set_hand_cards_helper(HAND_CARD_SUIT_REGIONS['card_2'], HAND_CARD_RANK_REGIONS['card_2'], 1)
            

            if not center_cards[0]:
                cards_available = set_middle_cards_helper(CARD_SUIT_REGIONS['card_1'], CARD_RANK_REGIONS['card_1'], 0)
                if not cards_available:
                    selected_action = take_action(available_actions, button_locations, position, center_cards, hand_cards)
                    actions.append(selected_action)
                    continue
                elif not center_cards[1]:
                    set_middle_cards_helper(CARD_SUIT_REGIONS['card_2'], CARD_RANK_REGIONS['card_2'], 1)
                    if not center_cards[2]:
                        set_middle_cards_helper(CARD_SUIT_REGIONS['card_3'], CARD_RANK_REGIONS['card_3'], 2)
            elif not center_cards[3]:
                set_middle_cards_helper(CARD_SUIT_REGIONS['card_4'], CARD_RANK_REGIONS['card_4'], 3)
            elif not center_cards[4]:
                set_middle_cards_helper(CARD_SUIT_REGIONS['card_5'], CARD_RANK_REGIONS['card_5'], 4)
            else:
                print("All center cards found")
                print(center_cards)

            selected_action = take_action(available_actions, button_locations, position, center_cards, hand_cards)
            actions.append(selected_action)

        elif not available_actions:
            print("No available actions")

    print('done 100 rounds!')
