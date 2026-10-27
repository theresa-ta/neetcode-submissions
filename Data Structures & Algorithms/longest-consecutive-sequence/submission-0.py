class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0 

        for num in new_nums:
            if num - 1 not in new_nums: #if num -1 is in new_nums, its not the start
                count = 1
                while num + count in new_nums:
                    count += 1
                
                longest = max(longest, count)
        return longest