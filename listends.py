#!/usr/local/bin/python3

nums = []
stahp = 'Y'

def addNum(n):
	nums.append(n)

while stahp != 'n':
	num = input("Please enter a number: ")
	nums.append(num)
	stahp = input("Would you like to enter another number? (Y/n) ")

print("First number in the list is {0}. Last number in the list is {1}".format(nums[0],nums[-1])


	



