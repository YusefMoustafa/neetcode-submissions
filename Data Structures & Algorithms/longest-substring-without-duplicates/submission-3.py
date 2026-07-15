class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
    # s = "zxyzxyz"
    #         L
    #            R  
    #                       window = {"x", "y", "z"  }
    #                       length = max(length, s[R]-s[L] + 1)
    # s="pwwkew" 
    #       L
    #.        R                  window = {"", "k", "e"  }. length = 3
        L = 0
        R = 0
        window = set()
        length = 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
                length = max(length, R - L + 1)
            window.add(s[R])
            length = max(length, R - L + 1)
        return length
