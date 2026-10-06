class Solution: 
    def firstOccur(self, haystack: str, needle: str) -> int: 
        haystack_idx = 0 
        while haystack_idx + len(needle) <= len(haystack): 
            if haystack[haystack_idx:haystack_idx+len(needle)] == needle:
                return haystack_idx 
            else: 
                haystack_idx += 1
      
        return -1


s = Solution()
print(s.firstOccur("asdfasdfneet", "neet"))


                
