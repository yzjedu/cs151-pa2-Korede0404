import random

def cpu_turn(sticks_left):
    choice = random.randint(1, 3)
    if sticks_left == 4 or sticks_left == 5:
        return 3
    elif sticks_left == 3:
        return 2
    elif sticks_left == 2 or sticks_left == 1:
        return 1
    return choice

def player_turn():
    choice = int(input("Please input the amount of sticks you want to take (you must take either 1 stick, 2 sticks, or 3 sticks): "))
    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input("You can't take that many sticks, please input the amount of sticks you want to take (you must take either 1 stick, 2 sticks, or 3 sticks): "))
    return choice

def display_name(player_name):
    print(player_name + "'s turn.")

def display_take(name, number, sticks_left):
    if number == 1:
        print(name + " takes " + str(number) + " stick.")
    else:
        print(name + " takes " + str(number) + " sticks.")
    if sticks_left == 1:
        print("There is now " + str(sticks_left) + " stick left.\n")
    else:
        print("There are now " + str(sticks_left) + " sticks left.\n")

def display_score(name1, score1, name2, score2, cpu, score_cpu):
    print("Here are the amount of times each player has lost: ")
    print(name1 + ": " + str(score1))
    print(name2 + ": " + str(score2))
    print(cpu + ": " +  str(score_cpu) + "\n")


def main():
    player_one_lose = 0
    player_two_lose = 0
    cpu_lose = 0

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Hello! Welcome to the Game of Sticks!")
    print("This is a game with two players. Your ")
    print("third player will be the computer himself.")
    print("(This is him) --> *_*")
    print("You can call him 'Comedy.")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    player_one_name = str(input("Player 1, would you please enter your name: "))
    player_two_name = str(input("Player 2, would you please enter your name: "))
    cpu_name = "Comedy"

    print("")

    print("Good to have you both, " + player_one_name + " and " + player_two_name + ".\n")

    table_sticks = int(input("Tell me... how many sticks do you want on the table?: "))
    while table_sticks < 10 or table_sticks > 100:
        table_sticks = int(input("You can't have that many sticks on the table. How many sticks do you want on the table?: "))

    game_status = str(input("Excellent! Are you ready to let the games begin? (Please input either Start or End) "))
    game_status = game_status.lower()
    while game_status != "start" and game_status != "end":
        game_status = str(input("Sorry, that isn't an answer I'm looking for. Are you ready to let the games begin? (Please input either Start or End) "))
        game_status = game_status.lower()

    print("Alright, let's start!")
    print("")
    while game_status != "end":
        display_name(player_one_name)
        take = player_turn()
        table_sticks -= take
        display_take(player_one_name, take, table_sticks)
        if table_sticks <= 0:
            player_one_lose +=1
            print(player_one_name + " has lost.\n")
            display_score(player_one_name, player_one_lose, player_two_name, player_two_lose, cpu_name, cpu_lose)
            game_status = str(input("Would you like to play again? (Please input either Start or End) "))
            game_status = game_status.lower()
            while game_status != "start" and game_status != "end":
                game_status = str(input("Sorry, that isn't an answer I'm looking for. Do you want to play again? (Please input either Start or End) "))
                game_status = game_status.lower()
            print("")
            table_sticks = int(input("How many sticks do you want on the table this time?: "))
            while table_sticks < 10 or table_sticks > 100:
                table_sticks = int(input("You can't have that many sticks on the table. How many sticks do you want on the table?: "))
            print("")
            print("Let's go again!\n")

        display_name(player_two_name)
        take = player_turn()
        table_sticks -= take
        display_take(player_two_name, take, table_sticks)
        if table_sticks <= 0:
            player_two_lose += 1
            print(player_two_name + " has lost.\n")
            display_score(player_one_name, player_one_lose, player_two_name, player_two_lose, cpu_name, cpu_lose)
            game_status = str(input("Would you like to play again? (Please input either Start or End) "))
            game_status = game_status.lower()
            while game_status != "start" and game_status != "end":
                game_status = str(input("Sorry, that isn't an answer I'm looking for. Do you want to play again? (Please input either Start or End) "))
                game_status = game_status.lower()
            print("")
            table_sticks = int(input("How many sticks do you want on the table this time?: "))
            while table_sticks < 10 or table_sticks > 100:
                table_sticks = int(input("You can't have that many sticks on the table. How many sticks do you want on the table?: "))
            print("")
            print("Let's go again!\n")

        display_name(cpu_name)
        take = cpu_turn(table_sticks)
        table_sticks -= take
        display_take(cpu_name, take, table_sticks)
        print("")
        if table_sticks <= 0:
            cpu_lose += 1
            print("Comedy has lost.\n")
            display_score(player_one_name, player_one_lose, player_two_name, player_two_lose, cpu_name, cpu_lose)
            game_status = str(input("Would you like to play again? (Please input either Start or End) "))
            game_status = game_status.lower()
            while game_status != "start" and game_status != "end":
                game_status = str(input("Sorry, that isn't an answer I'm looking for. Do you want to play again? (Please input either Start or End) "))
                game_status = game_status.lower()
            table_sticks = int(input("Tell me... how many sticks do you want on the table?: "))
            print("")
            while table_sticks < 10 or table_sticks > 100:
                table_sticks = int(input("You can't have that many sticks on the table. How many sticks do you want on the table?: "))
            print("")
            print("Let's go again!\n")
    print("Thank you for playing the Game of Sticks")

main()