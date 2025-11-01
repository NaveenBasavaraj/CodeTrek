def reverse_string(s):
    if not s:
        # base case or stopping condition
        return "" 
    # what is the smallest amount of work I can do in each iteration?
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("Hello World"))