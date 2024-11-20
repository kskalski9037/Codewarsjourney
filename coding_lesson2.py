# Strings are immutable meaning once they are created in a variable you 
# cannot change them
# creating strings with single and double quotes
single_quote = "Single quotes are great"
double_quote = "So are double quotes"
print(single_quote)
print(double_quote)

# Multiline strings using triple quotes
multi_line = """This is a 
string that 
spans multiple lines!"""
print("\nMulti-line String:") #\n means go to the next line after
print(multi_line)

# string indexing
word = "Coding Temple"
print("\nString Indexing:")
print(word[0])
print(word[-1])
print(word[-2])

# Concatenation (bring multiple strings together) of strings
greeting = "Why hello"
name = "George"
full_greeting = greeting + ", " + name + "!"
print("\nConcatenation:")
print(full_greeting)

# Repeat strings with * multiplies the strings 
laugh = "Ha" * 3 
print("\nString Repetition:")
print(laugh)

print("-" * 10)

# Finding the length of a string

phrase = "I'm not lazy, I'm on energy-saving mode."
length_of_phrase = len(phrase)
print("\nLength of Phrase:")
print(length_of_phrase)

# String slicing (substrings)
language = "Slice me up!"
print("\nString Slicing Examples:")
print(language[0:4]) #start at 0 and end at 4 without including 4
print(language[3:9])
print(language[-5:])

# Convert to uppercase and lowercase
message = "Hello Python!"
print("\nUppercase and Lowercase:")
print(message.upper())
print(message.lower())

# Remove whitespace from start and end of a string
# lstrip would get rip of whitespace on left side and rstrip on right side
whitespace_string = "    Trim this!    "
print("\nstrip() removes whitespace:")
print(whitespace_string.strip())

# Replace part of a string
text = "I love Java!"
print("\nReplace Example:")
print(text.replace("Java", "Python"))
print(text)

# Split and join
sentence = "Python rocks our world!" 
words = sentence.split()
print("\nSplit Example:")
print(words) #now can access words individually
print(words[0])

joined_sentence = " ".join(words)
print("\nJoin Example:")
print(joined_sentence)

# Check if a string starts or ends with a specific substring 
# (gives boolean values)
filename = "super_secret_file.txt"
print("\nStartswith and Endswith:")
print(filename.startswith("my"))
print(filename.startswith("super"))
print(filename.endswith(".txt"))

# String formatting with .format()
name = "Fred"
age = 99
print("\nString Formatting with .format():")
print("My name is {} and I am {} years old.".format(name, age))

# String formatting with f-strings
game_genre = "action-adventure"
game = "The Last of Us"
print("\nString Formatting with f-strings:")
print(f"My favorite game in the {game_genre} genre is \"{game}\".")

# More string methods: finding a substring and counting occurences
long_text = "Python is powerful. Python is versatile. Python is everywhere!"
print("\nFind and Count Examples:")
print(long_text.find("Python"))
print(long_text.count("Python"))

# Using slicing and immutability demonstration
original_text = "Jython"
fixed_text = "P" + original_text[1:]
print("\nFixing Strings by Slicing:")
print(f"Original text: {original_text}")
print(f"Fixed text: {fixed_text}")

# Title and capitalize
text = "hello world"
print("\nTitle and Capitalize:")
print(text.capitalize())
print(text.title())

# isdigit - check if a string consists only of digits
text = "12345"
print("\nIsdigit Example:")
print(text.isdigit())