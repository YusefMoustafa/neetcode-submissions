class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # use max(piles) as our search range since all bananas can be eaten within h hrs and at max(piles) speed.
        # use binary search on range(1-max(piles)) to find the min rate k. 
        # 

        # need a helper function that will check if k bananas can be eaten in h hrs.
        # call the helper function in our binary search loop, and cut down search space if depending on whether or not k bananas works in h hours. 


        L = 1
        R = max(piles)

        # for every pile in piles, we want to divide that pile by k bananas. That will give us the hrs it took to eat that pile. put hours in accumulator var. if hours <= our input h, then return true else false. 
        def test_bananas(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        while L < R:
            mid = (L + R) // 2
            if test_bananas(mid):
                R = mid
            else:
                L = mid + 1
        return R