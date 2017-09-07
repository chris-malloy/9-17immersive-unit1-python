# tip calculaor for split checks

bill_amount = float(raw_input("How much was your bill? >"))
level_of_service = raw_input("How was the service? Good, fair or bad? >").lower()
tip = 0
if level_of_service == "good":
	tip = bill_amount * .2
elif level_of_service == "fair":
	tip = bill_amount * .15
elif level_of_service == "bad":
	tip = bill_amount * .1
else:
	print "Please enter good, fair, or bad."

total_bill = bill_amount + tip

print "The total bill including tip is %d." % total_bill

split_check = raw_input("Would you like to split the check? (Y or N)" >).lower()

if split_check == "y":
	number_of_split = float(raw_input("How many ways would you like to split the check?" >))
	amount_per_person = total_bill / number_of_split
	print "The amount per person is %d.  Thank you for coming." % amount_per_person
elif split_check == "n":
	print "Very well. Thank you for coming."
else:
	print "Please enter either Y or N."

