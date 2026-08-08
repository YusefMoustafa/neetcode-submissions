class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # given an arr of temps where each temperatures[i] = the temp.
        # return a result arr where each val in the number of days until the next warmer temp.
        # if no future temp > temperatures[i], result[i] = 0.

        # a stack can be used to keep track of days that are still waitinf for warmer day
        # first we iterate through the input arr
        # while our stack is not empty and the value were iterating on is greater than the val at top of the stack, we compute the days (temp[i] - stack[-1]) and add it to result[i] and pop the top of the stack.
        # if stack is empty or the val isnt greater then we still need to add the index of the temp to the stack
        # return result arr.

        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                days = i - stack[-1]
                res[stack[-1]] = days
                stack.pop()
            stack.append(i)
        return res


