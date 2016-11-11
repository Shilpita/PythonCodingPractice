#Check if input is armstong number
num = int(input("Enter number :"))
sum=0
temp = num
while temp > 0:
	sum+= (temp%10)**3
	temp = temp/10

if num==sum:
   print(num, " is armstrong number")
else:
   print(num, " is not armstrong number")