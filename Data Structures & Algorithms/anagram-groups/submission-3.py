class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for word in strs:
            sorting_word = "".join(sorted(word))

            if sorting_word in count:
                count[sorting_word].append(word)
            else:
                count[sorting_word] = [word]

        return list(count.values())