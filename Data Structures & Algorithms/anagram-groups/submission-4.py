class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in count:
                count[sorted_word].append(word)

            else:
                count[sorted_word] = [word]

        return list(count.values())