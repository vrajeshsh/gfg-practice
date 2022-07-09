class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for j in range(n):
            i = j
            while i<len(nums):
                ans.append(nums[i])
                i+=n
        return ans
            
        