def merge(l,r):
    result=[]
    i,j=0,0

    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    while i<len(l):
        result.append(l[i])
        i+=1
    while j<len(r):
        result.append(r[j])
        j+=1
    return result


def mergesort(l):
    if len(l)<2:
        return l
    else:
        mid=len(l)//2
        first=mergesort(l[:mid])
        second=mergesort(l[mid:])
        return merge(first,second)

print (mergesort([2,1,3,6,7,5,-1,-3]))
