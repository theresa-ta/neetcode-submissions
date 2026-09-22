class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keep_count = {}

        for num in nums:
            if num in keep_count:
                keep_count[num] += 1
            else:
                keep_count[num] = 1

        sorted_value = sorted(keep_count.items(), key = lambda x: x[1], reverse = True)

        return [x[0] for x in sorted_value[:k]] #starting from list end to k] 
        #x[0] bc we used key = lambda x: x[1] which created a temp variable x that stores key pair values of keep_count.items(). thats why we were able to sort it by x[1] (value, amt of time num occured) and then returned x[0] (the correclated key with the value)