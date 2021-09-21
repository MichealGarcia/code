def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# The *args is actually pointless

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This next one will take only one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

# This one will take no arguments, so it will run with no parameters after being called

def print_none():
    print("I got nothin'.")

print_two("Micheal", "Garcia")
print_two_again("Micheal", "Garcia")
print_one("First!")
print_none()