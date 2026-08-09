class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        lst = nums.copy()

        for i in range(len(nums)):
            lst.append(nums[i])  # append each element again

        return lst
        