class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {} 

        for char in s:
            count[char] = count.get(char, 0) + 1 #get the character in count, if not there return 0. if it is, add 1.
            
        for char in t:
            count[char] = count.get(char, 0) - 1
        
        return all(value == 0 for value in count.values())