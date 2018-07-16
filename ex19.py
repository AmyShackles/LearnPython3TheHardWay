# defines a function that prints strings related to the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# prints a string that tells the reader that you can give the function numbers directly to the screen
print("We can just give the function numbers directly:")
# invokes the function cheese_and_crackers, passing it the arguments 20 and 30
cheese_and_crackers(20, 30)

# prints a string informing the reader that you can use variables from the script to invoke the function to the screen
print("OR, we can use variables from our script:")
# assigns the value 10 to variable amount_of_cheese
amount_of_cheese = 10
# assigns the value of 50 to variable amount_of_crackers
amount_of_crackers = 50

# invokes cheese_and_crackers function, passing the variables amount_of_cheese and amount_of_crackers as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints the string "We can even do math inside too:" to the screen
print("We can even do math inside too:")
# invokes the function cheese_and_crackers with 10 + 20 as the first argument and 5 + 6 as the second argument
cheese_and_crackers(10 + 20, 5 + 6)

# prints "And we can combine the two, variables and math" to the screen
print("And we can combine the two, variables and math:")
# invokes the function cheese_and_crackers by passing the variable amount_of_cheese plus 100 as the first argument and amount_of_crackers plus 1000 as the second argument
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
