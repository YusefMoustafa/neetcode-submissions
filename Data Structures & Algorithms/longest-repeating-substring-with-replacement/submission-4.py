class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        count = {}

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            window_len = R - L + 1
            max_freq = max(count.values())
            while window_len - max_freq > k:
                count[s[L]] = count.get(s[L], 0) - 1
                L += 1
                window_len = R - L + 1

            res = max(res, window_len)
        return res
