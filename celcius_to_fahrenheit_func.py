# funciton to convert Celcius to Fahrenheit
cel_temp = float(raw_input("What is the temperature? (in celcius) >"))
def celcius_to_fahrenheit(cel_temp):
	print "Let's convert that to fahrenheit."
	fah_temp = (cel_temp * 1.8 + 32)
	return fah_temp
	print "In fahrenheit, that temperature would be " + str(fah_temp)
celcius_to_fahrenheit(cel_temp)