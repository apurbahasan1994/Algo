string1='abcdaf'
string2='acbcf'
n=len(string1)
m=len(string2)
t=[[-1]*(n+1) for _ in range(m+1)]
for r in t:
    print(r)
def substring(m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j ==0:
                t[i][j]=0

    for  i in  range(m+1):
        for j in range(n+1):
            if string1[j-1]==string2[i-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    for r in t:
        print(r)
    return t[m][n]

print(substring(m,n))

