class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in s:
            count_s[i] = 0

        for i in s:
            count_s[i] += 1

        for i in t:
            count_t[i] = 0

        for i in t:
            count_t[i] += 1

        for key, value in count_s.items():
            if key in count_t:
                if count_t[key] != value:
                    return False
            else:
                return False

        return True