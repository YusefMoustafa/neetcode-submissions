class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given arr of integers sorted in ascending order and target int
        # we want to search for target in the arr and return its idx, if it dne return -1
        # use binary search to efficiently search for our given target
        # set up 2 ptrs L,R
        # as long as L is <= R ptr we can calc the midpt and compare that val with target val
        # if target < nums[mid] then we need to remove the search space to the right, so we update R to mid-1
        # if target > nums[mid], then we need to remove the search space to the left, so we update L to mid+1
        # if target == nums[mid], then return the idx of mid which is js mid

        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L+R) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                R = mid - 1
            else:
                L = mid + 1
        return -1