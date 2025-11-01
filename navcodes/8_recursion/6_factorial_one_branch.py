def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)

def factorial_iterative(n):
    res = 1

    while n > 0:
        res *= n
        n -= 1
    return res 

if __name__ == "__main__":
    print(factorial(5))
    print(factorial_iterative(5))