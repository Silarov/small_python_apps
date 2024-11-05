import random

print("Welcome to your Password Generator")

again = "true"

while(again == "true"):

    #different password-styles
    numbers = "1234567890"
    letters_little = "abcdefghijklmnopqrstuvwxyz"
    letters_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+*ç%&/()=?``!$£-_.:,;"

    number = input('Amount of passwords to generate: ')
    number = int(number)

    length = input('Length of your password: ')
    length = int(length)

    kind = input('kind of password [num, let-s, let-b, let, all]: ')

    print("Here are your passwords: \n")

    for pwd in range(number):
        passwords = ""
        for c in range(length):
            if(kind == "num"):
                passwords += random.choice(numbers)
            elif(kind == "let-s"):
                passwords += random.choice(letters_little)
            elif(kind == "let-b"):
                passwords += random.choice(letters_big)
            elif(kind == "let"):
                passwords += random.choice(letters)
            else:
                passwords += random.choice(chars)
        print(passwords)
    print("")


    againPlayer = "true"
    print('again? [y/n]')

    while(againPlayer == "true"):
        playAgain = input()
        if(playAgain == "n"):
            againPlayer = "false"
            again = "false"
        elif(playAgain == "y"):
            againPlayer = "false"
            print("Generator startet neu...")
        else:
            print("to use the generator again, write 'y'. to exit, write 'n'.")