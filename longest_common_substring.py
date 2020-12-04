string1='abcde'
string2='abfce'
m=len(string1)
n=len(string2)
t=[[-1]*(n+1) for _ in range(m+1)]
def substring(m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j ==0:
                t[i][j]=0

    for  i in  range(m+1):
        for j in range(n+1):
            if string1[i-1]==string2[j-1]:
                t[i][j]=1+t[i-1][j-1]
            # if string1[i-1]!=string2[j-1]:
            #     t[i][j]=0
            else:
                t[i][j]=0


substring(m,n)