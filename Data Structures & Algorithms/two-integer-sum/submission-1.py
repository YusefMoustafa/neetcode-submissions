class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [hashmap[diff], i]