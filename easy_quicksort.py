#  #  ///// Quicksort///////
def quicksort(l):
    if len(l)<2:
        return l
    else:
        pivot =l[0]
        less=[]
        equal=[]
        greater=[]
        for i in range(len(l)):
            if l[i]==pivot:
                equal.append(l[i])
            elif l[i]>pivot:
                greater.append(l[i])
            elif l[i]<pivot:
                less.append(l[i])
        return quicksort(less)+equal+quicksort(greater)

l=[3,4,5,8,7,6]
print(quicksort(l))


## not memory efficient for memory purpose use inplace sorting quicksort ####
