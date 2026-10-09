class Solution: 
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        findings = {}
        judge: int = -1
        for i in range(len(trust)): 
            if trust[i][1] not in findings: 
                findings[trust[i][1]] = [trust[i][0]]
            else: 
                findings[trust[i][1]].append(trust[i][0])
        
        for key, value in findings.items(): 
            if len(value) == n -1: 
                judge = key

        for key, value in findings.items(): 
            if judge in value: 
                judge = -1
                
        return judge

        


        