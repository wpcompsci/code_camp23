import random
import time

print("WELCOME TO THE MAGIC 8 BALL")
print("I can predict the future!")

input("\nAsk me a YES or NO question. ")

answer = random.randint(1,6)

time.sleep(2)
print("I am thinking of the response", end=".")
time.sleep(1)
print("", end=".")
time.sleep(1)
print("", end=".")
time.sleep(1)
print(".")
time.sleep(1)

if answer == 1:
    print("It is likely.")
elif answer == 2:
    print("Definitely.")
elif answer == 3:
    print("Doesn't look like it.")
elif answer == 4:
    print("NOPE!")
elif answer == 5:
    print("Answer is cloudy.")
elif answer == 6:
    print("Maybe.")

