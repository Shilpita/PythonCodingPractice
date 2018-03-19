## longest common substring

def lcs(s1,s2):
    n1= len(s1)
    n2= len(s2)
    mat =[[0 for k in range(n2+1)] for l in range(n1+1)]
    max =0
    index =0
    for i in range(n1+1):
        for j in range(n2+1):
            if i is 0 and j is 0:
                mat[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                mat[i][j] = mat[i-1][j-1]+1
                if max<mat[i][j]:
                    max = mat[i][j]
                    index =i
            else:
                #print(j)
                mat[i][j] = 0

    print(s1[index-max:index])
    return max


print(lcs('geeksr','geekyier'))
