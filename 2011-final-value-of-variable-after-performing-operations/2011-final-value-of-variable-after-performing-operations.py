class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0
        for i in operations:
            if i == "--X" or i == "X--":
                num-=1
            elif i == "X++" or i == "++X":
                num+=1
        return num