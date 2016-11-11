num = int(input("enter num"))
def recur_fact(n):
	#factorial =1
	if n== 1:
		return n
	else :
		return n * recur_fact(n-1)
if num == 0:
	print("zero! Factorial of zero is 1")
elif num > 0:
	print recur_fact(num)
	# factorial = 1
	# for i in range(1,num+1):
	# 	factorial = factorial*i
	# print "positive ! factorial of",num,"is:",factorial
else:
	print("negative")

