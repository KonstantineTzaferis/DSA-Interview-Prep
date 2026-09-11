class Solution: 
    def calPoints(self, operations: list[str]) -> int: 
        scores = []

        for i in range(len(operations)): 
            if operations[i] not in ["C", "+", "D"]:
                scores.append(int(operations[i]))
            else: 
                if operations[i] == "C": 
                    scores.pop()
                elif operations[i] == "D": 
                    scores.append(2*int(scores[-1]))
                else: 
                    scores.append(scores[-1] + scores[-2])

        return sum(scores)
