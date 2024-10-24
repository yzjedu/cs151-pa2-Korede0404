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
       6. cpu_lose which equals 0
       7. player_one_sticks which equals 0
       8. player_two sticks which equals 0
       9. cpu_sticks which equals 0
       10. game_status which equals an empty string
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
       2. Convert game_status to lowercase
    10. While game_status is not "end"
        1. Player 1 takes the sticks that they want using the player_one_turn function (the result is set to player_one_sticks)
        2. If sticks is 0
           1. Add 1 to player_one_lose
           2. Print that player one lost using their name
           3. Ask the user if they want to play again (Start or End) and game_status equal to that input
           4. Convert game_status to lowercase
           5. While game_status is not "start" and "end
              1. Output error message and ask the user if they want to play again (Start or End)
              2. Convert game_status to lowercase
        3. Player 2 takes the sticks that they want using the player_two_turn function (the result is set to player_two_sticks)
        4. If sticks is 0
           1. Add 1 to player_two_lose
           2. Print that player two lost using their name
           3. Ask the user if they want to play again (Start or End) and game_status equal to that input
           4. Convert game_status to lowercase
           5. While game_status is not "start" and "end
              1. Output error message and ask the user if they want to play again (Start or End)
              2. Convert game_status to lowercase
        5. Cpu takes the sticks that they want using the cpu_turn function (the result is set to cpu_sticks)
        6. If sticks is 0
           1. Add 1 to cpu_lose
           2. Print that the CPU lost using their name
           3. Ask the user if they want to play again (Start or End) and game_status equal to that input
           4. Convert game_status to lowercase
           5. While game_status is not "start" and "end
              1. Output error message and ask the user if they want to play again (Start or End)
              2. Convert game_status to lowercase