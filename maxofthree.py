#!/usr/local/bin/python3

def maxOfThree(n1,n2,n3):
	if n1 > n2 and n1 > n3:
		return n1
	elif n2 > n3 and n2 > n1:
		return n2
	elif n3 > n2 and n3 > n1:
		return n3

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the second number: ")

print(maxOfThree(num1,num2,num3))
