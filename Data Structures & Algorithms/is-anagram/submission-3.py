class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        hashmap_s = {}
        hashmap_t = {}

        for char in s:
            if char not in hashmap_s:
                hashmap_s[char] = 1
            else:
                hashmap_s[char] += 1
        for char in t:
            if char not in hashmap_t:
                hashmap_t[char] = 1
            else:
                hashmap_t[char] += 1

        if hashmap_s == hashmap_t:
            return True

        return False