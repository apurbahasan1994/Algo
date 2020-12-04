obj=[1,2,3]
profit=[10, 30, 20]
weight=[5, 10, 15]
n=len(profit)
m=100

def knspsack(m,n):
    if m==0 or n==0:
        return 0
    if obj[n-1]<=m:
        return max(profit[n-1]+knspsack(m-weight[n-1],n),knspsack(m,n-1))
    else:
        return knspsack(m, n - 1)

print(knspsack(m,n))