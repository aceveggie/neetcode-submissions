from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_counter = defaultdict(list)
        for each in strs:
            c_counter[tuple(sorted(each))].append(each)
        return list(c_counter.values())