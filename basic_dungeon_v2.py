#BASIC FUNCTION DUNGEON

def start_room():
    print("You have entered the start room.")
    print("You can go (n)orth, (e)ast, or (w)est.")
    next = input("Which way will you go? ")
    if next == "n":
        north_room()
    elif next == "e":
        east_room()
    elif next == "w":
        west_room()
    else:
        print("Invaild option!\n")
        start_room()

def east_room():
    print("You have entered the east room.")
    print("You can go (w)est.")
    next = input("Which way will you go? ")
    if next == "w":
        start_room()
    else:
        print("Invaild option!\n")
        east_room()

def west_room():
    print("You have entered the west room.")
    print("You can go to the (e)ast or (w)est.")
    next = input("Which way will you go? ")
    if next == "w":
        dragon_room()
    elif next == "e":
        start_room()
    else:
        print("Invaild option!\n")
        west_room()

def north_room():
    print("You have entered the north room.")
    print("You can go to the(s)outh.")
    next = input("Which way will you go? ")
    if next == "s":
        start_room()
    else:
        print("Invaild option!\n")
        north_room()

def dragon_room():
    print("You entered a room with a dragon.\n"
          "He eats you.\n"
          "Game over.")
    input("Press enter to close the game.")

start_room()


