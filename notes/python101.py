# # print "Hello World"
# # print("Hello, World")
# # # this is a comment

# # print """
# # Triple quotes will make
# # python happy.
# # Even thoguth this is ugly.
# # """


# # # variables - strings, letters, numnbers, or any numbers you can make with a keyboard.
# # # a vsriable is just a fast way to refer to something else.  It does not make the computer faster, it makes it slower.  
# # # a variable is for you.
# # # Python is NOT heavily type. (doesn't care what data type a variable is)

# # name = "Chris Malloy"; #this is a string.

# # # Date types
# # # - strings - English stuff, for people to read.

# # # Numbers - something digits and th estuff that goes with them (- or . or e)
# # # Floats, integers
# # # -- float has a . in it
# # # -- integer - has no .
# # # Booleans - True of false, 1 or 0, off or on. These are good as flags. Asking questions, yes or no
# # # list - list of things. A single variable with a bunch of like parts
# # # dictionary - variable of variable
# # # objects - we will deal with this later

# # name = "Chris " + "Malloy"
# # first = "Chris"
# # last = "Malloy"
# # full_name = first + last;
# # print full_name
# # meaning_of_life = 40 + 2; # + is now a summation symbol


# # print "-" * 20

# # #How to pass agruments to a string
# # first_name = "Chris"
# # last_name = "Malloy"
# # #Intermingle english and vars: way 1
# # print "Hello {} {}".format(first_name, last_name)
# # #Way 2
# # print "Hello %s" % first_name

# # #How to find out your data type
# # pi = 3.14
# # print type(pi)
# # makeMeAnInt = int(pi)
# # print makeMeAnInt


# # # Booleans
# # the_truth = True
# # print type(the_truth)

# # # to add a number to variable quick way
# # addOneToMe = 1
# # addOneToMe += 1
# # print addOneToMe

# # #Order of operations is what you learn in the 3rd grade.


# print "What is your name?"
# name = raw_input(">")
# print "Your name is %s" % name

# print "What is your age?"
# age = raw_input(">")
# print "Your age is %s" % age

# # CONDITIONALS 
# # == - compare left and right 
# # === - compare left and right and data types 

# if (16 == "16"):
# 	print True

# import this

# if(1 == 2):
# 	print "True!"
# elif(2 == 2):
# 	print "Second one is true!"
# else:
# 	print "False"

# classSize = 19
# question = "How big is your class?"
# print question
# response = raw_input("> ")
# response_as_an_int = int(response)
# if (response_as_an_int != classSize):
# 	print "You must not be in the September class."
# else:
# 	print "Let's learn to code!"

import random
rand_number = random.randint(1,10)
print rand_number

keep_going = True
while keep_going: 
	get_answer = raw_input("Please hit any key")
	keep_going = False
print "You are no longer in the loop!"

































