# Assigning values to variables
# cars equals 100
cars = 100
# space_in_a_car equals 4.0 (floating point number)
space_in_a_car = 4.0
# drivers equals 30
drivers = 30
# passengers eauals 90
passengers = 90
# cars_not_driven eauals number of cars minus number of drivers
cars_not_driven = cars - drivers
# cars_driven equals number of drivers
cars_driven = drivers
# carpool_capacity eauals number of cars driven multiplied by space in a car
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car equals number of passengers divided by number of cars driven
average_passengers_per_car = passengers / cars_driven

# Using variables in print statements
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
