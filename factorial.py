# Find the factorial of a given number using recursion technique

def factorial_recursion(n):
	if n==1:
		return 1
	else :
		return (n * factorial_recursion(n-1))

# Get user input
num = int(input("Enter the number"))

# Check input factorial
if num == 0:
	print("The factorial is ", 1)
else:
	print("The factorial of the given number ", num ," is " ,factorial_recursion(num))

