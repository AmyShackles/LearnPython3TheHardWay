# Assign a string to formatter that contains four placeholders
formatter = "{} {} {} {}"

# call the format function on the varialbe formatter, passing it the arguments 1, 2, 3, 4 and print it
print(formatter.format(1, 2, 3, 4))
# call the format function on the variable formatter, passing it the arguments "one", "two", "three", and "four" and print it
print(formatter.format("one", "two", "three", "four"))
# call the format function on the variable formatter, passing it the arguments True, False, False, True, and print it
print(formatter.format(True, False, False, True))
# call the format function on the variable formatter, passing it the value of formatter four times
print(formatter.format(formatter, formatter, formatter, formatter))
# call the format function on the variable formatter passing it the arguments "Try your", "Own text here", "Maybe a poem", "Or a song about fear" and print it
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
