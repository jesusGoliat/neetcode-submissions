class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        result = ""
        mini = len(strs[0])
        
        # Find the length of the shortest string
        for i in range(1, n):
            mini = min(mini, len(strs[i]))
            
        # Vertical scanning: compare character by character
        for i in range(mini):
            c = strs[0][i]
            for j in range(n):
                if c != strs[j][i]:
                    return result
            result += c  # Correctly appends the character
            
        return result