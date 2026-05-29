class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # hashmap_s = {}
        # hashmap_t = {}

        # for char in s:
        #     if char not in hashmap_s:
        #         hashmap_s[char] = 1
        #     else:
        #         hashmap_s[char] += 1
        # for char in t:
        #     if char not in hashmap_t:
        #         hashmap_t[char] = 1
        #     else:
        #         hashmap_t[char] += 1

        # if hashmap_s == hashmap_t:
        #     return True

        # return False

        count = [0] * 26
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
