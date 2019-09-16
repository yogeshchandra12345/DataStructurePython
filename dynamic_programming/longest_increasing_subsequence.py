def longest_increasing_subsequence(a):
    n = len(a)
    lis = [1]*n

    # Compute LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return lis


a = [10, 22, 9, 33, 21, 50, 41, 60]

print(longest_increasing_subsequence(a))
