class Solution: 
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        if sum(students) == sum(sandwiches): 
            return 0
        else: 
            while True: 
                if students[0] == sandwiches[0]: 
                    students = students[1:]
                    sandwiches = sandwiches[1:]
                else: 
                    top_student = students[0]
                    students = students[1:] + [top_student]
                if len(set(students)) == 1 and students[0] != sandwiches[0]: 
                    break 
                

        return len(students)

s = Solution()
print(s.countStudents(students=[1,1] , sandwiches=[0, 1]))