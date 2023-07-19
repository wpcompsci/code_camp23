#BASIC FUNCTION DUNGEON

def start_room():
    print("You have entered the start room.")
    print("You can go (n)orth, (e)ast, or (w)est.")
    next = input("Which way will you go? ")
    return next

def east_room():
    print("You have entered the east room.")
    print("You can go back to (s)tart.")
    next = input("Which way will you go? ")
    return next

def west_room():
    print("You have entered the west room.")
    print("You can go to the (s)tart or (f)urther west.")
    next = input("Which way will you go? ")
    return next

def north_room():
    print("You have entered the north room.")
    print("You can go to the(s)tart.")
    next = input("Which way will you go? ")
    return next

def dragon_room():
    print("You entered a room with a dragon.\n"
          "He eats you.\n"
          "Game over.")
    return "dead"

room = "s"

while True:
    if room == "s":
        room = start_room()
    elif room == "w":
        room = west_room()
    elif room == "n":
        room = north_room()
    elif room == "e":
        room = east_room()
    elif room == "f":
        room = dragon_room()
    elif room == "dead":
        break
