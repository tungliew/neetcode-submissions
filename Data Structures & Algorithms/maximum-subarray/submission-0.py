class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        currSum = 0
        for num in nums:
            currSum += num
            result = max(result, currSum)
            if currSum<0:
                currSum = 0
            
        return result