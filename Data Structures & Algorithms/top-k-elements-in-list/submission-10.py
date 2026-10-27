class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        reverse_count = sorted(count, key=count.get, reverse = True)

        return reverse_count[:k]
       