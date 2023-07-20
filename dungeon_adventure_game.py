# Import the random module for generating random numbers
import random
# Import the os module for interacting with the operating system
import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to simulate a battle with an enemy
def battle(player, enemies):
    # Clear the screen
    clear_screen()
    # Randomly select an enemy from the enemies dictionary
    enemy = random.choice(list(enemies))
    # Store the enemy's original health
    enemy_original_health = enemies[enemy]['health']
    # Print a message to inform the player about the enemy they encountered
    print('You have encountered a ' + enemies[enemy]['name'])
    # Continue the battle while both the player and the enemy are alive
    while enemies[enemy]['health'] > 0 and player['health'] > 0:
        # Print the player's and the enemy's current health
        print('You have ' + str(player['health']) + ' health.')
        print('The ' + enemies[enemy]['name'] + ' has ' + str(enemies[enemy]['health']) + ' health.')
        # Ask the player what they want to do (swing or charge)
        action = input('What do you want to do? (swing, charge) ')
        # If the player chooses to swing
        if action == 'swing':
            # If the player has a sword, calculate the damage as a random number between 5 and 25
            if player['sword'] == 1:
                damage = random.randint(5, 25)
            # If the player doesn't have a sword, calculate the damage as a random number between 0 and 5
            else:
                damage = random.randint(0, 5)
            # Print a message to inform the player they swung at the enemy
            print('You swing at the ' + enemies[enemy]['name'])
            # Reduce the enemy's health by the calculated damage
            enemies[enemy]['health'] = enemies[enemy]['health'] - damage
            # Print a message to inform the player the enemy attacked them
            print('The ' + enemies[enemy]['name'] + ' attacks you with it\'s claws.')
            # Reduce the player's health by the enemy's damage
            player['health'] = player['health'] - enemies[enemy]['damage']
        # If the player chooses to charge
        elif action == 'charge':
            # If the player has a sword, calculate the damage as a random number between 0 and 15
            if player['sword'] == 1:
                damage = random.randint(0, 15)
            # If the player doesn't have a sword, calculate the damage as a random number between 0 and 5
            else:
                damage = random.randint(0, 5)
            # Print a message to inform the player they charged at the enemy
            print('You charge at the ' + enemies[enemy]['name'])
            # Reduce the enemy's health by a random number between 0 and 25
            enemies[enemy]['health'] = enemies[enemy]['health'] - damage
            # Print a message to inform the player the enemy attacked them
            print('The ' + enemies[enemy]['name'] + ' attacks you with it\'s claws.')
            # Reduce the player's health by the enemy's damage
            player['health'] = player['health'] - enemies[enemy]['damage']
        # If the player's input was not 'swing' or 'charge'
        else:
            # Print a message to inform the player their input was not understood
            print('I do not understand.')
    # If the enemy's health is 0 or less
    if enemies[enemy]['health'] <= 0:
        # Print a message to inform the player they defeated the enemy
        print('You have defeated the ' + enemies[enemy]['name'])
        # Restore the enemy's health to its original value
        enemies[enemy]['health'] = enemy_original_health
        # Pause the game until the player presses enter
        input('Press enter to continue.')
        # Mark the battle in the player's current room as finished
        rooms[player['location']]['battle'] = False
    # If the player's health is 0 or less
    elif player['health'] <= 0:
        # Print a message to inform the player they died and pause the game until they press enter
        input('You have died. Press enter to close.')
        # Exit the game
        exit()
    # Print the room information and possible actions for the player
    print_room()

# Dictionary to store the rooms in the game
rooms = {
    'room1': {
        'name': 'Entrance',
        'description': 'You find yourself in a dark room. \nThere is a door to the north.',
        'exits': {'north': 'room2'},
        'items': '',
        'battle': False,
    },
    'room2': {
        'name': 'Great Hall',
        'description': 'You enter into a large hall. \nIt is dimly lit by a few torches.\nThere are doors to the west, south and east.',
        'exits': {'west': 'room3', 'south': 'room1', 'east': 'room4'},
        'items': '',
        'battle': False,
    },
    'room3': {
        'name': 'Closet',
        'description': 'You are in a small storage closet. It smells of old cheese.\nThere is a door to the east.',
        'exits': {'east': 'room2'},
        'items': 'sword',
        'battle': False,
    },
    'room4': {
        'name': 'Open Room',
        'description': 'You enter into a well lit room. \nThere are doors to the west, north and east.',
        'exits': {'west': 'room2', 'north': 'room5', 'east': 'room6'},
        'items': '',
        'battle': True,
    },
    'room5': {
        'name': 'Statue Room',
        'description': 'You are in a room with a large statue. \nThere are doors to the north and south.',
        'exits': {'north': 'room7', 'south': 'room4'},
        'items': '',
        'battle': False,
    },
    'room6': {
        'name': 'Guards Quarters',
        'description': 'You are in a room with a few beds. \nThere is a door to the west.',
        'exits': {'west': 'room4'},
        'items': '',
        'battle': True,
    },
    'room7': {
        'name': 'Exit',
        'description': 'You find the exit and can leave if you survive.',
        'exits': {},
        'items': '',
        'battle': True,
    }
}

# Dictionary to store the player's information
player = {
    'health': 100,
    'location': 'room1',
    'key': 0,
    'sword': 0
}

# Dictionary to store the enemies in the game
enemies = {
    'enemy1': {'name': 'Goblin', 'health': 50, 'damage': random.randint(5, 10)},
    'enemy2': {'name': 'Orc', 'health': 100, 'damage': random.randint(10, 15)},
}

# Function to print the room information and possible actions for the player
def print_room():
    # Clear the screen
    clear_screen()
    # Print the name of the room the player is in
    print('You are in the ' + rooms[player['location']]['name'])
    # Print the description of the room the player is in
    print(rooms[player['location']]['description'])
    # Print the possible exits from the room the player is in
    print('There are exits to the: ')
    for exit in rooms[player['location']]['exits']:
        print(exit, end=', ')
    # If there are items in the room the player is in
    if rooms[player['location']]['items'] != '':
        # Print the items in the room
        print('\nThere is a ' + rooms[player['location']]['items'] + ' here.')
    # If there is a battle in the room the player is in
    if rooms[player['location']]['battle'] is True:
        # Start a battle with an enemy
        battle(player, enemies)
    # Ask the player what they want to do (move or take)
    action = input('\nWhat do you want to do? (move, take) ')
    # If the player wants to move
    if action == 'move':
        # Ask the player where they want to go
        direction = input('What direction do you want to go? ')
        # If the direction the player wants to go in is a possible exit from the room
        if direction in rooms[player['location']]['exits']:
           # Move the player to the room in the direction they chose
           player['location'] = rooms[player['location']]['exits'][direction]
        # If the direction the player wants to go in is not a possible exit from the room
        else:
            # Print a message to inform the player they can't go in that direction
            print('You cannot go that way.')
    # If the player wants to take an item
    elif action == 'take':
        # If there are items in the room the player is in
        if rooms[player['location']]['items'] != '':
            # Add the item in the room to the player's inventory
            player[rooms[player['location']]['items']] = player[rooms[player['location']]['items']] + 1
            # Print a message to inform the player they took the item
            print('You take the ' + rooms[player['location']]['items'])
            # Remove the item from the room
            rooms[player['location']]['items'] = ''
        # If there are no items in the room the player is in
        else:
            # Print a message to inform the player there is nothing to take
            print('There is nothing to take.')
    # If the player's input was not 'move' or 'take'
    else:
        # Print a message to inform the player their input was not understood
        print('I do not understand.')

    # If the player is in the exit room
    if rooms[player['location']] == 'room7':
        # Print a message to inform the player they escaped and exit the game
        print('You have escaped.')
        exit()

    # Pause the game until the player presses enter
    input('Press enter to continue.')
    # Print the room information and possible actions for the player
    print_room()

# Call the function to start the game
print_room()
