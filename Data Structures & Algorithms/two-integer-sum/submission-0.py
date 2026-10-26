class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c_counter = {}
        for i, each in enumerate(nums):
            try:
                diff = target - each
                loc = c_counter[diff]
                return [loc, i]
            except:
                c_counter[each] = i