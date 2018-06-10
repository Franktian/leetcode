# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def mergeIntervals(intervals):
    intervals.sort(key = lambda x:x.start)
    
    
    merged = []
    for interval in intervals:
        if not merged or interval.start > merged[-1].end:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)

    return merged

if __name__ == '__main__':
    a = Interval(5,6)
    b = Interval(1,4)
    
    ins = [a, b]
    
    ans = mergeIntervals(ins)
    
    adj = (1,2), (3,4)
    
    for x, y in adj:
        print "{}, {}".format(x, y)
