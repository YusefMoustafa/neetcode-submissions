class Solution:
    def isPalindrome(self, s: str) -> bool:
        

       # given a string s. return true if palindrome. else false. 
       # lowercase the string. remove whitespace. remove non alnum chars. 

       
        clean_s = ''
        for i in s:
            if i.isalnum():
                clean_s += i.lower()

        L = 0
        R = len(clean_s) - 1
        while L < R:
            if clean_s[L] != clean_s[R]:
                return False
            L += 1
            R -= 1
        return True