from sys import argv

script, input_file = argv

# print_all prints the contents of the file
def print_all(f):
    print(f.read())

# seek looks for a specific point in the file
def rewind(f):
    f.seek(0)

# print_a_line prints one line of a document in order (line_count is just a value tacked onto the side of it in output)
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
