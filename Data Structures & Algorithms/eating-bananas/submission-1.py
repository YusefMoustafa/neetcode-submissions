class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # use max(piles) as our search range since all bananas can be eaten within h hrs and at max(piles) speed.
        # use binary search on range(1-max(piles)) to find the min rate k. 
        # 


        L = 1
        R = max(piles)

        res = R
        

        while L <= R:
            mid = (R + L) // 2
            total_hours = 0
            for i in piles:
                total_hours += math.ceil(i / mid)
            if total_hours <= h:
                res = mid
                R = mid - 1
            else:
                L = mid + 1 
        return res