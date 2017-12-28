#  #  ///// Quicksort///////
## not memory efficient for memory purpose use inplace sorting quicksort ##
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


## better than previous in term of memory ####
# in place sorting algorithm more memory efficient than quicksort1
def partition(l,low,high):
    pivot=low
    i=low   # use i to point to small element than pivot and previous to big element than pivot
    for j in range(low,high):
        if l[j+1]<l[pivot]:
            l[i+1],l[j+1]=l[j+1],l[i+1]
            i+=1
    l[pivot],l[i]=l[i],l[pivot]
    return i


def quicksort(l,low,high):
    if low<high:
        p=partition(l,low,high)
        first=quicksort(l,low,p-1)
        second=quicksort(l,p+1,high)
        return first+[l[p]]+second
    else:
        return l[low:high+1]

l=[8,9,5,4,6,7,-2]
print (quicksort(l,0,len(l)-1))
