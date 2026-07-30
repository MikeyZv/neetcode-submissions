class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[i] = target - nums[i]
            if h[i] in nums:
                idx = nums.index(h[i])
                if idx == i:
                    continue
                else:
                    if idx > i:
                        return [i, idx]
                    else:
                        return [idx, i]