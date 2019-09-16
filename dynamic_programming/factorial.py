def factorial(n):
    if n < 0:
        return -1
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(-1))

def factorial_dp(n):
    result = [0 for _ in range(n+1)]
    if n > 0:
        result[0] = 1
        for i in range(1, n+1):
            result[i] = i*result[i-1]
        return result[n]
    return -1

print(factorial_dp(-1))