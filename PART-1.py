# PART 1:
# A program that plays a game of m, n, k-Tic-tac-toe with a user. At the beginning the user chooses the values of m, n, k, and the type of AI that they will play against. 
# Each round, the game prints our the state of the board, asks the user where they would like to place their mark, and implements this decision. Once one of the player won, 
# the program declares the result and asks if the user would like to continue. The first player is selected at random. Here, m is the number of rows, n is the number of 
# columns, and k is the length of the sequence of marks arranged horizontally, vertically, or diagonally that constitutes a win.

import random;
import numpy as np;

# class to display board and operatte the first player for game 
class display:
    
    # display game board iterating though each row and column 
    def display_board(self):
        print(" ", end = " ");
        for i in range (n):
            print(i, end = " ");
        print();
        for i in range (m):
            print(i, end = " ")
            for j in range (n):
                print(board[i][j], end = " ");
            print();
        print();
    
    # passing the random int of first player(0 or 1)
    def first_player_message(self, first_player):
        self.display_board(); # To give the idea of the board of game
        
        # display message for first move according to the random int
        if first_player == 0:
            print("First player is computer.");
        else:
            print("You are the first player.");

class checking:
    
    # passing the row and column value of the move with their respective mark/sign
    def check_winner(self, i, j, sign):
        # count list 
        count = [0, 0, 0, 0, 0, 0, 0, 0];
        
        # passing move position with sign and count list 
        # calcualte is a stand alone function to be used by other classes easily 
        count = calculate(i, j, sign, count);
        
        # after recieving the count list; summing the vertical, horizontal and diagonal total marks and comparing it with k
        # count[0 + 1] = vertical sequence: count[2 + 3] = horizontal sequence: count[4 + 5] = diagonal left: count[6 + 7] = diagonal right
        if count[0] + count[1] >= k-1 or count[2] + count[3] >= k-1 or count[4] + count[5] >= k-1 or count[6] + count[7] >= k-1:
            return sign;
        else: # no win condition: go to check_tie
            return self.check_tie();
    
    # if any spot in board vacant: return '' else return tie
    def check_tie(self):
        for i in range(m):
            for j in range(n):
                if board[i][j] == '_':
                    return "";
        return "tie";

# For this problem we will implement three types of AI:
# inherites the checking class (contain winner and tie methods)
class moves(checking):
    def user_move(self):
        # infinte loop
        while True:
            # taking row and column number as input from the user 
            i,j = [int(x) for x in input("Enter row number and column number separted by space starting with 0: ").split()];
            
            # if move made is available and vacant: mark X in the board
            if i < m and j < n and board[i][j] == '_':
                board[i][j] = 'X';
                
                # goes to check_winner by passing the position and sign = X
                return self.check_winner(i,j,'X');
            
            # else if index beyong board limit: dispplay invalid
            elif i >= m or j >= n:
                print("Invalid index of input. Enter again.");
            else:
                print("Already occupied. Enter again.");
                
    # AI Level 0. The program then places its own mark on a randomly chosen available position.
    def comp_move_level0(self):
        while True:
            
            # choosing available moves randomly
            i = random.randint(0, m - 1); 
            j = random.randint(0, n - 1);
            
            # if the spot is available: place it's mark i.e. O
            if board[i][j] == '_':
                board[i][j] = 'O';
                
                # goes to check_winner method of checking class. passing the move made row and column position with the o sign
                return self.check_winner(i,j,'O');      

    # AI Level 1. The program checks if it can win by placing its mark in any of the available positions. If so, it makes the winning move. Otherwise, it places its mark 
    #              on a randomly chosen available position.
    # AI Level 2. The program checks if it can win by placing its mark in any of the available positions. If so, it makes the winning move. If not, it checks if the opponent
    #             can win the game on the next move by placing their mark on one of the available positions. If so, it blocks that position with its own mark. Otherwise, it
    #             places its mark on a randomly chosen available position.
    
    '''Combined function for AI level 1 and 2 for make the code more efficient'''
    def comp_move_level_1_2(self, sign):
        for i in range(m):
            for j in range(n):
                # if vacant board at i and j
                if board[i][j] == '_':
                    count = [0, 0, 0, 0, 0, 0, 0, 0];
                    
                    # same as level 0 
                    count = calculate(i, j, sign, count)
                    # combination same as level 0
                    if count[0]+count[1] == k-1 or count[2]+count[3] == k-1 or count[4]+count[5] == k-1 or count[6]+count[7] == k-1:
                        # make winning move
                        board[i][j] = 'O';
                        
                        # return O if computer win
                        if sign == 'O':
                            return 'O';
                        # return X if user might win
                        else:
                            return 'X';

'''Stand alone function that calcualtes all the winning possibilities'''
def calculate(i, j, sign, count):
    
    # vertically up count[0]
    # condition so that i does not go beyond 0th row 
    if i - k + 1 >= 0:
        # moving vertically up by 1 step each. from position one above ith row till 0th row. 
        
        for x in range(i-1, i-k, -1):
            # if all rows for same column  has same sign, then increase by 1 in count list's 0th position
            
            if board[x][j] == sign:
                count[0] += 1;
            # if any other sign in between: terminate loop
            else:
                break;
    else: # if i goes beyong 0th row
        
        # then run the loop from one abve the i row till 0 upwards
        for x in range(i-1, -1, -1):
            if board[x][j] == sign:
                count[0] += 1;
            else:
                break;
    
    # vertically down count[1]
    # same as vertical up but till the mth row. 
    if i + k -1 < m: 
        for x in range(i+1,i+k):
            if board[x][j] == sign:
                count[1] += 1;
            else:
                break;
    else: # if i is beyond mth row
        # execute the loop till the last row
        for x in range(i + 1, m):
            # if all rows for same column has same sign: increment count's 1th value
            if board[x][j] == sign:
                count[1] += 1;
            # if anyother sign in between: terminate loop
            else:
                break;

    # horizontally left count[2]
    # similar to vertical hcecking: if column not beyond 0
    if j - k + 1 >= 0: 
        # iterating each step back by -1 to the left of the columns till 0th column
        for x in range(j-1, j-k, -1):
            # if same sign for same row and all the columns: increase count's 2nd element by 1
            if board[i][x] == sign:
                count[2] += 1;
            # if any other sign: terminate
            else:
                break;
    # if the column goes beyond 0
    else:
        # execute the loop from till 0th column
        for x in range(j-1, -1, -1):
            # same sign for same row all columns
            if board[i][x] == sign:
                count[2] += 1;
            else:
                break;

    # horizontally right count[3]
    # all goes same as horizontal right, just go till the last column to right most 
    if j + k - 1 < n: 
        for x in range(j + 1, j + k):
            if board[i][x] == sign:
                count[3] += 1;
            else:
                break;
    else: # if beyond column limit
        for x in range(j+1,n):
            if board[i][x] == sign:
                count[3] += 1;
            else:
                break;

    # diagonally left up count[4]
    # combining the logic for vertical up and horizontal left together 
    if i - k + 1 >= 0 and j - k + 1 >= 0: 
        # going vertically and horizontally left together
        for x,y in zip(range(i-1, i-k, -1),range(j-1, j-k, -1)):
            if board[x][y] == sign:
                count[4] += 1;
            # if any other sign found: terminate loop
            else:
                break;
    else: # if diagonal goes beyond extreme left diagonally
        for x,y in zip(range(i-1, -1, -1),range(j-1, -1, -1)):
            if board[x][y] == sign:
                count[4] += 1;
            else:
                break;

    # diagonally right down count[5]
    # combining logic for verticaldown  and horizaontal right
    if i+k-1 < m and j+k-1 < n: 
        for x,y in zip(range(i+1, i+k),range(j+1, j+k)):
            if board[x][y] == sign:
                count[5] += 1;
            else:
                break;
    else:
        for x,y in zip(range(i+1, m),range(j+1, n)):
            if board[x][y] == sign:
                count[5] += 1;
            else:
                break;
                
    # diagonally left down count[6]
    # combining vertical down and horizontal left
    if i + k - 1 < m and j - k + 1 >= 0: 
        for x,y in zip(range(i+1, i+k),range(j-1, j-k, -1)):
            if board[x][y] == sign:
                count[6] += 1;
            else:
                break;
    else:
        for x,y in zip(range(i+1, m),range(j-1, -1, -1)):
            if board[x][y] == sign:
                count[6] += 1;
            else:
                break;

    # diagonally right up count[7]
    # combining for vertical up and horizontal right
    if i-k+1 >= 0 and j+k-1 < n: 
        for x,y in zip(range(i-1,i-k,-1),range(j+1,j+k)):
            if board[x][y] == sign:
                count[7] += 1;
            else:
                break;
    else:
        for x,y in zip(range(i-1,-1,-1),range(j+1,n)):
            if board[x][y] == sign:
                count[7] += 1;
            else:
                break;
    # return the count list with the incremented elements 
    return count;


# infinite loop
while True:
    print("New Tic-Tac-Toe match begins.") # First message for the player to see
    m = int(input("Enter the number of rows: ")); # the board with m rows
    n = int(input("Enter the number of columns: ")); # board with n columns 
    k = int(input("Enter the length of the sequence of marks arranged horizontally, vertically, or diagonally that constitutes a win: "));
    l = int(input("Enter the type of AI that they will play against (0,1,2): ")); # level of AI with which user wants to compete
    print();
    
    # instance for display class created 
    d = display();
    # instance for moves class created 
    t = moves();

    # to store the end result for iether of the player's win or tie 
    result = "";

    # board created of m*n dimension
    board = np.full((m,n), '_');
    first_player = random.randint(0,1); # random first player 

    # if AI level 0 
    if l == 0:

        # calling first_player_message method using object d of display class. Passing the randomly selected first player
        d.first_player_message(first_player);

        while True:

            # we assign computer first player if the random int is 0
            if first_player == 0:

                # entering computer level 0 method of moves class 
                result = t.comp_move_level0();
                
                d.display_board();
                
                # if after making the move and recieving no win or tie message: switch player to user
                if result == "":
                    # same as computer: go to user_move method of moves class called using t object
                    result = t.user_move();
            
            # if first player random int 1        
            elif first_player == 1:
                
                # user makes the first move: calls the user_move function of moves class
                result = t.user_move();
                # if no declared result: switch player to computer
                if result == "":
                    result = t.comp_move_level0();
                    d.display_board();
                    
            # after each move: check win and tie
            # if result is O: declare computer won
            if result == 'O':
                print("Computer won this time.");
                break;
                
            # if result is X: declare user won
            elif result == 'X':
                d.display_board();
                print("Yayy! You won.");
                break;
                
            # if result is tie: declare match tie
            elif result == "tie":
                if first_player == 1:
                    d.display_board();
                print("Match Tied.");
                break;
                
    # if AI level 1 selected
    elif l == 1:
        
        # evaluate the first player randomly 
        d.first_player_message(first_player);
        
        # infinite loop
        while True:
            # if random int is 0: 
            if first_player == 0:
                # if computer has winning move: result is O
                if t.comp_move_level_1_2('O') == 'O':
                    result = 'O';
                    
                # else make the computer move random as AI level 0
                else:
                    result = t.comp_move_level0();
                d.display_board();
                
                # if result is '': switch player to user player
                if result == "":
                    result = t.user_move();
            
            # if random player in 1: user moves first
            elif first_player == 1:
                result = t.user_move();
                # check result: if nothing, go for ai level 1 result checking
                if result == "":
                    if t.comp_move_level_1_2('O') == 'O':
                        result = 'O';
                    else:
                        result = t.comp_move_level0();
                    d.display_board();
                    
            # if result has O: computer won
            if result == 'O':
                print("Computer won this time.");
                break;
                
            # if result has X: user won
            elif result == 'X':
                d.display_board();
                print("Yayy! You won.");
                break;
                
            # if result has tie: match tie
            elif result == "tie":
                if first_player == 1:
                    d.display_board();
                print("Match Tied.");
                break;
                
    # if AI level 2
    elif l == 2:
        
        # choose first player randomly
        d.first_player_message(first_player);
        
        while True:
            # if first player is 0: computer plays first
            if first_player == 0:
                # if this method returns O: result is ) win
                if t.comp_move_level_1_2('O') == 'O':
                    result = 'O';
                elif t.comp_move_level_1_2('X') == 'X':
                    pass;
                # if nothing returned: make random move 
                else:
                    result = t.comp_move_level0();
                d.display_board();
                
                # if no reult yet: switch player to user
                if result == "":
                    result = t.user_move();
                    
            # if first player int is 1: user moves first
            elif first_player == 1:
                # execute the user_move method of moves class
                result = t.user_move();
                if result == "":
                    if t.comp_move_level_1_2('O') == 'O':
                        result = 'O';
                    elif t.comp_move_level_1_2('X') == 'X':
                        pass;
                    else:
                        result = t.comp_move_level0();
                    d.display_board();
            
            # if result is O: computer won
            if result == 'O':
                print("Computer won this time.");
                break;
                
            # if result is X: user won
            elif result == 'X':
                d.display_board();
                print("Yayy! You won.");
                break;
            # if tie: match tie
            elif result == "tie":
                if first_player == 1:
                    d.display_board();
                print("Match Tied.");
                break;
    
    # if any other level except 0, 1 and 2: invalid level
    else:
        print("Invalid Level.");
        
    # replay
    c = input("Wanna play again? Enter 'Y' or 'y' to play again, or anything else to quit: ");
    if c != 'Y' and c != 'y':
        print("Bye!");
        break;
    print();
    
