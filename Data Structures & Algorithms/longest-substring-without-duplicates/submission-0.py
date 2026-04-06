class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = set()

        max_len = 0

        n = len(s)

        left, right = 0, 0

        while right<n:
            while s[right] in record:
                record.remove(s[left])
                left += 1
            record.add(s[right])
            max_len = max(max_len, len(record))
            right += 1
        
        return max_len
            