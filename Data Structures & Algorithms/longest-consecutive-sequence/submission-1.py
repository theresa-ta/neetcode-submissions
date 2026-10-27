class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_list = set(nums)
        longest = 0

        for num in nums_list:
            if num - 1 not in nums_list:
                count = 1

                while num + count in nums_list:
                    count += 1

                longest = max(longest, count)

        return longest