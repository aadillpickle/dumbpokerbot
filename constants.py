import cv2 as cv
BUTTON_PICS = {
    'fold': cv.imread('./buttons/fold.png'),
    'call': cv.imread('./buttons/call.png'),
    'raise': cv.imread('./buttons/raise.png'),
    'check': cv.imread('./buttons/check.png'),
    'bet': cv.imread('./buttons/bet.png'),
}

RAISE_AMOUNT_PICS = {
    'raise_3bb': cv.imread('./buttons/raise3bb.png'),
    'raise_max': cv.imread('./buttons/raisemax.png'),
    'raise_min': cv.imread('./buttons/raisemin.png'),
    'raise_pot': cv.imread('./buttons/raisepot.png')
}

USERNAME_PIC = cv.imread('username_pic.png')
# REGION = {'top': 890, 'left': 920, 'width': 800, 'height': 210}

ENTIRE_SCREEN_REGION = {'top': 0, 'left': 0, 'width': 0, 'height': 0}

POT_SIZE_REGION = {'left': 862, 'top': 367, 'width': 190, 'height': 40}
X_SCALE_FACTOR = 0.44
Y_SCALE_FACTOR = 0.47
X_ADJUSTMENT_FACTOR = 135
Y_ADJUSTMENT_FACTOR = 75
NAME_Y_ADJUSTMENT_FACTOR = 80

# {'top': 1673, 'left': 1925, 'width': 300, 'height': 60}

# manual coordinates i found for the chip amounts, where 1 is the top center position at the table, and then it goes clockwise from there
CHIP_AMOUNT_POSITIONS = {
    1: {'top': 215, 'left': 859, 'width': 150, 'height': 30},
    2: {'top': 321, 'left': 1475, 'width': 150, 'height': 30},
    3: {'top': 648, 'left': 1518, 'width': 150, 'height': 30},
    4: {'top': 839, 'left': 933, 'width': 150, 'height': 30},
    5: {'top': 648, 'left': 279, 'width': 150, 'height': 30},
    6: {'top': 319, 'left': 329, 'width': 150, 'height': 30}
}