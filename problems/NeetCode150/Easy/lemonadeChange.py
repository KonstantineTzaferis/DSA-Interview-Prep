class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = 0
        tens = 0

        if bills[0] != 5:
            return False
        else:
            fives += 1
            for i in range(1, len(bills)):
                if bills[i] == 5:
                    fives += 1
                elif bills[i] == 20:
                    if tens > 0:
                        if fives > 0:
                            tens -= 1
                            fives -= 1
                        else:
                            return False
                    else:
                        if fives > 2:
                            fives -= 3
                        else:
                            return False
                else:
                    if fives > 0:
                        fives -= 1
                        tens += 1
                    else:
                        return False

        return True


s = Solution()
print(s.lemonadeChange(bills=[5, 10, 5, 5, 20]))
