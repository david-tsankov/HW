'''
Task: Create a Python program for a "Guess the Number" game. The game will generate a random number within a specified range and prompt the user to guess the number. The program provides feedback based on the user's guess - whether it's too high, too low, or correct. The game continues until the user guesses the number correctly.
Requirements:
Random Number Generation: The program should generate a random number within a given range (e.g., 1 to 10). You can use the random.randint(1, 10) method, after including in your code import random
User Input: Prompt the user to enter their guess. Ensure, the user guess is in the range, and if not, display "Your guess is out of bounds."
Feedback to User: After each guess, the program should provide feedback: 
If the guess is too high, display "Too hight!"
If the guess is too low, display "Too low!"
If the guess is correct, display "Congratulations! You guessed it right."
Repeat Guesses: The game should continue, allowing the user to guess again if the guess is incorrect.
Terminate the Game: Once the correct number is guessed, the game should end with message "Bravo, you guessed my number"
Optional - Guess Counter: Keep track of the number of guesses the user makes and display this count when the correct number is guessed.
Bonus Challenge:
Add a feature to limit the number of guesses a user can make. If the user doesn't guess the number within the limit, end the game with a message indicating that the user has lost.
Implement a difficulty level for the game (e.g., easy, medium, hard), where each level has a different range of numbers or a different number of allowed guesses.
'''

import random
def rules():
    print(f"{50*"$":^50}")
    print(f"${"Welcome to Guess the number!":^48}$")
    print(f"{50*"$":^50}")
    print(f"${"Rules:":^48}$")
    print(f"${"Only guess in range of numbers":^48}$")
    print(f"${"Fixed number of guesses based on level":^48}$")
    print(f"${"Really not that many rules, just have fun!":^48}$")
    print(f"{50*"$":^50}")
    print()
    print()
    

def choose_level():
    levels={
        "1":"Easy",
        "2":"Meadium",
        "3":"Hard",
        "4":"Extreme",
        "5":"Legit guessing"
    }
    print(f"{50*"$":^50}")
    print(f"${"Choose your level:":^48}$")
    print(f"${"Easy (1,10), max moves: 7 -> 1":^48}$")
    print(f"${"Medium (1,10), max moves: 5 -> 2":^48}$")
    print(f"${"Hard (1,100), max moves: 9 -> 3":^48}$")
    print(f"${"Extreme (1,100), max moves: 7 -> 4":^48}$")
    print(f"${"Legit guessing (1,1000), max moves: 9 -> 5":^48}$")
    print(f"{50*"$":^50}")
    print()
    
    level=levels[input("Enter level: ")]
    return level


def generating_random_number_easy_medium():
    number=random.randint(1,10)
    return number

def generating_random_number_hard_extreme():
    number=random.randint(1,100)
    return number

def generating_random_number_legit_guessing():
    number=random.randint(1,1000)
    return number

def gameplay_easy():
    number=generating_random_number_easy_medium()
    index=6
    for i in range(0,7):
        guess=int(input("Enter guess: "))
        if guess==number:
            print(f"Congrats, you guessed right!")
            break
        elif guess>number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too high, {index} guesses left!")
        elif guess<number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too low, {index} guesses left!")
        index-=1

def gameplay_medium():
    number=generating_random_number_easy_medium()
    index=4
    for i in range(0,5):
        guess=int(input("Enter guess: "))
        if guess==number:
            print(f"Congrats, you guessed right!")
            break
        elif guess>number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too high, {index} guesses left!")
        elif guess<number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too low, {index} guesses left!")
        index-=1

def gameplay_hard():
    number=generating_random_number_hard_extreme()
    index=8
    for i in range(0,9):
        guess=int(input("Enter guess: "))
        if guess==number:
            print(f"Congrats, you guessed right!")
            break
        elif guess>number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too high, {index} guesses left!")
        elif guess<number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too low, {index} guesses left!")
        index-=1

def gameplay_extreme():
    number=generating_random_number_hard_extreme()
    index=6
    for i in range(0,7):
        guess=int(input("Enter guess: "))
        if guess==number:
            print(f"Congrats, you guessed right!")
            break
        elif guess>number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too high, {index} guesses left!")
        elif guess<number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too low, {index} guesses left!")
        index-=1

def gameplay_legit_guessing():
    number=generating_random_number_legit_guessing()
    index=8
    for i in range(0,9):
        guess=int(input("Enter guess: "))
        if guess==number:
            print(f"Congrats, you guessed right!")
            break
        elif guess>number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too high, {index} guesses left!")
        elif guess<number:
            if index==0:
                print(f"BUahahaha you LOSE!!!")
                break
            print(f"Too low, {index} guesses left!")
        index-=1

def executing_difficulty_based_on_level_chosen():
    level=choose_level()
    if level=="Easy":
        gameplay_easy()
    elif level=="Medium":
        gameplay_medium()
    elif level=="Hard":
        gameplay_hard()
    elif level=="Extreme":
        gameplay_extreme()
    elif level==("Legit guessing"):
        gameplay_legit_guessing()

rules()
executing_difficulty_based_on_level_chosen()
