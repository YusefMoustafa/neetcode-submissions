class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        countT = {}
        window = {}
        for i in t:
            countT[i] = countT.get(i, 0) + 1

        need = len(countT)
        have = 0
        minRes = [-1, -1]
        resLen = float('infinity')

        L = 0
        for R in range(len(s)):
            window[s[R]] = window.get(s[R], 0) + 1
            if s[R] in countT and window[s[R]] == countT[s[R]]:
                have += 1
            while have == need:
                length = R - L + 1
                if length < resLen:
                    resLen = length
                    minRes = [L,R]
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1

        L, R = minRes
        if resLen != float('infinity'):
            return s[L:R+1]
        else:
            return ''




        