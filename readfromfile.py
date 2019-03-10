#!/usr/local/bin/python3

import os 

# Make a dictionary to store information
wordcount = {}

# Open the file to read information
file = open("nameslist.txt", "r")
for word in file.read().split():
	if word not in wordcount:
		wordcount[word] = 1 # Create word entry if it's not already int eh dictionary
	else:
		wordcount[word] += 1 # increase the count if the word is already in the dictionary

# Print every instance and its counts
for k,v in wordcount.items():
	print(k,v)
file.close()



