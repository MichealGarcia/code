# Created a variable with curly brackets
# that will be used to format four items when called in
# the format function.
formatter = "{} {} {} {}"

# each of these print functions are calling 4 variables to format into our string
# This is an outdated version of an f-string.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try Your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# Good example, since there is only one curly bracket, the format function will only grab one
# object
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))



