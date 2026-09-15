class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # nums = [1,1,2,3,3,4,4,8,8]
        #         L       M       R              if mid != mid + 1 or mid - 1: return mid
        #                 R                  

        #                                 if (mid - L) % 2 == 0: L = mid + 1, else: R = mid


        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2

            if (mid - 1 < 0 or nums[mid] != nums[mid + 1]) and (mid + 1 == len(nums) or nums[mid] != nums[mid - 1]):
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]: # everything up to this pair is normal so single element is on right side (even, even + 1)
                    L = mid + 1
                else:
                    R = mid                       # this tells you that the left has the single element so we shrink our search space to the left

            else:
                if nums[mid] == nums[mid - 1]:
                    L = mid + 1
                else:
                    R = mid
   
        return nums[L]