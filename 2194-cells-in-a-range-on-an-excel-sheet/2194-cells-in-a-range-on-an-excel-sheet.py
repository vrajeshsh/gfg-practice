class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        new = []
        
        for j in range(ord(s[0]), ord(s[3])+1):
            for i in range(int(s[1]), int(s[4])+1):
                new.append(chr(j)+str(i))
        return new
            