class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        lp = 0
        rp = len(s)-1
        while lp < rp:
            while lp <rp and s[lp].isalnum() is False:
                lp += 1
            while lp < rp and s[rp].isalnum() is False:
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True