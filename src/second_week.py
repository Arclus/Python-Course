range(3)                                                    # 0, 1, 2 çıktısını üretir.
range(5, 10)                                                # 5, 6, 7, 8, 9 çıktısını üretir.
range(2, 12, 3)                                             # 2, 5, 8, 11 çıktısını üretir.
range(-7, -30, -5)                                          # -7, -12, -17, -22, -27 çıktısını üretir.

# range(stop) or range(start, stop[, step])


for n in range(10):
    if n == 6:
        break
    print(n, end=',')                                       # => 0, 1, 2, 3, 4, 5, çıktısını üretir.


for n in range(10):
    if n % 2 == 0:
        print("Even", n)
        continue
    print("Odd", n)


isinstance(4, object)                                       # => True
isinstance("Hello", object)                                 # => True
isinstance(None, object)                                    # => True
isinstance([1, 2, 3], object)                               # => True


def compute(a, b, c):
    return (a + b) * c


compute(1, 2, 3)                                            # => 9 çıktısını üretir.
compute([1], [2, 3], 2)                                     # => [1, 2, 3, 1, 2, 3] çıktısını üretir.
compute('l', 'olo', 4)                                      # => 'lolololololololo' çıktısını üretir.


print(type(1) != type(1.0))

print(1 == 1.0)


print('doesn\'t')                                           # => doesn't çıktısını üretir.
print("doesn't")                                            # => doesn't çıktısını üretir.


print('"Yes," he said.')                                    # => "Yes," he said. çıktısını üretir.
print("\"Yes,\" he said.")                                  # => "Yes," he said. çıktısını üretir.
print('"Isn\'t," she said.')                                # => "Isn't," she said. çıktısını üretir.


greeting = "Hello world! "
greeting[4]                                                 # => 'o' # => True çıktısını üretir.
'world' in greeting
len(greeting)                                               # => 13 çıktısını üretir.

greeting.find('lo')                                         # => 3 (-1 if not found)
greeting.replace('llo', 'y')                                # => "hey world!"
greeting.startswith('hell')                                 # => True
greeting.isalpha()                                          # => False (due to '!')

greeting = "Hello world! "
greeting.lower()                                            # => "hello world! " çıktısını üretir.
greeting.title()                                            # => "Hello World! " çıktısını üretir.

greeting.strip()                                            # => "Hello world!" çıktısını üretir.
greeting.strip('! ')                                        # => "Hello world" (no '!') çıktısını üretir.


# `split` fonksiyonu ile string parçalama işlemi yapılır.
'ham cheese bacon'.split()                                  # => ['ham', 'cheese', 'bacon']


'03-30-2016'.split(sep='-')                                 # => ['03', '30', '2016']


# `join` listenin elemanlarından string oluşturur.
', '.join(['Eric', 'John', 'Michael'])                      # => "Eric, John, Michael"


'{} {}'.format('monty', 'python')                           # => 'monty python'


"{0} can be {1} {0}s".format("strings", "formatted")
"{name} loves {food}".format(name="Sam", food="plums")


"{} squared is {}".format(5, 5 ** 2)


# C dili formatı
"{:06.2f}".format(3.14159)                                  # => 003.14


'{:10}'.format('hi')                                        # => 'hi'
'{:^12}'.format('TEST')                                     # => '****TEST****'


captains = ['Kirk', 'Picard']
"{caps[0]} > {caps[1]}".format(caps=captains)


# C dili formatı
"%s, %s, %s. (Act %d)" % ('Words', 'words', 'words', 2)     # => Words, words, words. (Act 2) çıktısını üretir.


age = 15

"I am " + str(age) + " years old."


with open('file.txt', 'r') as f:
    content = f.read()


import math

math.sqrt(16)                                               # => 4  çıktısını üretir.


from math import ceil, floor

ceil(3.7)                                                   # => 4.0
floor(3.7)                                                  # => 3.0
