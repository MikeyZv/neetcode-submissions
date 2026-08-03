class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)

        for word in strs:
            count_letters = [0]*26
            for char in word:
                count_letters[ord(char)-ord('a')] += 1
        
            hash_key = tuple(count_letters)
            hash_table[hash_key].append(word)
        
        result = []
        for k, v in hash_table.items():
            result.append(v)

        return result
        
