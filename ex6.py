# Assign a value of 10 to types_of_people
types_of_people = 10
# Assign the string 'There are {the variable types_of_people} types of people' to variable x
x = f"There are {types_of_people} types of people."

#assign the string 'binary' to variable binary
binary = "binary"
# assign the string 'don't' to the variable do_not
do_not = "don't"
# assign the string 'Those who know {the variable binary} and those who {the variable do_not}'
y = f"Those who know {binary} and those who {do_not}."

# print the variable x to the screen
print(x)
# print the variable y to the screen
print(y)

#print the string 'I said {variable x}'
print(f"I said: {x}")
# print the string 'I also said: '{variable y}''
print(f"I also said: '{y}'")

# assign the value of boolean False to variable hilarious
hilarious = False

# set string 'Isn't that funny?! {replacement field which implicitly references the first positional argument} to variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# print formatted string for joke_evaluation where replacement field is replaced by variable hilarious
print(joke_evaluation.format(hilarious))

# assign string 'This is the left side of ...' to variable w
w = "This is the left side of..."
# assign string 'a string with a right side.' to variable e
e = "a string with a right side."

# print variable w plus variable e
print(w + e)
