# print a box of user specified size

width = int(raw_input("How wide is the box? "))
height = int(raw_input("How tall is the box? "))

for i in range(0, height):
	if (i == 0):
		print "*" * width
	elif (i == height - 1):
		print "*" * width
	else:
		print "*" + (" " * (width - 2)) + "*"

