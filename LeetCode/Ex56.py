# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Ex56(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals
        intervals = sorted(intervals, key=lambda interval: interval.end) 
        intervals = sorted(intervals, key=lambda interval: interval.start)
        l = intervals[0].start
        r = intervals[-1].end
        res = []
        j = 0
        cur = None
        while j <= len(intervals) - 1:
            if cur == None:
                cur = intervals[j]
            if j == len(intervals) - 1:
                res.append(cur)
                break
            
            if cur.end < intervals[j+1].start:
                res.append(cur)
                cur = None
                j += 1
            else:
                cur.end = max(cur.end, intervals[j+1].end)
                j += 1
            
        return res
    '''
    public List<Interval> merge(List<Interval> intervals) {
        if (intervals.size() <= 1)
            return intervals;
        
        // Sort by ascending starting point using an anonymous Comparator
        Collections.sort(intervals, new Comparator<Interval>() {
            @Override
            public int compare(Interval i1, Interval i2) {
                return Integer.compare(i1.start, i2.start);
            }
        });
        
        List<Interval> result = new LinkedList<Interval>();
        int start = intervals.get(0).start;
        int end = intervals.get(0).end;
        
        for (Interval interval : intervals) {
            if (interval.start <= end) // Overlapping intervals, move the end if needed
                end = Math.max(end, interval.end);
            else {                     // Disjoint intervals, add the previous one and reset bounds
                result.add(new Interval(start, end));
                start = interval.start;
                end = interval.end;
            }
        }
        
        // Add the last interval
        result.add(new Interval(start, end));
        return result;
    }
    '''

