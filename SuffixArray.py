def getSuffixArray(str):
	visited = set()
	suffixSet = set()
	list=[]
	for i in range(0,len(str)):
		suffixSet.add(str[i:])
	print suffixSet
	for c in str:
		if not c in visited:
			list.append(c)
			visited.add(c)
	list.sort()
	print list


getSuffixArray("banana")
