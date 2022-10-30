n = 18
no_of_guesses = 1
while (no_of_guesses<=7):
    user = int(input("Please enter your expected number\n"))
    if user<18:
        print("You enter lesser number, Please input greater number\n")
    elif user>18:
        print("You enter the greater number, Please enter lesser number\n")
    else:
        print("Congrulations! You win")
        print(no_of_guesses, "no.of guesses he took to finish.")
        break
    print(7-no_of_guesses, "no of gusses left")
    no_of_guesses = no_of_guesses + 1
if no_of_guesses>7:
    print("Game Over!")