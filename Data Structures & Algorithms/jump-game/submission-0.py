class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i, step in enumerate(nums):
            if i>max_reach:
                return False
            max_reach = max(max_reach, i+step)
            if max_reach >= n-1:
                return True
        
        return False