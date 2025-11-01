def sum_of_natural_numbers(n):
    if n<=1:
        return n
    return n + sum_of_natural_numbers(n-1)

if __name__ == "__main__":
    print(sum_of_natural_numbers(10))
    print(sum_of_natural_numbers(11))
    print(sum_of_natural_numbers(12))