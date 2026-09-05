class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # need to deliver packages within certain num of days
        # weights[i] is the actual weight of package i.
        # we want to return the least weight that can be packaged a day
        # need lower bound weight ( max(weights) since cant package that weight if our capacity is less than that) and upper bound weight ( sum(weights) since worst case scenario you can package all the weights in 1 day if our capacity is sum of all weights)

        lo = max(weights)
        hi = sum(weights)
        res = hi

        def testCap(cap):
            currDays = 1
            currentCap = cap
            for i in weights:
                if currentCap - i < 0:
                    currDays += 1
                    if currDays > days:
                        return False
                    currentCap = cap
                currentCap -= i
            return True

            


        while lo <= hi:
            cap = (lo + hi) // 2
            if testCap(cap):
                res = min(res, cap)
                hi = cap - 1
            else:
                lo = cap + 1
        return res

                