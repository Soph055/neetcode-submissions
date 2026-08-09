class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        times = n // 2
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        for k in dic.keys():
            if dic[k] > times:
                return k
            
#hashmap method O(n) Time and Space Complexity 