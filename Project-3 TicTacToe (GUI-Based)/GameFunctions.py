from tkinter import *
from tkinter import messagebox

current_character = 'X'
current_player = 'X'
positions = [''] * 10
positions[0] = '#' # no use

def reset_game(buttons) :
    global positions
    global current_character
    global current_player
    
    for i in range(1 , len(buttons) + 1) :
        buttons[i]['bg'] = '#f1f2f6'
        buttons[i]['text'] = ''
    positions = [''] * 10
    positions[0] = '#'
    current_character = 'X'
    current_player = 'X'

def is_win(buttons) :
    global positions
    
    if (
        (positions[1] == positions[2] == positions[3] == 'X') or 
        (positions[1] == positions[2] == positions[3] == 'O')
    ) :
        buttons[1]['bg'] = '#eb4d4b'
        buttons[2]['bg'] = '#eb4d4b'
        buttons[3]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[4] == positions[5] == positions[6] == 'X') or 
        (positions[4] == positions[5] == positions[6] == 'O')
    ) :
        buttons[4]['bg'] = '#eb4d4b'
        buttons[5]['bg'] = '#eb4d4b'
        buttons[6]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[7] == positions[8] == positions[9] == 'X') or 
        (positions[7] == positions[8] == positions[9] == 'O')
    ) :
        buttons[7]['bg'] = '#eb4d4b'
        buttons[8]['bg'] = '#eb4d4b'
        buttons[9]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[1] == positions[4] == positions[7] == 'X') or 
        (positions[1] == positions[4] == positions[7] == 'O')
    ) :
        buttons[1]['bg'] = '#eb4d4b'
        buttons[4]['bg'] = '#eb4d4b'
        buttons[7]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[2] == positions[5] == positions[8] == 'X') or 
        (positions[2] == positions[5] == positions[8] == 'O')
    ) :
        buttons[2]['bg'] = '#eb4d4b'
        buttons[5]['bg'] = '#eb4d4b'
        buttons[8]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[3] == positions[6] == positions[9] == 'X') or 
        (positions[3] == positions[6] == positions[9] == 'O')
    ) :
        buttons[3]['bg'] = '#eb4d4b'
        buttons[6]['bg'] = '#eb4d4b'
        buttons[9]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[1] == positions[5] == positions[9] == 'X') or 
        (positions[1] == positions[5] == positions[9] == 'O')
    ) :
        buttons[1]['bg'] = '#eb4d4b'
        buttons[5]['bg'] = '#eb4d4b'
        buttons[9]['bg'] = '#eb4d4b'
        return True
    elif (
        (positions[3] == positions[5] == positions[7] == 'X') or 
        (positions[3] == positions[5] == positions[7] == 'O')
    ) :
        buttons[3]['bg'] = '#eb4d4b'
        buttons[5]['bg'] = '#eb4d4b'
        buttons[7]['bg'] = '#eb4d4b'
        return True
    else :
        return False


def is_draw() :
    global positions
    count = 0
    for pos in positions :
        if pos != '' :
            count = count + 1
    if count == len(positions) :
        return True
    return False

def place_character(button , num) :
    global current_character
    global positions
    if button['text'] != 'X' and button['text'] != 'O' :
        button['text'] = current_character
        positions[num] = current_character

        if current_character == 'X' :
            current_character = 'O'
        else :
            current_character = 'X'

