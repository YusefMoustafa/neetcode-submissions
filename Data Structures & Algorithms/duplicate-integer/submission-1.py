class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for val in nums:
            if val not in freq_map:
                freq_map[val] = 1
            else:
                return True
        return False