import math

print("=======================================")
print("Hello! Pick a number between 0 and 100!")

solved = False
guess = 50
guessReserve = 50

while solved == False :
    print("Is your number: " + str(guess))
    print("1: Higher")
    print("2: Lower")
    print("3: Correct")

    choice = int(input())

    if choice == 1 :
        guessReserve = guessReserve/2
        guess = guess + math.ceil(guessReserve)
    elif choice == 2 :
        guessReserve = guessReserve/2
        guess = guess - math.ceil(guessReserve)
    elif choice == 3 :
        print("Yay! " + str(guess) + " is your number!")
        solved = True
