#!/usr/local/bin/python3

num = input("Please enter anumber: ")
a = range(2, int(num))

for i in a:
	if int(num) % i == 0:
		print(i)

