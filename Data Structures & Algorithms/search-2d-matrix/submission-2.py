class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        L = 0
        R = len(matrix) - 1
        while L <= R:
            mid = (L+R) // 2
            if target > matrix[mid][-1]:
                L = mid + 1
            elif target < matrix[mid][0]:
                R = mid - 1
            else:
                l = 0
                r = len(matrix[mid]) - 1
                while l<=r:
                    inner_mid = (l+r) // 2
                    if target == matrix[mid][inner_mid]:
                        return True
                    elif target > matrix[mid][inner_mid]:
                        l = inner_mid+1
                    else:
                        r = inner_mid -1
                return False
        return False
