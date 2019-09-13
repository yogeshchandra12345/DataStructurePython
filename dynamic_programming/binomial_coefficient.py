"""
Optimal Solutions for finding C(n,K)
C(n, k) = C(n-1, k-1) + C(n-1, k)
C(n, 0) = C(n, n) = 1
"""


def binomial_coeff_recursion(n, k):
    """
    Binomial Coefficient using recursion function
    """
    if k == n or k == 0:
        return 1

    return binomial_coeff_recursion(n-1, k-1) + binomial_coeff_recursion(n-1, k)


print(binomial_coeff_recursion(5, 2))


def binomial_coeff_dp(n, k):
    """
    Binomial Coefficient using dynamic programming
    """
    C = [[0 for x in range(k+1)] for y in range(n+1)]

    for row in range(n+1):
        for col in range(min(row, k)+1):
            if col==0 or col == row:
                C[row][col]=1
            else:
                C[row][col] = C[row-1][col-1] + C[row-1][col]

    return C[n][k]


print(binomial_coeff_dp(5, 2))
