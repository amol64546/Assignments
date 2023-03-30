factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

#input
n = int(input("Enter a number to find factorial: "))

#output
print("factorial of",n,"=",factorial(n))