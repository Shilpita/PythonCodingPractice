def lps(str):
    n = len(str)
    table =[[0 for col in range(n)] for row in range(n)]
    maxlength =1
    start = 0
    for i in range(0,n):
        table[i][i] = True

    for i in range(0,n-1):
        if str[i] == str[i+1] :
            table[i][i+1] = True
            start =i
            maxlength = 2
        else:
            table[i][i + 1] = False


    for k in range(3,n+1):
        for i in range(0,n-k+1):
            j = i+k-1
            if table[i+1][j-1] and str[i] == str[j]:
                table[i][j] = True
                if(maxlength < k):
                    maxlength = k
                    start = i
            else:
                table[i][j] = False


    print(str[start:start+maxlength])
    return maxlength


l = lps('geekee')
print(l)