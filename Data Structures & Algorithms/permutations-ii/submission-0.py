class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # contain duplicates
        nums.sort()

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
                
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                subset.append(nums[i])

                backtrack()

                subset.pop()
                used[i] = False
        
        backtrack()

        return result
