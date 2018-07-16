from sys import argv

# assigns arg[0] to the variable script and argv[1] to the variable filename
script, filename = argv

# assigns the function for opening the file to the variable txt
txt = open(filename)

# prints the string 'Here is your {value of variable filename}'
print(f"Here's your file {filename}:")
# prints the output of invoking read on open(filename)
print(txt.read())

# prints the string 'Type the filename again:'
print("Type the filename again:")
# asks the user for input (the filename)
file_again = input("> ")
# takes the user input and calls the function open on it and assigns it to the variable txt_again
txt_again = open(file_again)
# prints the output of invoking read on open(file_again)
print(txt_again.read())
