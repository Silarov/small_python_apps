number = input("Number you want to divide: ")

for i in range(0, int(number)):
    print(int(number))
    if (int(number) / (i + 1)) == 0:
        print("Die Nummer " + number +" ist durch " + i + " teilbar")