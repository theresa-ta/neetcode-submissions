class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cur_str = {}
        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter in cur_str:
                cur_str[letter] += 1
            else:
                cur_str[letter] = 1
        
        for letter in t:
            if letter in cur_str:
                cur_str[letter] -= 1
            else:
                return False

        for count in cur_str.values():
            if count != 0:
                return False

        return True
    