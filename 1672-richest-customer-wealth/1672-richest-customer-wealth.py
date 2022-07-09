class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi= 0
        for i in accounts:
            ssum = 0
            for j in i:
                ssum+=j
            if ssum>maxi:
                maxi = ssum
        return maxi
                