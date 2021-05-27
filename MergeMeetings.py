# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def insert(intervals, newInterval):
        result = []
        merged = False
        n = len(intervals)

        # sort the new interval
        if newInterval.start > newInterval.end:
            newInterval.start, newInterval.end = newInterval.end, newInterval.start

        for i in range(n):
            if intervals[i].end >= newInterval.start:
                # found a gap, newInterval can be merged
                if i + 1 == n or newInterval.end >= intervals[i + 1].start:
                    # newInterval overlaps with 2 intervals. merge 3.
                    result.append(Interval(intervals[i].start, max(intervals[i + 1].end, newInterval.end)))
                else:
                    # newInterval overlaps with 1 interval. merge 2.
                    result.append(Interval(intervals[i].start, max(intervals[i].end, newInterval.end)))
            merged = True

        if not merged:
            # not merged with any interval.. new interval might be inserted at start
            if newInterval.end >= intervals.start:
                # first interval overlaps with new interval, merge them
                result[0] = Interval(intervals.start, max(intervals.end, newInterval.end))
            else:
                # Doesn't overlap with any
                result.insert(0, Interval(newInterval.start, intervals.end))
        return result