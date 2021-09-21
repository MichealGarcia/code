# Import argv from the sys module
from sys import argv
# unpack te argument variable for running the script, 
# Create parameters to run script
script, filename = argv
# Create a variable that will open the txt file.
txt = open(filename)
# print the name of the file we call, then print the text inside the opened
# txt file using the read method
print(f"Here's your file {filename}:")
print(txt.read())
# Use the input method to get the name of the file and open then read it
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt = txt.close()
txt_again = txt_again.close()
