arr=[0,0,0,0,0,0,0,0,1]
sum=1
n=len(arr)
count=0
def subsetsum(sum,n):
    # global count
    # if sum==0:
    #     return 1
    # if n==0:
    #     return 0
    #
    # if arr[n-1]<=sum:
    #     return subsetsum(sum,n-1)+subsetsum(sum-arr[n-1],n-1)
    # elif arr[n-1]>sum:
    #     return subsetsum(sum,n-1)
    t=[[0]*(sum+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1

    for r in t:
        print(r)
    print('****')
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    for r in t:
        print(r)
    return t[n][sum]
print(subsetsum(sum,n))