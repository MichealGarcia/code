# This string is using the backslash t (\t) to create a tab in
# the string when printing.
tabby_cat = "\tI'm tabbed in."
# the "\n" is creating a new line, splitting the text where inserted.
persian_cat = "I'm split\non a line"
# The backslash is saying to "escape" with the backslash?
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

test = "\vinteresting\visn't it?"

print(test)

# I don't understand some of the escapes uses, and need to find more use cases or code examples

print(f"\\Hi there\vLets learn some code.\n {test}")