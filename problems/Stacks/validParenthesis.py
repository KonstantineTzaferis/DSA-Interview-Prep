class Solution: 
    def isValid(self, s: str) -> bool:
        par = "()"
        cr = "{}"
        br = "[]"
        o = "({["


        opening = []
        closing = []

        # Iteration through the string 
        for i in range(len(s)): 
            if s[i] not in o and len(opening) == 0: 
                return False
            else:
                if s[i] in o: 
                    opening.append(s[i])
                else: 
                    closing.append(s[i])
                    outcome = opening[-1] + closing[0]
                    if outcome == par or outcome == cr or outcome == br: 
                        opening.pop()
                        closing.pop()
                    else: 
                        return False 

        return len(opening) == 0 and len(closing) == 0
    

s = Solution()
st = "([{}])"
print(s.isValid(st))