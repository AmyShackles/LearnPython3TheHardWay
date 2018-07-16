from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}. Hit RETURN to continue, CTRL-C to abort.")

# we could do these two on one line - how?
in_file = open(from_file); indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

print(f"{from_file} successfully copied to {to_file}.")

out_file.close()
in_file.close()
