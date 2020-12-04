activity=[1,2,3,4,5,6]
start=[0,3,1,5,5,8]
finish=[6,4,2,9,7,9]
n=6
def activity_selection(activity,start,finish):
    sorted_activity=[x for x,y,z in sorted(zip(activity,finish,start),key=lambda x:x[1])]
    sorted_finishtime=[y for x,y,z in sorted(zip(activity,finish,start),key=lambda x:x[1])]
    sorted_startime = [z for x, y, z in sorted(zip(activity, finish, start), key=lambda x: x[1])]
    print(sorted_activity)
    print(sorted_startime)
    print(sorted_finishtime)
    ans=0
    print(sorted_activity[0])
    for i in range(1,len(activity)):
        if sorted_startime[i] >= sorted_finishtime[ans]:
            ans = i
            print(sorted_activity[i])

activity_selection(activity,start,finish)