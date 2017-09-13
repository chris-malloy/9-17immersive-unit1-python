# print a triangle of user specified size.
height = raw_input("How tall do you want the triangle? ")

for i in range(0, height):
	print (" " * (height - 1)) + "*" + (" " * (height - 1))
	print (" " * (height - 2)) + "*" * 3 + (" " * (height -2))
	print " " + "*" * 5 + " " 
	print "*" * 7
