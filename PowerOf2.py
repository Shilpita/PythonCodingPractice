#Print powers of two upto input number using lambda

def power2(x):
	if x== 0:
		return 1
	elif x>0:
		pow = 2
		for i in range(1,x):
			pow = pow * 2
		return pow
	else:
		pow = 2 
		temp_x = -1* x
		for i in range(1,temp_x):
			pow = pow * 2
		return 1/pow

#take inputs
num1 = int(input("enter number1:"))

power2lambda = lambda num1:  2 ** num1

print ("power of 2 to {} is {} without lambda.".format(num1,power2(num1)))

print ("power of 2 to {} is {} with lambda.".format(num1,power2lambda(num1)))