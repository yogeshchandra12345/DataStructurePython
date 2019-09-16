def lcs(a, b):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    max_ = 0
    for row in range(1, len(b)+1):
        for col in range(1, len(a)+1):
            if b[row-1] == a[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = 0
            max_ = max(max_, dp[row][col])

    return max_


X = "FABCDGH"
Y = "ABDCDGH"
print("Length of LCS = ", lcs(X, Y))

