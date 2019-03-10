#!/usr/local/bin/python3

# Import the universe
import random
import os

# Open the file we will need to read
f = open("sowpods.txt")
lines = f.readlines()
count = len(lines) - 1
print("There are " + str(count) + " words in the list.")

# Pick a random word from the list
r = random.randint(1,count)
print(lines[r])
print(str(lines[r]) + " is the " + str(r) +"'th word in the list.")
