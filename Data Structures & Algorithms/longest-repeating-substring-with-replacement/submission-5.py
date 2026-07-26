class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
    
    #    s = "XYYXXXX", k = 2              count= {X:3, Y:2}.     maxFreq = 4
    #          L                         windowLen = 6           res = 5
    #              R                         k = 1

    # windowLen - maxFreq > k. if so then we update our res = windowLen


        count = {}
        L = 0
        res = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            windowLen = R - L + 1
            maxFreq = max(count.values())
            while windowLen - maxFreq > k:
                count[s[L]] = count.get(s[L], 0) - 1
                L += 1
                windowLen = R - L + 1
            res = max(res, windowLen)
        return res
            
