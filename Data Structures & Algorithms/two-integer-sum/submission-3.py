
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        complement_map: Dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in complement_map:
                return [complement_map[diff], i]
            complement_map[num] = i
        return []