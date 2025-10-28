def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        # If we've used all parentheses (n opens and n closes)
        if len(current) == 2 * n:
            result.append("".join(current))
            return

        # If we can add an open bracket, do it
        if open_count < n:
            current.append("(")
            backtrack(current, open_count + 1, close_count)
            current.pop()  # undo the move

        # If we can add a close bracket, do it
        if close_count < open_count:
            current.append(")")
            backtrack(current, open_count, close_count + 1)
            current.pop()  # undo the move

    backtrack([], 0, 0)
    return result
