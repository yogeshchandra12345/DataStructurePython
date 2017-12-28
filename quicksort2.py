# in place sorting algorithm more memory efficient than quicksort1
def partition(l,low,high,reverse=False):
    if reverse==True:
        pivot = low
        i = low  # use i to point to small element than pivot and previous to big element than pivot
        for j in range(low, high):
            if l[j + 1] > l[pivot]:
                l[i + 1], l[j + 1] = l[j + 1], l[i + 1]
                i += 1
        l[pivot], l[i] = l[i], l[pivot]
        return i
    else:
        pivot = low
        i = low  # use i to point to small element than pivot and previous to big element than pivot
        for j in range(low, high):
            if l[j + 1] < l[pivot]:
                l[i + 1], l[j + 1] = l[j + 1], l[i + 1]
                i += 1
        l[pivot], l[i] = l[i], l[pivot]
        return i


def quicksort(l,low,high,reverse=False):
    if reverse==True:
        if low < high:
            p = partition(l, low, high,True)
            first = quicksort(l, low, p - 1,True)
            second = quicksort(l, p + 1, high,True)
            return first + [l[p]] + second
        else:
            return l[low:high + 1]



        pass
    else:

        if low<high:
            p=partition(l,low,high)
            first=quicksort(l,low,p-1)
            second=quicksort(l,p+1,high)
            return first+[l[p]]+second
        else:
                return l[low:high+1]

l=[8,9,5,4,6,7,-2]
print (quicksort(l,0,len(l)-1,reverse=True))
