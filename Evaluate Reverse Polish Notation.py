class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                stack.append(-stack.pop() + stack.pop())
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                stack.append(int((1/float(stack.pop())) * stack.pop()))
            else:
                stack.append(int(i))
        return stack[0]
        