class Solution:
    def helper(self, nums:List[int], start:int, end:int) -> int:
        if start==end:
            return nums[start]
        
        prev = nums[start]
        curr = max(nums[start], nums[start+1])

        # 从start之后的第2个开始
        for i in range(start+2, end+1):
            temp = curr
            curr = max(prev + nums[i], curr)
            prev = temp
        
        return curr
    
    def rob(self, nums: List[int]) -> int: 
        n = len(nums)

        if n==1:
            return nums[0]

        res1 = self.helper(nums, 0, n-2)
        res2 = self.helper(nums, 1, n-1)

        return max(res1, res2)   