# count with for, using user input

start_point = int(raw_input("Where would you like to start?\n>"))
end_point = int(raw_input("Where would you like to end\n>"))

for i in range(start_point, end_point + 1):
	print i
