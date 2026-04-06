class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        record = {}

        max_len = 0

        n = len(s)

        left, right = 0, 0

        max_freq = 0

        while right<n:
            record[s[right]] = record.get(s[right], 0) + 1

            max_freq = max(max_freq, record[s[right]])

            if (right-left+1) - max_freq > k:
                record[s[left]] -= 1
                left += 1

            max_len = max(max_len, right-left+1)

            right += 1

        return max_len      