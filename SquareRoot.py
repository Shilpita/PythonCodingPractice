# Find sqaure root of input
import cmath

num = int(input('Enter number :'))
sqrt = num ** 0.5  # sq.rt x = x^(1/2)
print("the square root of {} is {} without cmath".format(num,sqrt))

num1 =  input('Enter number :')
sqrt1 = cmath.sqrt(num1)
print("the square root of {} is {}+{}j with cmath".format(num1,sqrt1.real,sqrt1.imag))