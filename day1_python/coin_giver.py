# add coins to user when they ask for a coin

number_of_coins = 0

print "Welcome to my coin machine."

add_coin = raw_input("Would you like a coin? (Y or N) >").lower()

while add_coin == "y":
	number_of_coins += 1
	if number_of_coins == 1:
		print "Thank you. You have 1 coin."
	else:
		print "Thank you. You have %d coins." % number_of_coins
	add_coin = raw_input("Would you like another? (Y or N) >").lower()
else:
	if number_of_coins == 0:
		print "What you don't like my coins? :("
	elif number_of_coins >= 10:
		print "You nearly took all my coins!"
	elif number_of_coins >= 5:
		print "Enjoy your coins!"
	elif number_of_coins < 3:
		print "I have more you know..."



