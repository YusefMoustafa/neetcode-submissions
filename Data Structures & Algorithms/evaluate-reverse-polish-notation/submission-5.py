class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        # given arr of strings
        # need to return final answer to expression

        # initialize stack
        # loop through arr, convert val to int and add it to stack
        # if val is an operand then we need to pop the last 2 values in stack and then compute their result using that operand
        # add that result to the stack
        # once weve finished interating over arr, return top of stack

        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-": # make sure we do leftmost val - rightmost val
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/": # make sure we do leftmost val - rightmost val
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1)) # type cast so that it will strip off decimal and round down.
            else:
                stack.append(int(i))
            
        return stack[-1]
