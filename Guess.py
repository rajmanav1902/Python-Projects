import random
import time

#Get the range from the user
start,end=map(int,input("Enter the start and end of the range ").split())

#Validate start and end
if start==end:
    print("The start and end of range must be different ")
elif start>end:
    print("Enter a valid range ")
else:
    #Generate a random number in given range
    number=random.randint(start,end)

    #Decide the difficulty level
    print("Select the difficulty level : Easy , Medium and Hard ")
    difficulty= input()
    if difficulty not in ["Easy", "Medium", "Hard"]:
        print("Enter a valid difficulty level")
        exit()

    count=0
    attempts=0
    if difficulty== "Easy":
        attempts=15
        print("You have 15 attempts")
    elif difficulty=="Medium":
        attempts=10
        print("You have 10 attempts")
    elif difficulty =="Hard":
        attempts=5
        print("You have 5 attempts")
    else:
        print("Enter a valid difficulty level ")

    print("The Guess game starts")

    #Get the starting time
    start_time=time.time()

    #Loop for the guess
    while attempts>0:
        print()
        guess=int(input(" Make your guess between {} and {}: ".format(start,end)))
        count+=1
        attempts-=1
        if guess>number:
            print(" Your guess is higher than the number ")
        elif guess<number:
            print(" Your guess is lower than the number ")
        else:
            print()
            print("Congratulation! You have guessed the correct number ")
            print("Total time taken: ",time.time()-time.time())
            print("Total attempts taken: ",count)
            break
    print()
    print("Sorry! You have lost the game ")
    print(" {}  is the correct number ".format(number))
