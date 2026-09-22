class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cur_str = {}
        if len(s) != len(t):
            return False

        for char in s:
            if char in cur_str:
                cur_str[char] += 1
            else:
                cur_str[char] = 1
        
        for char in t:
            if char in cur_str:
                cur_str[char] -= 1
            else:
                return False

        for count in cur_str.values():
            if count != 0:
                return False
        
        return True