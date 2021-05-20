position = []
p1_score ,p2_score = 0 , 0
def initialize_positions() :
    global position
    position = [' '] * 10
    position[0] = '#'

# for chosing character for player
def initial_inputs() :
    p1_char , p2_char = '' , ''
    while p1_char not in ['X' , 'O'] :
        p1_char = input('Which character do you want for Player 1 (X/O) ? : ')
        if p1_char not in ['X' , 'O'] :
            print('Invalid Character please try again...')
        if p1_char == 'X' :
            p2_char = 'O'
        else :
            p2_char = 'X'

    print(f'Character for Player 1 : {p1_char}')
    print(f'Character for Player 2 : {p2_char}')
    
    return [p1_char , p2_char]

# displaying board structure
def print_board(positions) :
    board = [
        [positions[7] , '|' , positions[8] , '|' , positions[9]],
        ['-' , '-' , '-' , '-' , '-' , '-'] ,
        [positions[4] , '|' , positions[5] , '|' , positions[6]],
        ['-' , '-' , '-' , '-' , '-' , '-'] ,
        [positions[1] , '|' , positions[2] , '|' , positions[3]],
        
    ]
    for i in range(5) :
        for j in range(len(board[i])) :
            print(board[i][j] , end= '  ')
        print()

# check whether game is over or not

def game_over() :
    global position
    if (
        (position[1] == position[2] == position[3] == 'X') or (position[1] == position[2] == position[3] == 'O') or
        (position[4] == position[5] == position[6] == 'X') or (position[4] == position[5] == position[6] == 'O') or
        (position[7] == position[8] == position[9] == 'X') or (position[7] == position[8] == position[9] == 'O') or 
        (position[1] == position[4] == position[7] == 'X') or (position[1] == position[4] == position[7] == 'O') or
        (position[2] == position[5] == position[8] == 'X') or (position[2] == position[5] == position[8] == 'O') or
        (position[3] == position[6] == position[9] == 'X') or (position[3] == position[6] == position[9] == 'O') or
        (position[1] == position[5] == position[9] == 'X') or (position[1] == position[5] == position[9] == 'O') or
        (position[3] == position[5] == position[7] == 'X') or (position[3] == position[5] == position[7] == 'O')
    ) :
        return True
    else :
        return False
    

# check whether board is full (Draw Game)
def is_position_filled() :
    global position
    count = 0
    for pos in position :
        if pos != ' ' :
            count = count + 1
    if count == len(position) :
        return True
    return False


# game logic
def tic_tac_toe(characters) :
    global position
    global p1_score
    global p2_score
    
    turn = 0
    pos = 0
    while True :

        pos = int(input(f'For Player {turn + 1} - Enter Position : '))
        if position[pos] in characters :
            continue
        position[pos] = characters[turn]

        print_board(position)
        if game_over() :
            if turn == 0 :
                p1_score += 1
                print('Player 1 Wins')
            else :
                p2_score += 1
                print('Player 2 Wins')
            break
        elif is_position_filled() :
            print('Its a Draw')
            break
        if turn == 0 :
            turn = 1
        else :
            turn = 0    


# Driver's Code 
if __name__ == '__main__' :

	# intialize positions
    initialize_positions()

    # take inputs
    characters = initial_inputs()

    # actual game logic
    tic_tac_toe(characters)