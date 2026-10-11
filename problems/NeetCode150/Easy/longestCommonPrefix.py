class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0 
        lcp = ""
        while i <= 200: 
            iter_lcp = set()
            for word in strs:
                if i == len(word): 
                    return lcp 
                iter_lcp.add(word[i])
            if len(iter_lcp) > 1: 
                break
            else: 
                lcp += word[i]
            i += 1
        
        return lcp