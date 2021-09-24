# Importing variable arguments from sys
from sys import argv
# unpacking into 2 arguments
script, input_file = argv
# This function will take a file as input and print its content
def print_all(f):
    print(f.read())
# This function will rewind us back to first byte in the file.
def rewind(f):
    f.seek(0)
# This function prints out the specified line in the txt file.
def print_a_line(line_count, f):
    print(line_count, f.readline())
# This is opening the file we want to pull data from.
current_file = open(input_file)

print("First let's print the whole file:\n")
# Call the print_all function we made and use the current file as a parameter
print_all(current_file)

print("Now let's rewind, kind of like a tape.\n")
# This resets where we are reading the file from, byte 0 (the beginning of the document.)
rewind(current_file)


print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



