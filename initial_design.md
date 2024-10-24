# Initial Design Document

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


* Purpose: Allows player one to take sticks when it's their turn
* Name: player_one_turn
* Parameter(s): None
* Return: Number of sticks taken
* Algorithm:
    1. Ask player 1 to input either 1, 2, or 3 and set it to variable choice
    2. While the number inputted does not equal 1, 2, or 3
       1. Input error message and ask player 1 to input either 1, 2, or 3
    3. Return choice


* Purpose: Allows player two to take sticks when it's their turn
* Name: player_two_turn
* Parameter(s): None
* Return: Number of sticks taken
* Algorithm:
    1. Ask player 2 to input either 1, 2, or 3 and set it to variable choice
    2. While the number inputted does not equal 1, 2, or 3
       1. Input error message and ask player 2 to input either 1, 2, or 3
    3. Return choice


* Purpose: Check if the game has ended
* Name: end_check
* Parameter(s): Number of sticks on the table, the amount of sticks the current player has taken
* Return: True if the number of sticks on the table minus the player's choice is less than or equal to 0 and False if otherwise
* Algorithm:
    1. if the number of sticks on the table minus the player's current choice is less than or equal to 0
        1. return true
    2. Otherwise
       1. Return false


* Purpose: Allow the program to run
* Name: main
* Parameter(s): None
* Return: None
* Algorithm:
    1. Variables to be created
       1. player_one_name which equals an empty string
       2. player_two_name which equals an empty string
       3. table_sticks which equals 0
       4. player_one_lose which equals 0
       5. player_two_lose which equals 0
       6. cpu_wins which equals 0
       7. game_status which equals an empty string
    2. Output intro message welcoming user to the program and introduces the CPU player
    3. Prompt player one to enter their name and set the string equal to player_one_name
    4. Prompt player two to enter their name and set the string equal to player_two_name
    5. Prompt the user(s) to input the amount update table_sticks to this new amount
    6. While table_sticks is not greater than or equal to 10 or less than or equal to 100
       1. Tell the user that their input is invalid and ask them to try again
    7. Ask the user if they want to start the (input "Start" if yes or "End" if no) and set it to game_status
    8. Convert game_status to lowercase
    9. While game_status is not start and end
       1. Tell the user that their input is invalid and ask them to input start or end
    10. While game_status is not "end"
        1. If end_check(table_sticks, player_one_turn) = 0
           1. Add 1 to player_one_lose
           2. Print that player one lost using their name