# turn any group of 2 vowels to 5 vowels

user_input = raw_input("What string would you like to give long vowels to? \n>").lower()

user_input_list = list(user_input)

for i in range(0, len(user_input) - 1):
	print i
	if(user_input_list[i] == "a" and user_input_list[i + 1] == "a"):
		user_input_list[i] = "aaaa"
	elif(user_input_list[i] == "e" and user_input_list[i + 1] == "e"):
		user_input_list[i] = "eeee"
	elif(user_input_list[i] == "i" and user_input_list[i + 1] == "i"):	
		user_input_list[i] = "iiii"
	elif(user_input_list[i] == "o" and user_input_list[i + 1] == "o"):	
		user_input_list[i] = "oooo"
	elif(user_input_list[i] == "u" and user_input_list[i + 1] == "u"):	
		user_input_list[i] = "uuuu"

input_with_long_vowels = "".join(user_input_list)
print input_with_long_vowels
