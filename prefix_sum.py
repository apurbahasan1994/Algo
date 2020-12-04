array=[10,1,2,3,4,5]
sum_p=[0]*len(array)
def prefix_sum(array,sum_p,n):
    if n<=0:
        return array[0]
    sum_p[n]+=array[n]+prefix_sum(array,sum_p,n-1)
    return sum_p[n]
print(prefix_sum(array,sum_p,5))

