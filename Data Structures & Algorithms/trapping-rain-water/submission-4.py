class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxL = height[L]
        maxR = height[R]
        total = 0

        while L < R:
            if maxL <= maxR:
                L += 1
                water = min(maxL, maxR) - height[L]
                if water >= 0:
                    total += water
            else:
                R -= 1
                water = min(maxL, maxR) - height[R]
                if water >= 0:
                    total += water
        
            maxL = max(maxL, height[L])
            maxR = max(maxR, height[R])

        return total
