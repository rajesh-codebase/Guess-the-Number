import random
target = random.randint(1,100)

while True:
    userChoice = input("Guess the target between '1 to 100' or 'QUIT' :") 
    if(userChoice == "QUIT"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess !!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a biger guess..")
    else:
        print("your number was too big. Take a smaller guess..")

print("---GAME OVER---")
