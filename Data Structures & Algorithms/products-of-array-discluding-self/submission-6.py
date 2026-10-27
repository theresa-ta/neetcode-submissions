class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_list = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            num_list[i] = prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            num_list[i] *= postfix
            postfix *= nums[i]

        return num_list