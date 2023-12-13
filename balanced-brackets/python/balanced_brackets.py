class BalancedBrackets:
    def is_balanced(self, input):
        stack = []

        for c in input:
            if c == '[':
                stack.append(c)
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False

        return len(stack) == 0
