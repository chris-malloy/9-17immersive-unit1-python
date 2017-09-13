user_input = raw_input("Please enter text to be converted to ceasar cipher \n>")

user_input_list = list(user_input)

cipher_num = int(raw_input("Please enter number to shift text.\n>"))

alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



for i in range(0, len(user_input)):
	if (user_input_list[i] == " "):
		continue
	a = alpha_list.index(user_input_list[i])
	b = a + cipher_num
	if (b >= 26):
		b -= 26
	user_input_list[i] = alpha_list[b]

cipher_text = "".join(user_input_list)
print cipher_text 
alpha.index("a")




newstring2 = ["c", "a", "t"]

