from sys import maxsize
def max_sum_subarray(a):
    max_so_far = a[0]
    max_ending_here = max(a[0], 0)


    for i in range(1, len(a)):
        max_ending_here += a[i]
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far

a = [-3, 2, -1, 4, -5]

print(max_sum_subarray(a))

def max_sum_subarray_2(a):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    start, s, end = 0, 0, 0
    for i in range(0, len(a)):
        max_ending_here += a[i]
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
    return max_so_far, start, end


a = [-3, 2, -1, 4, -5]

print(max_sum_subarray_2(a))

