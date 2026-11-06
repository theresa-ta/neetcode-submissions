class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_list = [1] * len(nums)

        prefix = 1
        for num in range(len(nums)):
            count_list[num] = prefix
            prefix *= nums[num]

        postfix = 1
        for num in range(len(nums) -1, -1, -1):
            count_list[num] *= postfix
            postfix *= nums[num]

        return count_list