class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        mid = -1
        while start <= end:
            mid = (start + end) // 2
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][-1]:
                start = mid + 1
            else:
                break

        # print(mid)
        if start > end:
            return False
        
        start = 0
        end = len(matrix[mid]) - 1
        mid2 = -1
        
        while start <= end:
            mid2 = (start + end) // 2
            if target > matrix[mid][mid2]:
                start = mid2 + 1
            elif target < matrix[mid][mid2]:
                end = mid2 - 1
            else:
                print(mid,mid2)
                return True
        return False
            



        