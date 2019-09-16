def fibonacci(n):
    if n<0:
        return 'incorrect input'
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

def fibonacci_2(n):
    a = 0
    b = 1
    if n < 0:
        return 'incorrect input'
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        c = a+b
        a = b
        b = c
    return b

print(fibonacci_2(5))