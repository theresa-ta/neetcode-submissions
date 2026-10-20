class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
    count = {}

    for i, num in enumerate(nums):
        difference = target - num

        if difference in count:
            return [count[difference], i]

        count[num] = i

