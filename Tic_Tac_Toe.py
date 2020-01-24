#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    
    clear_output() #only works in jupyter
    
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|")
    print("|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|")


# In[3]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[4]:


def player_input():
    
    marker = ""
    
    #player1 = input("Please pick a marker 'X' or 'O'")
    
    while marker != ("X" or "O"):
        
         marker = input("Please pick a marker 'X' or 'O'")
            
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
        
    else:
        player2 = "X"
        
    return (player1, player2)


# In[5]:


player_input()


# In[6]:


def place_marker(board, marker, position):
    
    #position = int(input("enter the position where you want to place the marker"))
    
    #marker = 
    
    board[position] = marker


# In[7]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[8]:


def win_check(board, mark):
    
    #CHECKING HORIZENTALLY
    i=1
    while i<=7:
        
        if board[i] == board[i+1] == board[i+2] == mark:
            return "YOU WIN"
        else:
            i+=3
        
    #CHECKING VERICALLY
    i = 1
    while i<=3:
        
        if board[i] == board[i+3] == board[i+6] == mark:
            return "YOU WIN"
        else:
            i+=1
            
    #CHECKING DIAGONICALLY
    if board[1] == board[5] == board[9] == mark:

        return "YOU WIN"

    elif board[3] == board[5] == board[7] == mark:

        return "YOU WIN"

    # IF MARK ISN'T WIN THE GAME

    else :

        return "YOU LOST"       
        


# In[9]:


display_board(test_board)
win_check(test_board,'X')


# In[10]:


import random

def choose_first():
    
    flip = random.randint(0, 1)
    
    if flip == 1:
        return "player 2"
    else:
        return "player 1"


# In[11]:


def space_check(board, position):
    
     return board[position] == " "


# In[12]:


def full_board_check(board):
    
    for i in range(1, 10):
        
        if space_check(board, i):
            
            return False
        
    return True


# In[13]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    
        position = int(input("enter the next position (1-9)"))
        
    return position


# In[14]:


def replay():
    
    choice == input("Play again ? enter Yes or No")
    
    return choice == "Yes"


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    
    board_f = [" "]*10
    
    player1_m, player2_m = player_input()
    
    first = choose_first()
    
    print(first +  "will go first")
    
    play_start = input("Ready to start the play ? yes or no")
    
    if play_start == "yes":
        
        game_on = True
        
    else:
        
        game_on = False
        
        while game_on:

            #Player 1 Turn
            if first == "player 1":

                display_board(board_f)

                position = player_choice(board_f)
                
                place_marker(board_f, player1_m, position)
                
                if win_check(board_f, player1_m):
                    display_board(board_f)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(board_f):
                        display_board(board_f)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
                        
            else:
            # Player2's turn.
            
                display_board(board_f)
                position = player_choice(board_f)
                place_marker(board_f, player2_m, position)

                if win_check(board_f, player2_m):
                    display_board(board_f)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(board_f):
                        display_board(board_f)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'
                        
    if not replay():
        
        break


# In[ ]:




