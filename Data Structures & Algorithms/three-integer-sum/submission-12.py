class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(n^2) solution
        nums.sort()

        res = set()

        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue

            first = i+1
            last = len(nums)-1
            
            if nums[i] > 0:
                break
            
            while first < last:
                if (nums[i] + (nums[first] + nums[last])) < 0:
                    first += 1                
                elif (nums[i] + (nums[first] + nums[last])) > 0:
                    last -= 1   
                else:
                    res.add((nums[i], nums[first], nums[last]))  
                    first += 1
                    last -= 1

        result = []
        for l in res:
            result.append(list(l))
            
        return result

        -4,-1,-1,0,1,2





        -1,-1,2
        -1,0,1


    
