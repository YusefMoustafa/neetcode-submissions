class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        L = 0
        R = len(heights)-1

        while L < R:
            min_val = min(heights[L], heights[R])
            area = min_val * (R-L)
            max_area = max(area, max_area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return max_area

            
