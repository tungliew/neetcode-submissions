class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(start):
            if len(subset)==k:
                result.append(subset[:])
            
            for i in range(start, n+1):
                subset.append(i)
                backtrack(i+1)
                subset.pop()
        
        backtrack(1)

        return result