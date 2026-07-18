class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count = [0] * 26
        s2count = [0] * 26


        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        
        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[R]) - ord('a')
            s2count[idx] += 1
            if s2count[idx] == s1count[idx]:
                matches += 1
            elif s2count[idx] == s1count[idx] + 1:
                matches -= 1

            idx = ord(s2[L]) - ord('a')
            s2count[idx] -= 1
            if s2count[idx] == s1count[idx]:
                matches += 1
            elif s2count[idx] == s1count[idx] - 1:
                matches -= 1
            L += 1
        if matches == 26:
            return True
        else:
            return False
