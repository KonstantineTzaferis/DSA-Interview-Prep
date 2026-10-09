class Solution: 
    def mergeAlternatively(self, word1: str, word2: str) -> str: 
        final = "" 
        if len(word1) >= len(word2): 
            for i in range(len(word1)): 
                if i > len(word2) - 1: 
                    final += word1[i]
                else: 
                    final += word1[i]
                    final += word2[i]
        else: 
            for i in range(len(word2)): 
                if i > len(word1) - 1: 
                    final += word2[i]
                else: 
                    final += word1[i]
                    final += word2[i]
        
        return final
        