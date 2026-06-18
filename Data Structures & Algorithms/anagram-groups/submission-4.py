class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) #create hashmap

        for word in strs: #iterate through strs array
            count = [0] * 26 #create buckets for letters
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)
            anagrams[key].append(word)

        return list(anagrams.values())

        