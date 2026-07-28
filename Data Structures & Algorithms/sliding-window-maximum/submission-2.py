class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        # we want to return a list that contains the max element in each window of size k
        # use 2 ptrs. Use R ptr to iterate through input arr
        # for each num we will check if len(q)>0 and nums[R] > nums[q[R]],
        # if so that means that the rightmost number is less than what were gonna add to q. 
        # so we pop it since its impossible for that number to now be the max
        # then we append R to the queue once we popped all the values less than R.
        # 
        q = collections.deque()
        res = []

        L = 0
        for R in range(len(nums)):
            while len(q) > 0 and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)
            if L > q[0]:
                q.popleft()
            if (R+1) >= k:
                res.append(nums[q[0]])
                L += 1
        return res