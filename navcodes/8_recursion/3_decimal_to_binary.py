def decimal_to_binary(decimal, result=""):
    if decimal == 0:
        return result or "0"
    
    result = str(decimal%2) + result
    return decimal_to_binary(decimal//2, result)

if __name__ == "__main__":
    print(decimal_to_binary(0))
    print(decimal_to_binary(1))
    print(decimal_to_binary(2))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(19))