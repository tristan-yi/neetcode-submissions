class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containsDupes = set()

        for num in nums:
            if num in containsDupes:
                return True
            containsDupes.add(num)
        return False
        