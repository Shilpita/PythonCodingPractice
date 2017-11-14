#sum =0
def calcHash(str,m):
	if m > 0:
	        sum =0
		for c in str:
			sum = sum + ord(c)

		return [sum, sum % m]

	else:
	   return [0,0]


#sum =0
#print (calcHash("Hello",100))
#print (calcHash("HelloShilpita",100))

sum, h = calcHash("Hello",100)
#print sum
str = "HelloShilpita"
for x in range(5,len(str)):
	sum = sum - ord(str[x-5])
        #print ord(str[x-5])
	sum = sum + ord(str[x])
	#print sum
        newHash = sum%m
	
