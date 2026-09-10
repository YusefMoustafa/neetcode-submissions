class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # given rotated sorted arr of len n with unique elements, which could have been rotated up to n times. 
        # given a target integer
        # want to return the index of that target int, or -1 if DNE.


        # implement a binary search algorithm
        # establish our l,R ptr and calc mid.

        # nums = [3,5,6,0,1,2], target = 4
        #         L      .     
        #           R
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                if nums[mid] < target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
        return -1
            
            