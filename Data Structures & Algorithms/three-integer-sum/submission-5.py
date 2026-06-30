class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i>0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            L = i + 1
            R = len(sorted_nums)-1
            while L < R:
                if sorted_nums[i] + sorted_nums[L] + sorted_nums[R] > 0:
                    R -= 1
                elif sorted_nums[i] + sorted_nums[L] + sorted_nums[R] < 0:
                    L += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[L], sorted_nums[R]])
                    L += 1
                    R -= 1
                    while L < R and sorted_nums[L] == sorted_nums[L-1]:
                        L +=1
                    while L < R and sorted_nums[R] == sorted_nums[R+1]:
                        R-=1
        return res
                