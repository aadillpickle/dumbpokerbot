import cv2 as cv
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

HAND_NUMBER_REGION = (205, 134, 135, 35)
POT_SIZE_REGION = (324, 733, 190, 36)
CHIPS_REGION = (1069, 649, 150, 30)


SCALE_FACTOR = 2