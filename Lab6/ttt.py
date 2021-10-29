'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def spot_empty(square_num):
    return board[(square_num - 1) // 3][(square_num-1)%3]==" "
def put_X_O():
    global turn
    choice = turn
    return choice
def take_input():
    print('Enter your move:')
    square_num = input() 
    while not spot_empty(square_num) or type(square_num)!=int or square_num>9 or square_num<1:
        print('Error, please re-enter:')
        square_num = input() 
    board[(square_num - 1) // 3][(square_num-1)%3]=put_X_O()
    free_squares.remove([(square_num - 1) // 3, (square_num-1)%3])
def get_free_squares():
    return free_squares
def make_random_move(board, mark):
    position = free_squares[int(len(free_squares)*random.random())]
    board[position[0]][position[1]]=mark
    free_squares.remove(position)
def make_smart_move(board, mark):
    for x, y in free_squares:
        board[x][y]=mark
        if is_win(board, turn):
            free_squares.remove([x,y])
            return
        else:
            board[x][y]=" "
    make_random_move(board, mark)
def is_row_all_marks(board, row_i, mark):
    return board[row_i]==[mark, mark, mark]
def is_diaganal_all_marks(board, mark):
    lr= (board[0][0]==board[1][1] and board[1][1]==mark and board[2][2]==mark) 
    rl= (board[2][0]==board[1][1] and board[1][1]==mark and board[0][2]==mark)
    return rl or lr
def is_col_all_marks(board, col_i, mark):
    return board[0][col_i]==mark and board[1][col_i]==mark and board[2][col_i]==mark
def is_win(board, mark):
    for i in range(3):
        if is_col_all_marks(board, i, mark): return True
        if is_row_all_marks(board, i, mark): return True
    if is_diaganal_all_marks(board, mark): return True
    return False
    
if __name__ == '__main__':
    global free_squares
    free_squares=[[x,y] for x in range(3) for y in range (3)]
    global board
    board = make_empty_board()
    global turn
    turn = "X"
    for i in range (9):
        if i%2==0: take_input()
        else: make_smart_move(board, put_X_O())
        print_board_and_legend(board)
        if is_win(board, turn): 
            print(turn,"wins!")
            break
        turn = turn =="X" and "O" or "X"
