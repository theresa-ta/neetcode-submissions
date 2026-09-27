class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) #create list of 4 with value 1

        prefix = 1 #keeping track of prefix starting at 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output


