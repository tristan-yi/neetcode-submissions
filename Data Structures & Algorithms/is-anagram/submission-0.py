class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        check = defaultdict(int)

        for char in s:
            check[char] += 1

        for char in t:
            check[char] -= 1
            if check[char] < 0:
                return False
        
        return True
        