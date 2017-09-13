# reverse a string

user_text = raw_input("What string would you like to reverse?\n>")

text_as_list = list(user_text)
print text_as_list 

text_as_list.reverse()

reverse_string = "".join(text_as_list)
print reverse_string