class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            isConsistent = True
            for j in i:
                if j not in allowed:
                    isConsistent = False
            if isConsistent:
                count+=1
        return count
                