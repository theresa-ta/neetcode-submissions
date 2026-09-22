class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_ana = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in group_ana:
                group_ana[sorted_word].append(word)
            else:
                group_ana[sorted_word] = [word]

        return list(group_ana.values())

