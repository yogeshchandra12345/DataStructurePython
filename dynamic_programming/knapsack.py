def knapsack(weights_, values_, w):
    n = len(weights_)
    dp = [[0 for _ in range(0, w+1)] for _ in range(0, n+1)]

    for i in range(1, n+1):
        for j in range(1, w+1):
            if weights_[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], values_[i-1] + dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][w]


values = [12, 1000, 30, 10, 1000]  # values of each item
weights = [19, 120, 20, 1, 120]  # weights of each item in same order
W = 40
print(knapsack(weights, values, W))

