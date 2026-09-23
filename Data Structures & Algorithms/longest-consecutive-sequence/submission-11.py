class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #O(nlogn) solution 
        nums_set = set()
        longest_seq = 1
        count = 1

        if len(nums) == 0:
            return 0
    
        for num in nums:
            nums_set.add(num)

        arr_set = list(nums_set)
        arr_set.sort()

        for i in range(len(arr_set)-1):
            if arr_set[i]+1 == arr_set[i+1]:
                count += 1
            else:
                if count > longest_seq:
                    longest_seq = count
                count = 1

        if count > longest_seq:
            longest_seq = count

        return longest_seq