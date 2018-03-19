from collections import Counter

def palindrome_position(myList):
    if not myList:
        print("input empty")

    letter = dict()

    odd_count = 0
    odd = ''
    i = 0
    for x in myList:
        if x in letter.keys():
            i = i+1
            letter[x].append(i)
        else:
            i = i+1
            letter[x] = [i]

        if myList.count(x)%2 is not 0:
            odd_count = odd_count+1
            odd = x

    if odd_count > 1:
            print("Not possible")
            return

    #print(letter)
    pos =[]
    palin =""
    for x in letter.keys():
        if x is not odd :
            mid = len(letter[x])//2
            for i in range (0,mid):
                palin = palin+x
                pos.append(letter[x][i])
            #count = count+1
    if odd_count > 0 :
        pos.append(letter[odd][0])
        letter.pop(odd)
        #print(letter)

    for x in reversed(letter.keys()):
        mid = len(letter[x])// 2
        for i in range(mid, len(letter[x])):
            pos.append(letter[x][i])

    print(pos)
    return pos

myList =['c','b','b','b','b','a','a']
palindrome_position(myList)