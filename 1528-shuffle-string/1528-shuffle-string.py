class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new =""
        for i in range(len(indices)):
            new +=s[indices.index(i)]
        return new
            