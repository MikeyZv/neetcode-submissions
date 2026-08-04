class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers)-1

        while first < last:
            if numbers[first] + numbers[last] > target:
                last -= 1
                continue
            elif numbers[first] + numbers[last] < target:
                first += 1
                continue
            else:
                break
                
        first += 1
        last += 1

        return [first, last] 