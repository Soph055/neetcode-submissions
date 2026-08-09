class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = n + m - 1
        #idea we start at end of nums 2 and and compare with last value of nums1
        while n > 0 and m > 0: 

            #we know nums2 is sorted so nums2[n] is biggest value is nums2
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
    
        while n > 0:
            nums1[last] = nums2[n -1]
            n -= 1
            last -=1
            



