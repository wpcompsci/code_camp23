import random

class Pokemon:
    def __init__(self, name, attacks, hp):
        self.name = name
        self.attacks = attacks
        self.hp = hp

    def attack(self, attack_key):
        if attack_key in self.attacks:
            damage = random.randint(*self.attacks[attack_key]['damage'])
            print(f"{self.name} uses {self.attacks[attack_key]['name']} for {damage} damage.")
        else:
            print(f"{self.name} misses!")
            damage = 0
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        return self.hp <= 0  # Return True if Pokemon has fainted, else False


# Define the attacks for Pikachu and Charizard
pikachu_attacks = {
    'a': {'name': 'Thunderbolt', 'damage': (0, 15)},
    'b': {'name': 'Iron Tail', 'damage': (3, 10)},
    'c': {'name': 'Quick Attack', 'damage': (6, 7)}
}

charizard_attacks = {
    'a': {'name': 'Dragon Breath', 'damage': (0, 15)},
    'b': {'name': 'Fire Ball', 'damage': (3, 10)},
    'c': {'name': 'Tackle', 'damage': (6, 7)}
}

# Initialize Pokemon
pikachu = Pokemon('Pikachu', pikachu_attacks, 50)
charizard = Pokemon('Charizard', charizard_attacks, 50)

# Main battle loop
while True:
    # Display their health
    print(f"\n{pikachu.name} has {pikachu.hp}hp.")
    print(f"{charizard.name} has {charizard.hp}hp.")

    # Player attack
    print("\nIt is Pikachu's attack.\n"
          "Select a letter:\n"
          "a) Thunderbolt\n"
          "b) Iron Tail\n"
          "c) Quick Attack")
    player_attack = input(">>> ")

    damage = pikachu.attack(player_attack)
    if charizard.take_damage(damage):
        print(f"{charizard.name} fainted. {pikachu.name} wins!")
        break

    # Computer attack
    computer_attack = random.choice(list(charizard.attacks.keys()))
    damage = charizard.attack(computer_attack)
    if pikachu.take_damage(damage):
        print(f"{pikachu.name} fainted. {charizard.name} wins!")
        break
