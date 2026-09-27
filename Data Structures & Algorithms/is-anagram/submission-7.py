class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(t) != len(s):
            return False #can exit code early if length do not match

        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            count[char] = count.get(char, 0) -1
            
        return all(value == 0 for value in count.values()) #checks if all values in count.values() == 0