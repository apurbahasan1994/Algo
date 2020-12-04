coin=[1,2,5]
sum=5
n=3

# def coin_chnage(sum,n):
#     if n==0 and sum==0:
#         return 1
#     if n == 0:
#         return 0
#     if sum == 0:
#         return 1
#
#     if coin[n-1]<=sum:
#         return coin_change(sum,n-1)+coin_chnage(sum-coin[n-1],n)
#     else:
#         return coin_chnage(sum,n-1)
#
# print(coin_chnage(sum,n))

def coin_change(sum,n):
    t=[[0]*(sum+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1


    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coin[i-1]<=j:
                t[i][j]=t[i-1][j]+t[i][j-coin[i-1]]
            else:
                t[i][j]=t[i-1][j]
    for r in t:
        print(r)
    return (t[n][sum])

print(coin_change(sum,n))