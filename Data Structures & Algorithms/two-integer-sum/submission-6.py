class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #dict

        for i, num in enumerate(nums):#for index, value in enumerate(nums), this means that it creats a tuple automatically for (i, value). so when you do for i, nums -> aka (i, value) it follows enumerate(nums)
            difference = target - num #seen[num(value)] = difference(index)

            if difference in seen:
                return [seen[difference], i] #difference = index = value
                #return [index where difference is, current i]
        
            seen[num] = i
            #else, dict[key] = the index its in. 
