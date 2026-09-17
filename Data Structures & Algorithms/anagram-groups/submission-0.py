class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in group_anagram:
                group_anagram[sorted_word].append(word) #dict[key].append[value]
            else:
                group_anagram[sorted_word] = [word] #dict[key] = [value]
        
        return list(group_anagram.values())
