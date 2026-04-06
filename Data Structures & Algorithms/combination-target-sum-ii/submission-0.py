class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        subset = []

        def backtrack(start, total):
            if total==target:
                result.append(subset[:])
            
            if total>target:
                return 
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1, candidates[i]+total)
                subset.pop()

        backtrack(0, 0)

        return result