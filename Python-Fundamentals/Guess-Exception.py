'''Write a program using user defined exception class that will ask the user to enter a number until he guess a stored
number correctly.To help users figure out. Provide a hint whether their gusess is gretaer than or less than the stored
number using user defined exceptions.'''

class GuessException(Exception):
    pass
stored_number=42
while True:
    try:
        guess=int(input("\nGuess the number:"))
        if guess<stored_number:
            raise GuessException("The number you guessed is Smaller.")
        elif guess>stored_number:
            raise GuessException("The number you guessed is larger.")
        else:
            print("Good,Correct Guess!!")
            break
    except ValueError:
        print("\nInvalid input. Please enter a number.")

    except GuessException as e:
        print(e)
