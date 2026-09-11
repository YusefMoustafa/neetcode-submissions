class Solution:
    def findPeakElement(self, nums: List[int]) -> int:


# nums = [1,2,3,1]

        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2
            if nums[mid] < nums[mid+1]:
                L = mid + 1
            else:
                R = mid
        return L

