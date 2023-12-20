BUTTON_PICS = {
    'fold': './buttons/fold.png',
    'call': './buttons/call.png',
    'raise': './buttons/raise.png',
    'check': './buttons/check.png',
    'bet': './buttons/bet.png',
}

RAISE_AMOUNT_COORDINATES = {
    'all_in': {'x': 1650, 'y': 390},
    'raise_max': {'x': 1650, 'y': 495},
    'raise_min': {'x': 1650, 'y': 605},
    'raise_pot': {'x': 1650, 'y': 705},
}

HAND_NUMBER_REGION = (205, 134, 340, 169)
POT_SIZE_REGION = (324, 733, 514, 769)
NET_WINNINGS_REGION = (1100, 680, 1195, 715)
CHIPS_REGION = (1069, 649, 1219, 679)

POSITION_REGION = (977, 720, 1067, 755) 

POSSIBLE_POSITIONS = ['UTG', 'MP', 'CO', 'D', 'SB', 'BB']
SCALE_FACTOR = 2

#NEED TO ADD region[0] to region [2] and region[1] to region[3] to get the actual coordinates, mss works diff than pag, but only for fxns that use mss (maybe not??)
# CARD_RANK_REGIONS = {
#     'card_1': (593, 372, 43, 35),
#     'card_2': (685, 372, 43, 35),
#     'card_3': (776, 372, 43, 35),
#     'card_4': (867, 372, 43, 35),
#     'card_5': (961, 372, 43, 35),
# }

CARD_RANK_REGIONS = {
    'card_1': (593, 372, 636, 407),
    'card_2': (685, 372, 728, 407),
    'card_3': (776, 372, 819, 407),
    'card_4': (867, 372, 910, 407),
    'card_5': (961, 372, 1004, 407),
}

CARD_SUIT_REGIONS = {
    'card_1': (658, 386, 659, 387), 
    'card_2': (745, 386, 746, 387),
    'card_3': (838, 386, 839, 387),
    'card_4': (929, 386, 930, 387),
    'card_5': (1022, 386, 1023, 387),
}


HAND_CARD_RANK_REGIONS = {
    'card_1' : (1010, 564, 1055, 599),
    'card_2' : (1102, 564, 1147, 599),
}

HAND_CARD_SUIT_REGIONS = {
    'card_1' : (1075, 575, 1076, 576),
    'card_2' : (1165, 575, 1166, 576),
}

SUITS_RGB_VALUES = {
    'hearts': (198, 48, 29),
    'hearts_2': (197, 47, 29),
    'clubs': (44, 104, 26),
    'diamonds': (41, 97, 173),
    'diamonds_2': (40, 96, 172),
    'diamonds_3': (41, 96, 173),
    'diamonds_4': (40, 96, 171),
    'spades': (1, 1, 1),
}