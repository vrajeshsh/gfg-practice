class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0
        for ch in s:
            cnt+=1 if ch=="L" else -1
            if cnt==0:
                res+=1
        return res