import random

again = "true"
counter = 0

while(again == "true"):

    import os

    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    clearConsole()

    print("Wie hoch soll die höchste Zahl sein?")

    highestNumber = int(input())


    #creates random number between 1 and your number
    randomNumber = random.randrange(1, highestNumber)

    guessedNumber = "false"

    print("Errate die Nummer zwischen 1 und " + str(highestNumber))
    print("")

    while(guessedNumber == "false"):
        guess = int(input())
        if(guess == randomNumber):
            print("Sie haben die Zahl erraten!")
            guessedNumber = "true"
        elif(guess > randomNumber):
            print("Zahl muss kleiner sein")
        else:
            print("Zahl muss grösser sein")
        print("")
        counter += 1
    print("Sie haben " + str(counter) + " Versuche gebraucht.")
    print("nochmals spielen? [y/n]")

    againPlayer = "true"

    while(againPlayer == "true"):
        playAgain = input()
        if(playAgain == "n"):
            againPlayer = "false"
            again = "false"
        elif(playAgain == "y"):
            counter = 0
            againPlayer = "false"
            print("Spiel startet neu...")
        else:
            print("Um nochmal spielen zu können, schreiben Sie 'y'. Um abzubrechen, schreiben Sie 'n'")

clearConsole()