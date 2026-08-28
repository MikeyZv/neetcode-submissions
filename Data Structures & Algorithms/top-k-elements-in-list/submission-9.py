class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = defaultdict(int)

        for key in nums:
             hash_table[key] += 1

        res = defaultdict(int)

        while k > 0:
            max = (-math.inf, -math.inf)
            for key, val in hash_table.items():
                if val > max[1]:
                    if key in res:
                        continue
                    else:
                        max = (key, val)

            res[max[0]] = max[0]
            k -= 1

        return list(res.values())
        