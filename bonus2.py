import random

def guessing_game():
    secret_number = random.randint(1, 20)
    attemps = 0
    max_attempts = 7

    print("Welcome to My guessing game! Try and guess the number I'm thinking of.")
    
for attempts_taken in range(1, max_attempts + 1):
    guess = int(input(f"Attemps {attempts_taken}/{max_attempts}: Enter your guess:"))
    if guess < secret_number:
        print("To low")
    elif guess > secret_number:
        print("Too High!")
    else:
        print(f"Congratulations! You guessed ({secret_number}) in only {attempts_taken} attempts! Wow!")
        break
            
        attempts += 1

        if attempts == max_attempts:
            print(f"What! You had {max_attempts} and you wasted it! How!? The number was {secret_number}")

            guessing_game()