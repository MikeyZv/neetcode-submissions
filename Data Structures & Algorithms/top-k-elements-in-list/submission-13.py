class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}

        for key in nums:
             hash_table[key] = 0

        for key in nums:
             hash_table[key] += 1
        
        freq_arr = [[] for _ in range(len(nums)+1)]

        for key, val in hash_table.items():
            freq_arr[val].append(key)

        res = []

        for i in range(len(freq_arr)-1,-1,-1):
            if k > 0:
                if freq_arr[i]:
                    if k <= len(freq_arr[i]):
                        res += (freq_arr[i][:k])
                        k -= len(freq_arr[i][:k])
                    else:
                        res += (freq_arr[i])
                        k -= len(freq_arr[i])

        return res
        