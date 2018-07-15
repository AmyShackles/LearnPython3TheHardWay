name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 #inches
height_in_cm = height_in_inches * 2.54
weight_in_pounds = 180 # pounds
weight_in_kg = weight_in_pounds * .453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_inches} inches tall, which is {height_in_cm} centimeters.")
print(f"He's {weight_in_pounds} pounds heavy, which is {weight_in_kg} kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_in_inches + weight_in_pounds
print(f"If I add {age}, {height_in_inches}, and {weight_in_pounds} I get {total}.")
