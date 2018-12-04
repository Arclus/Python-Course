empty = []
letters = ['a', 'b', 'c', 'd']
numbers = [2, 3, 5]

print("Boş Liste {} --- Harfler Listesi {} --- Sayılar Listesi {}".format(empty, letters, numbers))


mixed = [4, 5, "seconds"]

print(mixed)

numbers.append(7)                                                       # numbers == [2, 3, 5, 7]
numbers.append(11)                                                      # numbers == [2, 3, 5, 7, 11]

print(numbers[0])                                                       # => 2
print(numbers[-1])                                                      # => 11

print(letters[:3])                                                      # => ['a', 'b', 'c']
print(numbers[1:-1])                                                    # => [3, 5, 7]


x = [letters, numbers]
print(x)                                                                # => [['a', 'b', 'c', 'd'], [2, 3, 5, 7, 11]]
print(x[0])                                                             # => ['a', 'b', 'c', 'd']
print(x[0][1])                                                          # => 'b'
print(x[1][2:])                                                         # => [5, 7, 11]


list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

print("1. Liste --> {} --- 2. Liste --> {}".format(list_1, list_2))

list_1.extend(list_2)

print("1. Liste --> {}".format(list_1))

list_1.insert(5, "yeni eleman")

print("1. Liste --> {}".format(list_1))

list_1.remove(5)

print("1. Liste --> {}".format(list_1))

list_1.clear()

print("1. Liste --> {}".format(list_1))

list_3 = ['a', 'b', 'c', 'd', 'e', 'd', 'd']

print("3. Liste --> {}".format(list_3))

print(list_3.count('d'))

print(list_3.index('b'))

print(list_3.pop(5))

list_3.sort(key=None, reverse=False)

print("3. Liste --> {}".format(list_3))

list_3.reverse()

print("3. Liste --> {}".format(list_3))


empty = {}

print(type(empty))                                                          # => dict

print(empty == dict())                                                      # => True

a = dict(one=1, two=2, three=3)

b = {"one": 1, "two": 2, "three": 3}

print(a == b)                                                               # => True

b = {"one": 1, "two": 2, "three": 3}

print(b['one'])                                                             # => 1

b['two'] = 22                                                               # Modify an existing key

b['four'] = 4                                                               # Add a new key

print(b.values())

print(b.keys())

print(b.items())

del b["one"]

print(b.items())

print(len(b.keys()))

print(('one', 1) in b.items())

for value in b.values():
    print(value)

keys_list = list(b.keys())

print(keys_list)

print(b.copy())

for key in b:
    print(key)

b.clear()


fish = (1, 2, "red", "blue")

print(fish)

print(fish[0])                                                              # => 1

print(len(fish))                                                            # => 4

print(fish[:2])                                                             # => (1, 2)

print("red" in fish)                                                        # => True


t = 12345, 54321, 'hello!'

print(t)                                                                    # (12345, 54321, 'hello!')

print(type(t))                                                              # => tuple

x, y, z = t

print("x {} y {} z {}".format(x, y, z))                                     # x => 12345  y => 54321  z => 'hello!'


for index, color in enumerate(['red','green','blue']):
    print(index, color)


empty_set = set()

set_from_list = set([1, 2, 1, 4, 3]) # => {1, 3, 4, 2}

for item in set_from_list:
    print(item, end='-')

basket = {"apple", "orange", "apple", "pear", "banana"}

print(len(basket))                                                          # => 4
print("orange" in basket)                                                   # => True
print("crabgrass" in basket)                                                # => False

for fruit in basket:
    print(fruit, end='/')


a = set("mississippi")                                                      # {'i', 'm', 'p', 's'}
a.add('r')

print("\n {}".format(a))

a.remove('m')

print("\n {}".format(a))

a.discard('x')

print("\n {}".format(a))

a.pop()

print("\n {}".format(a))

print(len(a))

a.clear()



EFFICIENT_LETTERS = "BCDGIJLMNOPSUVWZ"


def is_efficient(word):
    for letter in word:
        if letter not in EFFICIENT_LETTERS:
            return False
    return True

print(is_efficient("BCDGIJLMNOPSUVWZ"))



EFFICIENT_LETTERS = set("BCDGIJLMNOPSUVWZ")


def is_efficient(word):
    return set(word) <= EFFICIENT_LETTERS

print(is_efficient("BCDGIJLMNOPSUVWZ"))
