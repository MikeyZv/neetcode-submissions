class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}

        for i in nums:
            numDict[i] = 0

        for i in nums:
            numDict[i] += 1

            if numDict[i] == 2:
                return True

        return False