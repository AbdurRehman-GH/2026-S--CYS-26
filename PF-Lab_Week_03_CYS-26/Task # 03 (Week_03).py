user_string = input("Enter a string: ")
make_upper = lambda x: x.upper()
upper_string = make_upper(user_string)
print("Uppercase string is: ", upper_string)

def invert(text):
    reverse_text = ""

    for i in text:
        reverse_text = i + reverse_text
    print("Reversed string is: ", reverse_text)

invert(upper_string)