class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 1.0
        negative = n<0
        total = 1

        n = abs(n)
        for _ in range(n):
            total = total * x
        
        return 1 / total if negative else total