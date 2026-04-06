class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        n = len(nums)

        used = [False] * n

        def backtrack():
            if len(subset)==n:
                result.append(subset[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                
                used[i] = True
                subset.append(nums[i])
                
                backtrack()
                
                subset.pop()
                used[i] = False
        
        backtrack()
        
        return result
        