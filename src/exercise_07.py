def fib(n):
    """Prints the first n Fibonacci numbers."""
    a, b = 0, 1
    for i in range(n):
        print(i, a)
        a, b = b, a + b


temp = int(input("Lütfen bir sayı giriniz? "))

fib(temp)
