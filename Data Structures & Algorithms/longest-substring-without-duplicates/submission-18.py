class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = 0
        count = 0
        max_count = 0

        for i in range(len(s)):
            if s[i] in hash_map and left <= hash_map[s[i]]:
                if count > max_count:
                    max_count = count
                left = hash_map[s[i]] + 1
                hash_map[s[i]] = i
            else:
                hash_map[s[i]] = i
                count = (i+1) - left
                
        if count > max_count:
            max_count = count

        return max_count

        dvdsa

        pwwkew

        txesdt