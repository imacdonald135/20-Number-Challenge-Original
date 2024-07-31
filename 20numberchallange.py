from random import randint

def is_full(board):
    full = True
    for number in board.values():
        if number == "":
            full = False
            return full
    return full
    
def print_board(board):
    print()
    print("--------------------")    
    for key, value in board.items():
        print(f"{key:2}  :  {value}")
    print("--------------------")    
    print()
    
def place_number(number, board, won):
    finished = False
    placed = False
    
    
    place = number//50
    place +=1
    count = 0
    while not placed and count<21 :
        
        if board[place] == "":
            board[place] = number
            placed = True
            
        elif int(board[place]) > number:
            place -= 1
            
        elif int(board[place]) < number:
            place += 1
            
        else:
            placed = True
            
        if place > 20 or place < 1:
            finished = True
            placed = True
           
        
        count += 1
        #print(place)
        if count>=21:
            placed = True
            finished = True
        
        
    full = is_full(board)
    if full:
        finished = True
        won = True    
    
    return board, finished, won


def playagame():
    won = False
    finished = False
    board = {
        1:"",
        2:"",
        3:"",
        4:"",
        5:"",
        6:"",
        7:"",
        8:"",
        9:"",
        10:"",
        11:"",
        12:"",
        13:"",
        14:"",
        15:"",
        16:"",
        17:"",
        18:"",
        19:"",
        20:"",

        }
    count = 0
    while not finished and count < 20:
        number = randint(0,999)
        #print(f"number: {number}")
        board, finished, won = place_number(number, board, won)
        #print_board(board)
        #if count >= 100:
            #print("count exceeded while trying to fill board")
        
    
    #print(f"won: {won}\nfinished: {finished}\ncount: {count}")
    return won
            

    

def main(number):
    
    games_won = 0
    for i in range(number):
        
        awin = playagame()
        if awin:
            games_won += 1
            
    percent =  games_won*100/number
    print(f"won {games_won} from {number} games ({percent}%)\n")

main(1000000)

