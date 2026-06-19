class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
    # given sorted arr of integers. 
    # return indices of 2 nums in arr that add up to target num. 
    # cannot use extra space. 
    # use 2 pointers at both ends of list, if values at L + R > Target val, then dec R.
    # if values at L + R < Target val, then increment L. 
    # if values at L + R == target val, then return [L, R]

        L = 0
        R = len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            elif numbers[L] + numbers[R] == target:
                return [L+1, R+1]