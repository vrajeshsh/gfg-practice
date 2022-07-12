class Solution:
    def countAsterisks(self, s: str) -> int:
        count, str_cnt = 0, 0
        for ch in s:
            if ch=="|":
                count+=1
                
            elif ch=="*" and count%2==0:
                str_cnt+=1
        return str_cnt