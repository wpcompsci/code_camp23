# POKEMON BATTLE
import random

#INITALIZE STARTING VARIABLES
pikachu_hp = 50
charizard_hp = 50

# LOOP UNTIL ONE FAINTS
while pikachu_hp > 0 and charizard_hp > 0:
    # DISPLAY THEIR HEALTH
    print(f"\nPikachu has {pikachu_hp}hp.")
    print(f"Charizard has {charizard_hp}hp.")

    # PLAYER ATTACK
    print("\nIt is Pikachu's attack.\n"
          "Select a letter:\n"
          "a) Thunderbolt\n"
          "b) Iron Tail\n"
          "c) Quick Attack")
    player_attack = input(">>> ")

    #PLAYER DOES DAMAGE
    if player_attack == "a":
        damage = random.randint(0, 15)
        print(f"Pikachu uses Thunderbolt for {damage} damage.")
    elif player_attack == "b":
        damage = random.randint(3, 10)
        print(f"Pikachu uses Iron Tail for {damage} damage.")
    elif player_attack == "c":
        damage = random.randint(6, 7)
        print(f"Pikachu uses Quick Attack for {damage} damage.")
    else:
        print("Pikachu misses!")
        damage = 0

    charizard_hp = charizard_hp - damage
    if charizard_hp <= 0:
        break
    
    # COMPUTER ATTACK
    computer_attack = random.choice(['a', 'b', 'c'])
    if computer_attack == "a":
        damage = random.randint(0, 15)
        print(f"Charizard uses Dragon Breath for {damage} damage.")
    elif computer_attack == "b":
        damage = random.randint(3, 10)
        print(f"Charizard uses Fire Ball for {damage} damage.")
    elif computer_attack == "c":
        damage = random.randint(6, 7)
        print(f"Charizard uses Tackle for {damage} damage.")

    pikachu_hp = pikachu_hp - damage
    if pikachu_hp <= 0:
        break

if pikachu_hp <= 0:
    print("Pikachu fainted. Charizard wins!")
else:
    print("Charizard fainted. Pikachu wins!")

