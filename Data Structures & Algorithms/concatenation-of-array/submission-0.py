class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)
        j = 0
        for i in range(0, len(nums) * 2):
            if i < len(nums):
                res[i] = nums[i]
                j += 1
            else:
                res[i] = nums[i - j]
        return res