
guessed = False
while not guessed:
    guess = input("Guess a Number")
    if int(guess) == 14:
        guessed = True

print("You win!")
