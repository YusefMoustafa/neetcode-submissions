class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        window = set()
        L = 0
        length = 0
        
        for R in range(len(s)):
            if s[R] not in window:
                window.add(s[R])
                length = max(length, R - L + 1)
            else:
                while s[R] in window:

                    window.remove(s[L])
                    L += 1
                window.add(s[R])
                length = max(length, R-L+1)

        return length
            