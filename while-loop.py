import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1, 10)

isGuessRight = False

while not isGuessRight:
    guess = input("Guess a number between 1 and 10: (Type 'exit' to exit) ")
    
    if guess.lower() == 'exit':
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == number:
        print(f"You guessed {guess}. That's correct! You win!")
        isGuessRight = True
        
    else:
        print(f"You guessed {guess}. You're silly! The number was {number}. Try again!!!")


print("Count to 10!")

for i in range (0, 11):
    print(i, end=', ' )
    