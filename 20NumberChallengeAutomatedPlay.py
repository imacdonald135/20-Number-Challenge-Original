from random import randint

def is_full(board):
    full = True
    for number in board.values():
        if number == "":
            full = False
            return full
    return full

def is_valid(board):
    
    is_valid = True
    
    badboardlist = board.values()
    goodboardlist = []
    
    for entry in badboardlist:
        if entry == "":
            pass
        else:
            goodboardlist.append(entry)
    
    for i in range(len(goodboardlist)-1):
        if goodboardlist[i] > goodboardlist[i+1]:
            is_valid = False
    
    return is_valid
    
    
def print_board(board):
    print()
    print("--------------------")    
    for key, value in board.items():
        print(f"{key:2}  :  {value}")
    print("--------------------")    
    print()
    
def have_lost(number, board):
   
    empty = True
    
    for entry in board.values():
        if number != "":
            empty = False
    if empty:
        return False
    
    boardlist = []
    for entry in board.values():
        if entry == "":
            boardlist.append("")
        else:
            boardlist.append(entry)

    
    lower_index = 0
    lower = -1
    upper_index = 21
    upper = 1000
    
    
    
    for i in range(0,len(boardlist)):
        
        if boardlist[i] != "":
            if boardlist[i] < number:
                if boardlist[i] > lower:
                    lower = boardlist[i]
                    lower_index = i + 1
                    
            if boardlist[i] > number:
                if boardlist[i] < upper:
                    upper = boardlist[i]
                    upper_index = i + 1
            
       
    
    #print(f"lower index is {lower_index}\nupper index is {upper_index}")
    
    if upper_index - lower_index == 1:
        #print("you lost")
        return True
    
    
   

        
        
        
    
    
    
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
    lost = False
    while not finished:
        placed = False
        print("")
        print("-------------------------")
        number = randint(0,999)
        valid = False
        while not valid:
            if number not in board.values():
                valid = True
            else:
                number = randint(0,999)
                
            
        print_board(board)
        print(f"Your Number is {number}")
        
        
        lost = have_lost(number, board)
        
        if lost:
            break
            
        
        goodSlot = False
        slot = int(input("Where would you like to put it? "))
        while not goodSlot:
            if slot < 1 or slot>20:
                slot = int(input("Invalid slot!\nTry again. "))
            else:
                goodSlot = True
                
        while not placed:
            board[slot] = number
            ordered = is_valid(board)
            if ordered:
                placed = True
            else:
                print("You can't park there sir!")
                board[slot] = ""
                slot = int(input("Try another slot. "))
                goodSlot = False
                while not goodSlot:
                    if slot < 1 or slot>20:
                        slot = int(input("Invalid slot!\nTry again. "))
                    else:
                        goodSlot = True                
            
        
    
    if lost:
        print("so, sorry, you lost.\n")
        
        playagain = input("Would you like to try again? (y/n) ")
        if playagain == "y":
            playagame()
        else:
            print('Thank you for playing')
        
playagame()