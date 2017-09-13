
# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.
# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.
# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.
# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.
# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)


# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
#datetime is uncluded in Python... we just need to imprt it!
# import datetime
# now = datetime.date.now()
# currentYear = now.year
def myAge(yearBorn):
	print (2017 - yearBorn)
myAge(1992)
# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# HINT: Consider using a 'for loop'.

# method 1
def sum_odd_numbers():
	# init a var "sum" at 0 so we can increment it
	sum = 0
	#run a loop from 1-5000 (don't inlcude 5001)
	for i in range(1, 5001):
		if (i % 2 == 1):
			# odd number!
			sum += i 
	print sum 
sum_odd_numbers()

# method 2
def sum_odd_numbers2():
	sum = 0
	# range has 3rd arg. Step is the third, so you can run the 
	# loop by 2s (instead of 1s)
	for i in range(1, 5001,2):
		sum  += i
	print sum
sum_odd_numbers2()


































