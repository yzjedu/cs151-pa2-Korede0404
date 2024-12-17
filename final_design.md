# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

* Purpose: Allows the CPU to take sticks when it's its turn
* Name: cpu_turn
* Parameter(s): Amount of sticks currently on the table
* Return: Number of sticks taken
* Algorithm:
    1. Create variable choice and set it equal to a random number between 1 and 3 inclusive
    2. If the amount of sticks is either or 4 or 5
       1. return 3
    3. Otherwise, if the amount of sticks is 3
       1. return 2
    4. Otherwise, if the amount of sticks is 2 or 1
       1. return 1
    5. Otherwise
       1. return choice


* Purpose: Allows the current player to take sticks when it's their turn
* Name: player_turn
* Parameter(s): None
* Return: Number of sticks taken
* Algorithm:
    1. Ask player 1 to input either 1, 2, or 3 and set it to variable choice
    2. While the number inputted does not equal 1, 2, or 3
       1. Input error message and ask player 1 to input either 1, 2, or 3
    3. Return choice

* Purpose: Displays 