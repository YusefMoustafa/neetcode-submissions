class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, count in freq_map.items():
            buckets[count].append(num)
        
        res = []

        for i in buckets[::-1]:
            for val in i:
                res.append(val)
                if len(res) == k:
                    return res
