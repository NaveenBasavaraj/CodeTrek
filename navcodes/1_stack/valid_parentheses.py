class ValidParentheses:
    def solution(self, s):
        stack = []
        close_to_open_map = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in close_to_open_map: 
                if stack and stack[-1] == close_to_open_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)  # FIXED: previously missing argument
        
        return not stack  # valid only if stack is empty at the end


def main():
    vp = ValidParentheses()
    
    # Valid cases
    print(vp.solution("()"))        # True
    print(vp.solution("()[]{}"))    # True
    print(vp.solution("{[()]}"))    # True

    # Invalid cases
    print(vp.solution("(]"))        # False
    print(vp.solution("([)]"))      # False
    print(vp.solution("{[]}"))      # True
    print(vp.solution("((("))       # False


if __name__ == "__main__":
    main()
