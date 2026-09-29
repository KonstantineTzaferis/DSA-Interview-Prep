class Solution: 
    def isPalindrome(self, s: str) -> bool: 
        # We are going to actually impemenet the two pointer approach 
        if len(s) <= 1: 
            return True

        left = 0 
        right = len(s) - 1

        while left < right: 
            while not s[left].isalnum() and left < right: 
                left += 1
            while not s[right].isalnum() and left < right: 
                right -= 1

            if s[left].lower() != s[right].lower(): 
                return False

            left += 1
            right -= 1

        return True 


                                                                                                                                                                                    