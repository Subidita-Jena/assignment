from typing import Text


story = "one upon a time i was a student of CET"
print(len(story)) #len string

#endswith
print(story.endswith("mine"))

print(story.endswith("CET"))

#string.count
print(story.count("o"))

print(story.count("upon"))

#string.capitalize

print(story.capitalize())

#string.find

print(story.find("time"))

print(story.find("once"))

#string.replace

print(story.replace("upon","subi"))

#string.casefold
print(story.casefold())

#string.centre
print(story.center(100))

#string.encode
print(story.encode())

#string.expandtabs
Text = "s\tr\tu\tt\ti"
print(Text.expandtabs(2))

#string.index
print(story.index("was"))

#string.isalnum
print(story.isalnum())

#string.isalpha()
print(story.isalpha())

#string.isascii()
print(story.isascii())

#string.isdecimal()
print(story.isdecimal())

#string.isdigit()
print(story.isdigit())

#string.isidentifier()
print(story.isidentifier())

#string.islower()
print(story.islower())

#string.isnumeric()
print(story.isnumeric())

#string.isprintable()
print(story.isprintable())

#string.isspace()
print(story.isspace())

#string.istitle()
print(story.istitle())

#string.isupper()
print(story.isupper())

#string.join()
x = "#".join(story)
print(x)

#string.lower()
print(story.lower())

#string.lstrip()
print(story.lstrip())

#string.maketrans()
print(story.maketrans("s","p"))

#string.partition()
print(story.partition("was"))

#string.rfind()
print(story.rfind("was"))

#string.rindex()
print(story.rindex("was"))

#string.rjust()
y = story.rjust(50)
print(y)

#string.rpartition()
print(story.rpartition("CET"))

#string.rstrip()
print(story.rstrip())

#string.spiltlines()
print(story.splitlines())

#string.swapcase()
print(story.swapcase())

#string.title()
print(story.title())

#string.translate()
print(story.translate(story))

#string.upper()
print(story.upper())

#string.zfill()
print(story.zfill(10))