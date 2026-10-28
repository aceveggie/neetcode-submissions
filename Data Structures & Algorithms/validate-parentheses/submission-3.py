class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        l = []
        c_dict = {
            '(':')',
            '[': ']',
            '{':'}'
        }
        c_list = []
        for each in s:
            if each in ['(','{','[']:
                c_list.append(c_dict[each])
            else:
                try:
                    found = c_list.pop()
                    if each != found:
                        return False
                except:
                    return False
        if len(c_list) > 0:
            return False
        return True