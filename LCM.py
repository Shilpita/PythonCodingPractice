#Find LCM of two input numbers
def LCM(x,y):
	if x > y:
		greater = x
	else:
		greater = y
	while(1):
		if greater%x == 0 and greater%y == 0:
			print ('LCM of {} and {} is {}'.format(x,y,greater))
			break
		else:
			greater = greater +1

#take inputs
num1 = int(input("enter number1:"))
num2 = int(input("enter number2:"))

LCM(num1,num2)
