class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Given that we are trying to return an array where each num is the 
        # product of all elements we want to get the prefix array and the suffix array.
        # then we will multiply the prefix[i] by suffix[i+1] and return our res array. 

        prefix = [1] * (len(nums) + 1) # [1,1,1,1,1]

        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i-1] * nums[i-1] # [1,1,2,8,48]

        suffix = [1] * (len(nums) + 1)  # [1,1,1,1,1]
        for i in range((len(nums) -1), -1, -1):
            suffix[i] = suffix[i+1] * nums[i] # [48,48,24,6,1]

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i+1])

        return output

        
