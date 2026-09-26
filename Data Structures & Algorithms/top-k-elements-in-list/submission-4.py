class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first, you want to take the input and put it in a dict
        #the dict will be frequency[letter] = count

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        sorted_count = sorted(count, key=count.get, reverse=True)

        return sorted_count[:k]