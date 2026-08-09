class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            count = defaultdict(int)
            minVal = min(nums)
            maxVal= max(nums)
            #(O n+n)

            for val in nums:
                count[val] += 1

            index = 0
            for val in range(minVal, maxVal +1):
                while count[val] > 0:
                    nums[index] = val
                    index +=1
                    count[val] -=1

        counting_sort()
        return nums
                            