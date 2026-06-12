
# Read the entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# Writing to a file
with open("data.txt", "w") as file:
    file.write("This will replace everything in the file.\n")


# Appending text to the end of a file
with open("example.txt", "a") as file:
    file.write("This line is safely added to the end.\n")