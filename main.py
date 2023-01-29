import random as rm
import time

# Clear run line before each value changes
# Create GUI - Maybe in JAVA
# Store data in a txt file located on Github for easy access
# after each trial show reaction time and percentile compared to previous players
# Want the letter to be a ghost/shadow letter

letter = chr(rm.randint(97, 122))
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(letter)

userLetter = input()


if userLetter == letter:
    print('Well Done!')
else:
    print('Really Dude! You SUCK!!!')
