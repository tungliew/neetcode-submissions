class Solution:
    def isHappy(self, n: int) -> bool:
        # n positive integer
        curr = n
        record = set()

        while curr!=1 and (curr not in record):
            # calculate sum of squares of its digits
            record.add(curr)
            total = 0
            while curr:
                total = total +  (curr%10)**2
                curr = curr // 10
            curr = total
        
        return True if curr==1 else False
