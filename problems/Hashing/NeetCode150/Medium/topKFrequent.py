from tkinter import W
class Solution: 
    def topKFrequent(self, nums: list[int], k: int) -> list[int]: 
        counts = {}

        for num in nums: 
            if num not in counts: 
                counts[num] =1 
            else: 
                counts[num] += 1

        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        final_array = []

        for key in sorted_counts.keys(): 
            final_array.append(sorted_counts[key])

        return final_array[:k]


