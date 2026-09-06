class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We will use two hash_maps
        comb = {}
        for element in strs:
            hash_map = [0]*26
            
            for c in element:
                hash_map[ord(c) - ord('a')] += 1
                
            key = tuple(hash_map) #Array can't be a key in a dict
            
            if key in comb:
                comb[key].append(element)
            else:
                comb[key] = [element]
        
        result = []
        for x in comb.values():
            result.append(x)
        
        return result
                