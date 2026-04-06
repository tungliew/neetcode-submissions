class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # len(piles) is even
        # sum(piles) is odd

        # alice starting first
        # beginner/end of the row
        # the most stones wins

        alice = 0

        n = len(piles)

        total = sum(piles)

        for i in range(n//2):
            alice = alice + max(piles[i], piles[n-i-1])

        
        return alice>(total-alice)