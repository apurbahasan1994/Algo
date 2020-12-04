profit=[20,15,10,5,1]
deadline=[2,2,1,3,3]

def job_scheduling():
    slots=[0]*(max(deadline))

    for i in range(len(profit)):
        for j in range(deadline[i]-1,-1, -1):
            if slots[j]==0:
                slots[j] = i
                break


        # if slots[deadline[i]]==0:
        #     slots[deadline[i]]=i
        # else:
        #     for j in range(min(len(deadline)-2,deadline[i]-5), -1, -1):
        #         if slots[deadline[j]]:
        #             continue
        #         else:
        #             slots[deadline[j]]=i
    print(slots)

job_scheduling()


