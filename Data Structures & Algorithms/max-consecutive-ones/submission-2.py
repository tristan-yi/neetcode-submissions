class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        longest = 0
        length = 0
        for num in nums:
            if num == 1:
                length += 1
                longest = max(longest, length)
            else:
                length = 0

        return longest
        


        