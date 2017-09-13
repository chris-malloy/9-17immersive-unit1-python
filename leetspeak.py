# turn a given string into leetspeak

user_text = raw_input("What text would you like to turn into leetspeak?\n>").upper()

length_of_user_text = len(user_text)

user_text_as_list = list(user_text)

for i in range(0, length_of_user_text):
	if(user_text_as_list[i] == "A"):
		user_text_as_list[i] = "4"
	elif(user_text_as_list[i] == "E"):
		user_text_as_list[i] = "3"
	elif(user_text_as_list[i] == "G"):
		user_text_as_list[i] = "6"
	elif(user_text_as_list[i] == "I"):
		user_text_as_list[i] = "1"
	elif(user_text_as_list[i] == "O"):
		user_text_as_list[i] = "0"
	elif(user_text_as_list[i] == "S"):
		user_text_as_list[i] = "5"
	elif(user_text_as_list[i] == "T"):
		user_text_as_list[i] = "7"

leet_text = "".join(user_text_as_list)
print leet_text

