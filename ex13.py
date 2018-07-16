from sys import argv
# read the WYSS section for how to run this
# this takes the arguments in argv and assigns them to variables in order
print(type(argv))
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

favorite_color = input("What is your favorite color? ")
print(f"So your favorite color is {favorite_color}.  That's nice.")
