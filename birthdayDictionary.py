#!/usr/local/bin/python3

d = {
	'Hanna' : 'October 3rd',
	'Lina' : 'September 18th',
	'Nick' : 'Marach 26th',
	'Charlie' : 'October 18th',
	'Sami' : 'October 18th'
}

print("Welcome to the birthday dictionary! We know the birthdays of Hanna, Lina, and Nick, Charlie, Sami")
select = input("Who's birthday would you like to know? ")

print(d[select])
