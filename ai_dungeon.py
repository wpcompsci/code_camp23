locations = {
    "The Bunny Fields": {
        "description": "You are in a lush field, full of hopping bunnies.",
        "exits": {"n": "The Rainbow Falls", "e": "Fairy Farm"}
    },
    "The Rainbow Falls": {
        "description": "You're standing in front of a majestic waterfall, casting a beautiful rainbow.",
        "exits": {"s": "The Bunny Fields", "e": "The Magic Forest"}
    },
    "The Magic Forest": {
        "description": "You're in a magical forest. The trees sparkle with enchantment.",
        "exits": {"w": "The Rainbow Falls", "s": "Fairy Farm", "e": "Mystic Caves"}
    },
    "Pixie Ring": {
        "description": "You're in a mystical ring where pixies dance.",
        "exits": {"n": "Fairy Farm", "e": "The Bunny Fields"}
    },
    "Fairy Farm": {
        "description": "You're in a small farm, where fairies tend to their magical plants.",
        "exits": {"n": "The Magic Forest", "w": "The Bunny Fields", "s": "Pixie Ring"}
    },
    "Mystic Caves": {
        "description": "You're in an ancient mystic cave, glowing with an ethereal light.",
        "exits": {"w": "The Magic Forest"}
    },
}

current_location = "The Bunny Fields"

while True:
    print("\n" + locations[current_location]["description"])
    print("You can go to the following locations: ")
    for direction, place in locations[current_location]["exits"].items():
        print(f"{direction}: {place}")
    move = input("\nWhere would you like to go? ")
    if move in locations[current_location]["exits"]:
        current_location = locations[current_location]["exits"][move]
    else:
        print("\nInvalid direction! Please try again.")
