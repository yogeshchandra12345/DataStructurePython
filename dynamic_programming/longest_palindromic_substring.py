def longest_palindromic_substring(a):
    b = ''.join([x for x in a][::-1])

    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]

    for row in range(1, len(a)+1):
        for col in range(1, len(a)+1):
            if a[row-1] == b[col-1]:
                dp[row][col] = dp[row-1][col-1]+1
            else:
                dp[row][col] = 0 #max(dp[row - 1][col], dp[row][col-1])

    return dp[-1][-1]


x = 'avna'
print(longest_palindromic_substring(x))