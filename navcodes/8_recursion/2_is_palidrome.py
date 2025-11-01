def is_palindrome(s):
    # base case or stopping condition
    if len(s) == 0 or len(s) == 1:
        return True
    
    # do some work to shrink the problem space
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    
    # additional base case to handle non palindromes
    return False 

if __name__ == "__main__":
    print(is_palindrome("KAYAKA"))
    print(is_palindrome("KAYAK"))