class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        self.counter1 = {}
        self.counter2 = {}
        for each in s:
            try:
                self.counter1[each] += 1
            except:
                self.counter1[each] = 1
        for each in t:
            try:
                self.counter2[each] += 1
            except:
                self.counter2[each] = 1
        for k,v in self.counter1.items():
            try:
                if self.counter1[k] != self.counter2[k]:
                    return False
            except:
                return False
        return True
        