class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        intervals.sort(key = lambda x: x[1])

        keep = 1

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start>=prev_end:
                keep += 1
                prev_end = end

        return n-keep   