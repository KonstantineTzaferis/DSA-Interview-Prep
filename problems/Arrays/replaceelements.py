class Solution: 
    def replaceElements(self, arr: list[int]) -> list[int]: 
        current_max = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            tmp = arr[i]
            arr[i] = current_max 
            
            if tmp >= current_max: 
                current_max = tmp 
        arr[-1] = -1 
        return arr
        
