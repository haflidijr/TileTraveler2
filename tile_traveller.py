#test test
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def coins(total_coins, valid):
    if valid:
        lever = str(input("Pull a lever (y/n): "))
        while lever != "y" or lever != "n":
            if lever == 'y':
                total_coins += 1
                print("You received 1 coin, your total is now {0}.".format(total_coins))
                break
            elif lever == 'n':
                break
            else:
                print("Invalid Input")
                lever = str(input("Pull a lever (y/n): "))
                continue
    return total_coins
        
def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row, total_coins, valid):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        total_coins = coins(total_coins, valid)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        total_coins = coins(total_coins, valid)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        total_coins = coins(total_coins, valid)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        total_coins = coins(total_coins, valid)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions, total_coins

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    valid = True
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
        valid = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row, valid

# The main program starts here
play_again = True

while play_again:
    victory = False
    row = 1
    col = 1
    total_coins = 0
    valid = True

    while not victory:
        valid_directions, total_coins = find_directions(col, row, total_coins, valid)
        print_directions(valid_directions)
        victory, col, row, valid = play_one_move(col, row, valid_directions)
    print("Victory! Total coins {0}.".format(total_coins))
    play = str(input("Play again (y/n): "))
    if play == 'y':
        continue
    elif play == 'n':
        play_again = False
