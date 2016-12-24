class Ex57(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        for i in range(len(intervals)):
            if i == 0 and intervals[0].start >= newInterval.start:
                intervals.insert(0, newInterval)
                break
            if intervals[i].start <= newInterval.start:
                if intervals[i].end >= newInterval.start:
                    intervals.insert(i+1, newInterval)
                    break
            if i <= len(intervals) - 1 and intervals[i].end <= newInterval.start:
                if i == len(intervals) - 1:
                    intervals.insert(i+1, newInterval)
                elif intervals[i+1].start >= newInterval.start:
                    intervals.insert(i+1, newInterval)
                    break
                
        return self.merge(intervals)
        
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
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
                j += 2
            
        return res
    '''
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new LinkedList<>();
        int i = 0;
        // add all the intervals ending before newInterval starts
        while (i < intervals.size() && intervals.get(i).end < newInterval.start)
            result.add(intervals.get(i++));
        // merge all overlapping intervals to one considering newInterval
        while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
            newInterval = new Interval( // we could mutate newInterval here also
                    Math.min(newInterval.start, intervals.get(i).start),
                    Math.max(newInterval.end, intervals.get(i).end));
            i++;
        }
        result.add(newInterval); // add the union of intervals we got
        // add all the rest
        while (i < intervals.size()) result.add(intervals.get(i++)); 
        return result;
    }
    '''
    '''    
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right
    def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
        parts = merge, left, right = [], [], []
        for i in intervals:
            parts[(i.end < s) - (i.start > e)].append(i)
        if merge:
            s = min(s, merge[0].start)
            e = max(e, merge[-1].end)
        return left + [Interval(s, e)] + right
    '''
    '''
    class Solution {
    public:
        vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
            auto compare = [] (const Interval &intv1, const Interval &intv2)
                              { return intv1.end < intv2.start; };
            auto range = equal_range(intervals.begin(), intervals.end(), newInterval, compare);
            auto itr1 = range.first, itr2 = range.second;
            if (itr1 == itr2) {
                intervals.insert(itr1, newInterval);
            } else {
                itr2--;
                itr2->start = min(newInterval.start, itr1->start);
                itr2->end = max(newInterval.end, itr2->end);
                intervals.erase(itr1, itr2);
            }
            return intervals;
        }
    };
    '''

