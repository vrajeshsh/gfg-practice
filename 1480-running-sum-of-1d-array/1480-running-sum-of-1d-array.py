class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new, new_arr = 0, []
        for i in nums:
            new+=i
            new_arr.append(new)
        return new_arr