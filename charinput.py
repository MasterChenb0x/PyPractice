#!/usr/local/bin/python3

year = 2019

name = input("Please enter your name: ")

age = input("Please enter your age: ")

diff  = 100 - int(age)

ans = year + diff

print("Hello {0}. You will turn 100 in the year {1}".format(name, ans))
