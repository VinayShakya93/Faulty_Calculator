# Snake, Water and gun
import random
print("Welcome to our game Snake, Water and Gun")
Option = ["snake", "water", "gun"]
s = "snake"
g = "gun"
w = "water"
i = 7
User_score = 0
Computer_score = 0
try:
    while i!=0:
        User = input("Enter your choice: Gun for g, Snake for s and Water for w: ")
        Computer = random.choice(Option)
        i = i-1
        print("Your Chance left is: ", i)
        if (User=="s" and Computer=="snake"):
            print("Game is tie!")
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="g" and Computer=="snake"):
            print("You got a point")
            User_score += 1
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="s" and Computer=="water"):
            print("You got a point")
            User_score += 1
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="s" and Computer=="gun"):
            print("Computer got a point")
            Computer_score += 1
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="w" and Computer=="snake"):
            print("Computer got a point")
            Computer_score += 1
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="g" and Computer=="gun"):
            print("Game is tie!")
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="w" and Computer=="water"):
            print("Game is tie!")
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        elif (User=="w" and Computer=="gun"):
            print("You got a point")
            User_score += 1
            print(f"Your score is: {User_score} and Computer's score is: {Computer_score}, \n", end="")
            print(f"Your choice is: {User} and Computer's choice is: {Computer}\n", end="")
        else:
            print("Input Error")

        if User_score==Computer_score:
            print(f"**Game is tie. Score's are equal**")
        elif User_score>Computer_score:
            print("**You win!!** ")
        else:
            print("**Computer Win!!**")
except Exception as e:
    print("Invalid Input!")

