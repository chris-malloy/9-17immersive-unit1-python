# calculate the tip

bill_amount = float(raw_input("How much was your bill? >"))
level_of_service = raw_input("How was the service? Good, fair or bad? >").lower()
tip = 0
if level_of_service == "good":
	tip = bill_amount * .2
elif level_of_service == "fair":
	tip = bill_amount * .15
else: 
	tip = bill_amount * .1
total_bill = bill_amount + tip
print "Your bill including tip is $%d. Thank you for coming." % total_bill
