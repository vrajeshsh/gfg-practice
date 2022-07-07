class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new1, new2 = "", ""
        for i in word1:
            new1+=i
        for j in word2:
            new2+=j
        return new1==new2