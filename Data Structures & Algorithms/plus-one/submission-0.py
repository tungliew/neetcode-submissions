class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []

        n = len(digits)

        carry = 1

        for i in range(n-1, -1, -1):
            total = digits[i] + carry
            result.append(total % 10)
            carry = total // 10

        if carry!=0:
            result.append(carry)

        return result[::-1]