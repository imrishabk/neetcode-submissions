class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        trackerSet = set(nums)
        if len(trackerSet) != len(nums):
            return True
        return False