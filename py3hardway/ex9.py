
# variable containing a string of each day
# of the week separated by a space
days = "Mon Tue Wed Thu Fri Sat Sun"
# using a back-slash n will print the following text in a new line.
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)
# This is new, and my guess is that using three quotes is the 
# same as telling the print function to copy as typed including new lines.
# This also created the opportunity to use single and double quotes in the string.
print("""
Theres something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")