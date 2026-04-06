class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        currSum = 0
        startIdx = 0

        n = len(gas)

        for i in range(n):
            currSum = currSum + gas[i] - cost[i]
            if currSum<0:
                startIdx = i +1
                currSum = 0


        # check
        currSum = 0
        for i in range(n):
            idx = (startIdx + i) % n
            currSum = currSum + gas[idx] - cost[idx]
            if currSum<0:
                return -1

        return startIdx          