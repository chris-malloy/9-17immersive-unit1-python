
# # A function (in Python "definition"), is a piece of cod that can be 
# # called from somewhere else. They are meant to be re-usable and to make
# # things clean.
# # If you have complicated code, you can break it into pieces that are easier to understand.
# # Repeating yourself is BAD.
# # - Copy and paste erros
# # - odd behavior
# # - etc...
# # to declare a function in python, you use "def"
# # function ALWAYS have a ()_

# # This defines the function.
# def say_hello():
# 	print "Hello"

# # This calls the funciton (tells Python to run the code to run)
# say_hello()

# # Passing cvariable in to function are called arguments on the in 
# # paramteters once inside

# def say_hello_with_name(name):
# 	print "Hello, %s" % name

# say_hello_with_name("Chris")

# You can set a default for a parameter
def say_hello_safe(name, in_class="yes"):
	print "%s, %s is in the class" % (in_class, name)

say_hello_safe("Chris")
