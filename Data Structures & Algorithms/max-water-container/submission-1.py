class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        biggest = 0
        while left != right:
            print(min(heights[left], heights[right]) * (right - left))
            biggest = max(min(heights[left], heights[right]) * (right - left), biggest)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return biggest
