class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()                      # a waiting day that today resolves
                result[j] = i - j                    # days waited
            stack.append(i)                          # today now waits for its warmer day

        return result