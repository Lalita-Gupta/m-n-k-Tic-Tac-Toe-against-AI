# PART 2: 
# This part builds upon Part 1. AI0 makes random moves. AI1 checks if there are winning moves and makes them. AI2 does what AI1 does and also prevents the opponent 
# from winning on the next move if possible. We will play these strategies against each other.
# Choose the versus then just sit back and enjoy the show of Tic Tac Toe AI vs AI.

import random;
import numpy as np;

# class to display board and operatte the first player for game 
class display:
    
    # display game board bu iterating though each row and column 
    def display_board(self):
        print(" ", end = " ");
        for i in range (n):
            print(i, end = " ");
        print();
        for i in range (m):
            print(i, end = " ");
            for j in range (n):
                print(board[i][j], end = " ");
            print();
        print();
    
    # passing the random int of first player(0 or 1)
    def first_player_message(self, first_player):
        self.display_board(); # To give the idea of the board of game
        
        # display message for first move according to the random int
        if first_player == 0:
            print("First player is AI Level 0."); 
        elif first_player == 1:
            print("First player is AI Level 1.");
        elif first_player == 2:
            print("First player is AI Level 2.");


# same as part 1: cheacking for all possible winning sequences; if not :match tie
class checking:
    def check_winner(self, i, j, sign):
        #count list 
        count = [0, 0, 0, 0, 0, 0, 0, 0];
        
        # passing move position with sign and count list 
        # calcualte is a stand alone function to be used by other classes easily 
        count = calculate(i, j, sign, count);
        
        # after recieving the count list; summing the vertical, horizontal and diagonal total marks and comparing it with k
        # count[0 + 1] = vertical sequence: count[2 + 3] = horizontal sequence: count[4 + 5] = diagonal left: count[6 + 7] = diagonal right
        if count[0] + count[1] >= k-1 or count[2] + count[3] >= k-1 or count[4] + count[5] >= k-1 or count[6] + count[7] >= k-1:
            return sign;
        else:
            return self.check_tie();
        
    def check_tie(self):
        for i in range(m):
            for j in range(n):
                if board[i][j] == '_':
                    return "";
        return "tie";

# the strategy for each AI level is build in different methods within the moves class. The class also inherits checking class
class moves(checking):
    
    # AI level 0 makes random moves at available spot
    def comp_move_level0(self, sign):
        while True:
            i = random.randint(0, m - 1); 
            j = random.randint(0, n - 1);
            if board[i][j] == '_':
                board[i][j] = sign;
                return self.check_winner(i,j,sign);      
    
    # AI level 1 tries and makes winning moves 
    def comp_move_level_1(self, sign):
        for i in range(m):
            for j in range(n):
                if board[i][j] == '_':
                    count = [0, 0, 0, 0, 0, 0, 0, 0];
                    count = calculate(i, j, sign, count);
                    if count[0]+count[1] == k-1 or count[2]+count[3] == k-1 or count[4]+count[5] == k-1 or count[6]+count[7] == k-1:
                        board[i][j] = sign;
                        return sign;
        return "";
    
    # AI level 2 tries to block the winning move of the opponent and makes the winning moves as well
    def comp_move_level_2(self, sign, opp_sign):
        for i in range(m):
            for j in range(n):
                if board[i][j] == '_':
                    count = [0, 0, 0, 0, 0, 0, 0, 0];
                    count = calculate(i, j, sign, count);
                    if count[0]+count[1] == k-1 or count[2]+count[3] == k-1 or count[4]+count[5] == k-1 or count[6]+count[7] == k-1:
                        board[i][j] = opp_sign;
                        return sign;
        return "";

'''Stand alone function that calcualtes all the winning possibilities'''
# same as PART-1 
def calculate(i, j, sign, count):
    # vertically up count[0]
    if i - k + 1 >= 0:
        for x in range(i-1, i-k, -1):
            if board[x][j] == sign:
                count[0] += 1;
            else:
                break;
    else:
        for x in range(i-1, -1, -1):
            if board[x][j] == sign:
                count[0] += 1;
            else:
                break;
    
    # vertically down count[1]
    if i + k -1 < m: 
        for x in range(i+1, i+k):
            if board[x][j] == sign:
                count[1] += 1
            else:
                break;
    else:
        for x in range(i + 1, m):
            if board[x][j] == sign:
                count[1] += 1;
            else:
                break;

    # horizontally left count[2]
    if j - k + 1 >= 0: 
        for x in range(j-1, j-k, -1):
            if board[i][x] == sign:
                count[2] += 1;
            else:
                break;
    else:
        for x in range(j-1, -1, -1):
            if board[i][x] == sign:
                count[2] += 1;
            else:
                break;

    # horizontally right count[3]
    if j + k - 1 < n: 
        for x in range(j + 1, j + k):
            if board[i][x] == sign:
                count[3] += 1;
            else:
                break;
    else:
        for x in range(j+1,n):
            if board[i][x] == sign:
                count[3] += 1;
            else:
                break;

    # diagonally left up count[4]
    if i - k + 1 >= 0 and j - k + 1 >= 0: 
        for x,y in zip(range(i-1, i-k, -1),range(j-1, j-k, -1)):
            if board[x][y] == sign:
                count[4] += 1;
            else:
                break;
    else:
        for x,y in zip(range(i-1, -1, -1),range(j-1, -1, -1)):
            if board[x][y] == sign:
                count[4] += 1;
            else:
                break;

    # diagonally right down count[5]
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
    return count;

'''Each of the 3 VS set cominations are created in 3 different functions (AI1 VS AI0), (AI2 VS AI0) and (AI2 VS AI1)'''
# the way of calling is most important: different for different combinations 
# at the entry in the functions, instances of move and checking are created 
# at the end: the result stores which Ai won or if tie. 

# ai1 vs ai0
def ai1_vs_ai0():
    t = moves();
    first_player = random.choice([0,1]);
    d.first_player_message(first_player);
    while True:
        if first_player == 0:
            result = t.comp_move_level0('0');
            d.display_board();
            
            if result == "":
                if t.comp_move_level_1('1') == '1':
                    result = '1';
                else:
                    result = t.comp_move_level0('1');
                    d.display_board();
                
        elif first_player == 1:
            if t.comp_move_level_1('1') == '1':
                result = '1';
            else:
                result = t.comp_move_level0('1');
                d.display_board();
            
            if result == "":
                result = t.comp_move_level0('0');
                d.display_board();
                
        #check which Ai won 0/1/tie
        if result == '0':
            return result;
        elif result == '1':
            d.display_board();
            return result;
        elif result == "tie":
            return result;
        
# ai2 vs ai0
def ai2_vs_ai0():
    t = moves();
    c = checking();
    first_player = random.choice([0,2]);
    d.first_player_message(first_player);
    while True:
        if first_player == 0:
            result = t.comp_move_level0('0');
            d.display_board();
            
            if result == "":
                if t.comp_move_level_1('2') == '2':
                    result = '2';
                elif t.comp_move_level_2('0','2') == '0':
                    result = c.check_tie();
                    d.display_board();
                else:
                    result = t.comp_move_level0('2');
                    d.display_board();
                
        elif first_player == 2:
            if t.comp_move_level_1('2') == '2':
                result = '2';
            elif t.comp_move_level_2('0','2') == '0':
                result = c.check_tie();
            else:
                result = t.comp_move_level0('2');
                d.display_board();
            
            if result == "":
                result = t.comp_move_level0('0');
                d.display_board();
                
        #check which Ai won 0/2/tie
        if result == '0':
            return result;
        elif result == '2':
            d.display_board();
            return result;
        elif result == "tie":
            return result;
        
# ai2 vs ai1
def ai2_vs_ai1():
    t = moves();
    c = checking();
    first_player = random.randint(1,2);
    d.first_player_message(first_player);
    while True:
        if first_player == 1:
            if t.comp_move_level_1('1') == '1':
                result = '1';
            else:
                result = t.comp_move_level0('1');
            d.display_board();
            
            if result == "":
                if t.comp_move_level_1('2') == '2':
                    result = '2';
                elif t.comp_move_level_2('1','2') == '1':
                    result = c.check_tie();
                else:
                    result = t.comp_move_level0('2');
                d.display_board();
                    
        elif first_player == 2:
            if t.comp_move_level_1('2') == '2':
                result = '2';
            elif t.comp_move_level_2('1','2') == '1':
                result = c.check_tie();
            else:
                result = t.comp_move_level0('2');
            d.display_board();
                
            if result == "":
                if t.comp_move_level_1('1') == '1':
                    result = '1';
                else:
                    result = t.comp_move_level0('1');
                d.display_board();
                    
        #check which Ai won 2/1/tie
        if result == '1':
            return result;
        elif result == '2':
            #d.display_board();
            return result;
        elif result == "tie":
            #d.display_board();
            return result;
        

# infinite loop
while True:
    print("New Tic-Tac-Toe match begins."); # First message for the player to see
    m = int(input("Enter the number of rows: ")); # the board with m rows
    n = int(input("Enter the number of columns: ")); # board with n columns 
    k = int(input("Enter the length of the sequence of marks arranged horizontally, vertically, or diagonally that constitutes a win: "));
    choice = int(input("Enter the type of AI that they will play against each other: 1 for AI1 vs AI0, 2 for AI2 vs AI9 and 3 for AI2 vs AI1: ")); #levels of AI user wants to compete each other.
    print();
    
    # instance for display class created 
    d = display();
    # instance for moves class created 
    t = moves();

    # to store the end result for iether of the player's win or tie 
    result = "";

    # board created of m*n dimension
    board = np.full((m,n), '_'); # creating standard board of m*n as per case 

    # if AI level 0 
    if choice == 1:
        result = ai1_vs_ai0();
        if result == '1':
            print("Level 1 won this time.");
        elif result == '0':
            print("Level 0 won this time.");
        elif result == "tie":
            print("Match Tied.");
            
    elif choice == 2:
        result = ai2_vs_ai0();
        if result == '2':
            print("Level 2 won this time.");
        elif result == '0':
            print("Level 0 won this time.");
        elif result == "tie":
            print("Match Tied.");
        
    elif choice == 3:
        result = ai2_vs_ai1()
        if result == '2':
            print("Level 2 won this time.");
        elif result == '1':
            print("Level 1 won this time.");
        elif result == "tie":
            print("Match Tied.");
            
    # if any other level except 0, 1 and 2: invalid level
    else:
        print("Invalid Level.");
        
    # replay
    c = input("Wanna play again? Enter 'Y' or 'y' to play again, or anything else to quit: ");
    if c != 'Y' and c != 'y':
        print("Bye!");
        break;
    print();
    
