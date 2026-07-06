class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0

        left, right = 0, len(heights) - 1

        while left < right:
            area = min(heights[right], heights[left]) * (right - left)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
            most = max(area, most) 
        return most

        