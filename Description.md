# Tic-Tac-Toe-against-AI

A program that plays a game of m, n, k-Tic-tac-toe with a user. At the beginning the user chooses the values of m, n, k, and the type of AI that they will play against. 
Each round, the game prints out the state of the board, asks the user where they would like to place their mark, and implements this decision. The program then places 
its own mark on a randomly chosen available position. Once one of the players wins, the program declares the result and asks if the user would like to continue. 
The first player is selected at random.

*The description of the game can be found at https://en.wikipedia.org/wiki/Tic-tac-toe.*

> Designing of this program was done with thinking about what kind of program structure would make it easy to develop extensions such as a more sophisticated AI, an 
> ability to play with another program, or play the game on boards of arbitrary rectangular shape. Also, thinking about objects and classes that would make sense to develop 
> and the three pillars of OOP. However, focus was on the more important task of having a working program that plays regular Tic-tac-toe with a user. 

## PART 1:

A program that plays a game of m, n, k-Tic-tac-toe with a user. At the beginning the user chooses the values of m, n, k, and the type of AI that they will play against. 
Each round, the game prints our the state of the board, asks the user where they would like to place their mark, and implements this decision. Once one of the player wins, 
the program declares the result and asks if the user would like to continue. The first player is selected at random. Here, m is the number of rows, n is the number of columns, 
and k is the length of the sequence of marks arranged horizontally, vertically, or diagonally that constitutes a win.

For this problem we will implement three types of AI:

    • AI Level 0. The program then places its own mark on a randomly chosen available position.
    • AI Level 1. The program checks if it can win by placing its mark in any of the available positions. If so, it makes the winning 
                  move. Otherwise, it places its mark on a randomly chosen available position.
    • AI Level 2. The program checks if it can win by placing its mark in any of the available positions. If so, it makes the winning 
                  move. If not, it checks if the opponent can win the game on the next move by placing their mark on one of the 
                  available positions. If so, it blocks that position with its own mark. Otherwise, it places its mark on a randomly 
                  chosen available position.
                  
## PART 2:

This part builds upon Part 1. AI0 makes random moves. AI1 checks if there are winning moves and makes them. AI2 does what AI1 does and also prevents the opponent from 
winning on the next move if possible. We will play these strategies against each other. 

    Choose the versus then just sit back and enjoy the show of Tic Tac Toe AI vs AI.

## PART 3:

This part builds upon Part 2. This part is addressed for the standard board (m, n, k) = (3, 3, 3), for (m, n, k) = (4, 4, 4), and for (m, n, k) = (4, 3, 3). Some games 
will result in draws. We will count these games towards the total number of games, but not towards winning. Thus, for each scenario will be obtaining two 
winning probabilities. One minus the sum of them will be the probability of a draw. We determine the probabilities of winning for AI1 vs. AI0, AI2 vs. AI0, and 
AI2 vs. AI1. We perform enough simulations for each scenario to determine the smallest probability with 5% accuracy. 
> Explanation is provided in the description.
