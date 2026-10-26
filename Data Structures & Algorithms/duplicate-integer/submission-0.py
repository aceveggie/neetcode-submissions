class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.counter = {}
        for each in nums:
            try:
                self.counter[each] += 1
                return True
            except:
                self.counter[each] = 1
        return False
