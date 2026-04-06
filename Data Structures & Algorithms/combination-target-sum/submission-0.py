class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start, total):
            if total==target:
                result.append(subset[:])
            
            if total>target:
                return
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, total+nums[i])
                subset.pop()
        
        backtrack(0, 0)

        return result
        