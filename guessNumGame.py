print "I am thinking of a number between 1 and 10."

import random 
secret_number = random.randint(1,10)
print secret_number

keep_going = True
while keep_going == True:
	initial_guesses = 5
	while keep_going: 
		guess = int(raw_input("What's the number? >"))
		if (guess == secret_number):
			print "Yes! You got it!"
			keep_going = False	
		elif (initial_guesses == 0):
			print "You ran out of guesses! The number was %d" % secret_number
			keep_going = False
		elif (guess < secret_number):
			print str(guess) + " is too low."
			initial_guesses -= 1
			print "You have " + str(initial_guesses) + " guesses left."
		elif (guess > secret_number):
			print str(guess) + " is too high."
			initial_guesses -= 1
			print "You have " + str(initial_guesses) + " guesses left."

		







