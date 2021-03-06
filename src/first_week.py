
#  Basic data types

x = 3
print(type(x))                          # Prints "<class 'int'>"
print(x)                                # Prints "3"
print(x + 1)                            # Addition; prints "4"
print(x - 1)                            # Subtraction; prints "2"
print(x * 2)                            # Multiplication; prints "6"
print(x ** 2)                           # Exponentiation; prints "9"
x += 1
print(x)                                # Prints "4"
x *= 2
print(x)                                # Prints "8"
y = 2.5
print(type(y))                          # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2)          # Prints "2.5 3.5 5.0 6.25"

# Booleans

t = True
f = False
print(type(t))                          # Prints "<class 'bool'>"
print(t and f)                          # Logical AND; prints "False"
print(t or f)                           # Logical OR; prints "True"
print(not t)                            # Logical NOT; prints "False"
print(t != f)                           # Logical XOR; prints "True"

# Strings

hello = 'hello'                         # String literals can use single quotes
world = "world"                         # or double quotes; it does not matter.
print(hello)                            # Prints "hello"
print(len(hello))                       # String length; prints "5"
hw = hello + ' ' + world                # String concatenation
print(hw)                               # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)                             # prints "hello world 12"

s = "hello"
print(s.capitalize())                   # Capitalize a string; prints "Hello"
print(s.upper())                        # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))                       # Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))                      # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))          # Replace all instances of one substring with another;
# prints "he(ell)(ell)o"
print('  world '.strip())               # Strip leading and trailing whitespace; prints "world"

# Containers
# Lists

xs = [3, 1, 2]                          # Create a list
print(xs, xs[2])                        # Prints "[3, 1, 2] 2"
print(xs[-1])                           # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'                           # Lists can contain elements of different types
print(xs)                               # Prints "[3, 1, 'foo']"
xs.append('bar')                        # Add a new element to the end of the list
print(xs)                               # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()                            # Remove and return the last element of the list
print(x, xs)                            # Prints "bar [3, 1, 'foo']"

# Slicing

nums = list(range(5))                   # range is a built-in function that creates a list of integers
print(nums)                             # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])                        # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])                         # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])                         # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])                          # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])                        # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]                      # Assign a new sublist to a slice
print(nums)                             # Prints "[0, 1, 8, 9, 4]"

# Loops

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)                       # Prints "cat", "dog", "monkey", each on its own line.


animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))  # Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line


# List comprehensions

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)                          # Prints [0, 1, 4, 9, 16]

# example
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)                          # Prints [0, 1, 4, 9, 16]

# example2
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)                     # Prints "[0, 4, 16]"


# Prime Number Generator

def is_prime(n):
    for i in range(2, n):

        if n % i == 0:
            return False

        return True


n = input("Enter the number\n")

for x in range(2, int(n)):

    if is_prime(x):
        print(x, "is prime")
    else:
        print(x, "is not prime")
