class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keep_count = {}

        for num in nums:
            if num in keep_count:
                keep_count[num] += 1
            else:
                keep_count[num] = 1

        sorted_value = sorted(keep_count.items(), key = lambda x: x[1], reverse = True)

        return [x[0] for x in sorted_value[:k]]