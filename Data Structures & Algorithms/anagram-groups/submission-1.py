from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c_dict = defaultdict(list)
        for s in strs:
            c_dict[tuple(sorted(s))].append(s)
        return list(c_dict.values())