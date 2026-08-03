class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1]
        suffix = [1]

        for n in range(1,len(nums)):
            prefix.append(nums[n-1] * prefix[n-1])

        for n in range(len(nums)-2,-1,-1):
            suffix = [nums[n+1] * suffix[0]] + suffix

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res