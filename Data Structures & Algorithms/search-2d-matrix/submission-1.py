class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        L = 0
        R = len(matrix) - 1
        while L <= R:
            mid = (L+R) // 2
            if target in matrix[mid]:
                return True
            elif target > matrix[mid][-1]:
                L = mid + 1
            else:
                R = mid - 1
        return False
