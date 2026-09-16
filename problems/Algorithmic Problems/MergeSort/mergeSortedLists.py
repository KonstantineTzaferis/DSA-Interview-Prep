class Solution: 
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None: 
        """Do not return anything, just modify the nums1 in place."""
        k = 0 
        while k < len(nums2): 
            if m == 0: 
                nums1[k] = nums2[k]
            else: 
                j = m # Index for the nums1 array
                i = j - 1 # Index for the previous element 
                nums1[j] = nums2[k]
                while i >= 0: 
                    if nums1[j] <= nums1[i]: 
                        tmp = nums1[j]
                        nums1[j] = nums1[i]
                        nums1[i] = tmp
                        i -= 1
                        j -= 1
                    else: 
                        break 

                m += 1
            k += 1

