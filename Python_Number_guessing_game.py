import random

lowest_num = 0
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("---- Python Number Guessing Game ----")
print(f"You need to select a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("Enter your number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < 0 or guess > 100:
            print("That number is out of range.")
            print(f"Please select a number between {lowest_num} and {highest_num}.")

        elif guess < answer:
            print("TOO LOW! Try again.")
        elif guess > answer:
            print("TOO HIGH! Try again.")
        else:
            print(f"CORRECT! The answer is {answer}.")
            print(f"That takes you {guesses} guesses.")
            is_running = False

    else:
        print("Thats not a valid number.")
        print(f"Please select a number between {lowest_num} and {highest_num}.")