"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""

def is_empty(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] !=' ':
                return False
    return True
def is_full(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] ==' ':
                return False
    return True
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    block =0
    if (y_end+d_y>7 or y_end+d_y<0 or x_end+d_x>7 or x_end+d_x<0) or board[y_end+d_y][x_end+d_x]!=" ":
        block+=1
    x_start=x_end
    y_start=y_end
    while(length>0):
        x_start-=d_x
        y_start-=d_y
        length-=1
        if(x_start<0 or y_start<0 or x_start>7 or y_start>7):
            if length==0:
                block+=1
            else: 
                return "Hit the wall before length ends"
        elif(length==0 and board[y_start][x_start]==board[y_end][x_end]):
            return "LONGER THAN LENGTH"
        elif (board[y_start][x_start]!=" " and length==0):
            block+=1
        elif(length>0 and board[y_start][x_start]!=board[y_end][x_end]):
            return "bbwbb or bb bb"
        
    return block == 0 and "OPEN" or (block==1 and "SEMIOPEN" or "CLOSED")
    
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count=0
    semi_open_seq_count=0
    lastColor=None
    while not (y_start>7 or y_start<0 or x_start>7 or x_start<0):
        if lastColor==None and board[y_start][x_start]==col:
            lastColor=col
        elif lastColor==col and board[y_start][x_start]!=col:
            lastColor=None
            if(is_bounded(board, y_start-d_y, x_start-d_x, length, d_y, d_x)=="OPEN") : open_seq_count+=1
            elif (is_bounded(board, y_start-d_y, x_start-d_x,length,  d_y, d_x)=="SEMIOPEN"): semi_open_seq_count+=1
        y_start+=d_y
        x_start+=d_x
    if lastColor==col:
        if(is_bounded(board, y_start-d_y, x_start-d_x, length, d_y, d_x)=="OPEN"): open_seq_count+=1
        elif (is_bounded(board, y_start-d_y, x_start-d_x, length, d_y, d_x)=="SEMIOPEN"): semi_open_seq_count+=1
    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range (8):
        holder=detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count+=holder[0]
        semi_open_seq_count+=holder[1]
        #vertical
        holder=detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count+=holder[0]
        semi_open_seq_count+=holder[1]
        #horizontal
    for i in range (1,7):
        holder=detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count+=holder[0]
        semi_open_seq_count+=holder[1]
        #top left to bottom right from left side
        holder=detect_row(board, col, 0, i, length, 1, 1)
        open_seq_count+=holder[0]
        semi_open_seq_count+=holder[1]
        #top left to bottom right from top side
    open_seq_count+=detect_row(board, col, 0, 0, length, 1, 1)[0]
    semi_open_seq_count+=detect_row(board, col, 0, 0, length, 1, 1)[1]
    for i in range (1,7):
        holder=detect_row(board, col, i, 7, length, 1, -1)
        open_seq_count+=holder[0]
        semi_open_seq_count+=holder[1]
        #top left to bottom right from right side
        holder=detect_row(board, col, 0, i, length, 1, -1)
        open_seq_count+=holder[0]
        semi_open_seq_count+=holder[1]
        #top left to bottom right from top side
    open_seq_count+=detect_row(board, col, 0, 7, length, 1, -1)[0]
    semi_open_seq_count+=detect_row(board, col, 0, 7, length, 1, -1)[1]
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    max=[[0,0],-999999999999999]
    for i in range (8):
        for j in range(8):
            if board[i][j]==" ":
                board[i][j]="b"
                if score(board)>max[1]:
                    max[0]=[i,j]#y,x
                    max[1]=score(board)
                board[i][j]=" "
    return max[0][0], max[0][1]
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])
















def detect_row5(board, col, y_start, x_start, d_y, d_x):
    count5=0
    lastColor=None
    while not (y_start>7 or y_start<0 or x_start>7 or x_start<0):
        if lastColor==None and board[y_start][x_start]==col:
            lastColor=col
        elif lastColor==col and board[y_start][x_start]!=col:
            lastColor=None
            if(is_bounded(board, y_start-d_y, x_start-d_x, 5, d_y, d_x)=="OPEN" or
            is_bounded(board, y_start-d_y, x_start-d_x, 5, d_y, d_x)=="CLOSED" or 
            is_bounded(board, y_start-d_y, x_start-d_x, 5, d_y, d_x)=="SEMIOPEN"
            ): count5+=1
        y_start+=d_y
        x_start+=d_x
    if lastColor==col:
        if(is_bounded(board, y_start-d_y, x_start-d_x, 5, d_y, d_x)=="OPEN" or
            is_bounded(board, y_start-d_y, x_start-d_x, 5, d_y, d_x)=="CLOSED" or 
            is_bounded(board, y_start-d_y, x_start-d_x, 5, d_y, d_x)=="SEMIOPEN"
            ): count5+=1
    return count5
def detect_rows5(board, col):
    count5=0
    for i in range (8):
        holder=detect_row5(board, col, 0, i, 1, 0)
        count5+=holder
        #vertical
        holder=detect_row5(board, col, i, 0, 0, 1)
        count5+=holder
        #horizontal
    for i in range (1,7):
        holder=detect_row5(board, col, i, 0, 1, 1)
        count5+=holder

        #top left to bottom right from left side
        holder=detect_row5(board, col, 0, i, 1, 1)
        count5+=holder

        #top left to bottom right from top side
    count5+=detect_row5(board, col, 0, 0, 1, 1)
    for i in range (1,7):
        holder=detect_row5(board, col, i, 7, 1, -1)
        count5+=holder

        #top left to bottom right from right side
        holder=detect_row5(board, col, 0, i, 1, -1)
        count5+=holder

        #top left to bottom right from top side
    count5+=detect_row5(board, col, 0, 7, 1, -1)
    return count5
def is_win(board):
    if detect_rows5(board, "w")!=0:
        return("White won")
    elif detect_rows5(board, "b")!=0:
        return("Black won")
    elif is_full(board):
        return("Draw")
    else:
        return("Continue playing")

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    """
    board[1][2]="b"
    board[2][3]="w"
    board[3][4]="w"
    board[4][5]="w"
    board[5][6]="w"
    board[6][7]="w"
    """
    
    return board
                


def analysis(board):
   
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i)
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            #print (game_res)
            return game_res
        
        #print (game_res)
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    play_gomoku(8)
    