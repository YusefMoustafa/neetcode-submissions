class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq_map = {}

        # for val in nums:
        #     if val not in freq_map:
        #         freq_map[val] = 1
        #     else:
        #         return True
        # return False


        seen = set()
        for val in nums:
            if val in seen:
                return True
            else:
                seen.add(val)
        return False