# While the functions given to us by Python's Standard Library are useful, it's not incredibly expansive.
# You can see from the built-in functions, there actually isn't much there.
#   - https://docs.python.org/3/library/functions.html

# --------------- BUILT-INS --------------- #

# The functions we've really only worked with so far is print, and the arithmetic operators. Some functions provide
#   utility by returning a value (or resulting in). For example the function type() returns the type of the object
#   provided as an argument.

type('cat')  # Nothing will appear to happen despite calling this function. Remember I am only getting the type of 10.

# If I want the value to be printed, then I must explicitly call the function print().
# Notice that the code almost follows english sentence structure.
print(type(10))  # English Sentence Comparison: PRINT the TYPE of 10.
print()

# You can also save the return value of a function to a function.
# For example, if I wanted to save the type of a string:
text_type = type('cat')
print('the type of text_type is:', text_type)
print()

# You can also use return values in operations or expressions.
# len() returns the length of a sequence. Since strings are a sequence of characters, you can get the length by using
#   the len() function.

length_of_text = len('this text is 31 characters long')
print('length of the text: ', length_of_text)

# Or in an expression:
print('length of the text + 10:', len('this text is 31 characters long') + 10)

# Or an expression saving to a variable.
length_of_text = len('this text is 31 characters long') * 4 - 10
print('length of the text * 4 - 10:', length_of_text)
print()

# NOTE: Functions are specific in the type that they return. Be sure to be aware of what the return value will be by
#   checking the documentation.


# --------------- DEFINING FUNCTIONS --------------- #


# Defining our own functions allows us to create custom functionality for our programs and is incredibly useful
#   at condensing simple and complex sets of operations into a single line.

# See below, an example of a simple function that prints songs on repeat. Above it is the standard setup for comments
#   for functions. Take note of the structure.

# function - print_albums
#   parameters
#       - none
#   return values
#       - none
# description: prints the top three songs on repeat according to spotify
def print_songs():
    print('Top Three Songs on Repeat')
    print('1: Law of Averages by Vince Staples')
    print('2: LEMONHEAD by Tyler, The Creator')
    print('3: A+ by Kenny Mason')                   # last indented line, last line in the function.


# This function is now defined and exists in memory, meaning I can use it any time within the file.
# Defining a function DOES NOT call the function. Only calling a function, calls a function. Naturally (¬‿¬ ).

# If I call the album three times, then it will be executed three times.
print_songs()
print_songs()
print_songs()
print()

# As you know when we call functions, like print() or len(), we sometimes supply arguments. So where do those go?
# The answer: parameters.


# Parameters are special variables that are defined in the function definition, between the parentheses.
def print_number(a):
    print(a)


# When you call a function that has a parameter(s), you must supply the same number of arguments as parameters.
print_number(5)
print_number(10.245)

# Otherwise you will cause an error.


# Here is an example with 3 parameters:
def print_numbers(a, b, c):
    print(a, b, c)


print_numbers(-41, 2324, 21.23)  # 3 parameters --> 3 arguments
print()


# You can also do operations in functions!
def print_squared(num):
    print(f'{num} squared is: {num ** 2}')


print_squared(11)
