print("Welcome to the Mad Libs game!")
print("Please enter the following words to create your story:")

name = input("Enter a name: ")
place = input("Enter a place: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

print(f"\nOnce upon a time, there was a person named {name} who lived in {place}."
      f" One day, {name} found a magical {noun} and decided to {verb} with it."
      f" The {noun} was incredibly {adjective} and could {verb} {adverb}."
      f" {name} was amazed by its powers and decided to keep it as a precious treasure."
      f" From that day on, {name} and the {noun} became inseparable, embarking on {adjective} adventures together.")