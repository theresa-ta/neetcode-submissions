class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in count:
                return [count[difference], i] #for dictonaries, you use the key to get the value. so, count[difference] is the dictionary[key] to get the value. so, count[3] will return the value 0. the dictonary doesnt know that this is an index, just the value associated with it. but it will output 0, so [0,1]

            count[num] = i #setting the dictonary. making this count[num] = index. this is that we can output the index as the value. a dictoary is already programmed to output the value associated with the key. 


