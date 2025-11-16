name = "Alex"
guesses = 0 

while True:
    print("Please, guess my name.")
    guess = input()
    guesses += 1
    if guess == name:
        print("Congratulations! You guessed my name.")
        print("Guesses:", guesses)
        break
    else:
        print("Do you want to quit (y/n)?")
        quit_choice = input().lower()
        if quit_choice == 'y':
            print("You quit the game.")
            break