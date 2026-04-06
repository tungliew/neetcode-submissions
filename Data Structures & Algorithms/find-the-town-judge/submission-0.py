class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        source = [[] for _ in range(n+1)]
        dest = [[] for _ in range(n+1)]

        for edge in trust:
            start, end = edge[0], edge[1]
            source[start].append(end)
            dest[end].append(source)
        
        for i in range(1, n+1):
            if len(source[i])==0 and len(dest[i])==n-1:
                return i
        
        return -1
            