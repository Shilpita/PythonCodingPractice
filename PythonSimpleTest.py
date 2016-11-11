# create random number
import random

num = random.random()	
num1 = random.randint(0,100)
print num," and ", num1

#swap
x = 5
y = 8
print "before  swap " ,x ," and ",y
x,y =y,x
print "after swap " ,x ," and ",y

# Celsius to Farenheit

celsius = float(input("enter temp (C):"))
farenheit = (celsius * 1.8)+32
print ("%0.2f celsius in farenheit is %0.2f"%(celsius,farenheit))

# Area of trinagle
print "Enter the sides:"
a = 5
b = 3
c = 4
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print "The area of triangle with sides ",a,",",b,",",c ,"is ", area

# Enter year Leap year
year = int(input("enter year"))
if year < 0:
	print "Invalid year"
else:
	if year %4 ==0 :
		if year %100 == 0:
			if year% 400 == 0 :
				print year," is leap year!"
			else:
				print year," is not leap year!"
		else:
			print year," is leap year!"
	else:
		print year," is not leap year!"