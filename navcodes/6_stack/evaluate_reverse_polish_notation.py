class Solution:
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c in {"+", "-", "*", "/"}:
                a, b = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(b + a)
                elif c == "-":
                    stack.append(b - a)
                elif c == "*":
                    stack.append(b * a)
                else:  # division
                    # force truncate toward zero (like LeetCode expects)
                    stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    print(Solution().evalRPN(tokens))

    tokens = ["4","13","5","/","+"]
    print(Solution().evalRPN(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(tokens))
