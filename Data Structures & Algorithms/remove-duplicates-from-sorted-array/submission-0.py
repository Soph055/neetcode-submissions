class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        tracker = 0  # points to last unique element
        i = 1        # scan from the second element

        while i < len(nums):
            if nums[i] != nums[tracker]:
                tracker += 1
                nums[tracker] = nums[i]
            i += 1  # always move the scan pointer forward

        return tracker + 1  # number of unique elements



      

