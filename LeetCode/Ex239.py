class Ex239(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if k == 0:
            return []
        window = deque()
        for i in range(k):
            window.append(nums[i])
        max_e = max(window)
        res = [max_e]
        for i in range(k, len(nums)):
            cur = nums[i]
            a = window.popleft()
            window.append(cur)
            if a == max_e and max_e > cur:
                max_e = max(window)  
            else:
                max_e = max(max_e, cur)
                            
            res.append(max_e)
        return res
        
    def maxSlidingWindow0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        if k == 0:
            return []
        window = nums[:k]
        res = [max(window)]
        for i in range(k, len(nums)):
            cur = nums[i]
            window.pop(0)
            window.append(cur)
            res.append(max(window))
        return res
    '''
    public static int[] slidingWindowMax(final int[] in, final int w) {
        final int[] max_left = new int[in.length];
        final int[] max_right = new int[in.length];

        max_left[0] = in[0];
        max_right[in.length - 1] = in[in.length - 1];

        for (int i = 1; i < in.length; i++) {
            max_left[i] = (i % w == 0) ? in[i] : Math.max(max_left[i - 1], in[i]);

            final int j = in.length - i - 1;
            max_right[j] = (j % w == 0) ? in[j] : Math.max(max_right[j + 1], in[j]);
        }

        final int[] sliding_max = new int[in.length - w + 1];
        for (int i = 0, j = 0; i + w <= in.length; i++) {
            sliding_max[j++] = Math.max(max_right[i], max_left[i + w - 1]);
        }

        return sliding_max;
    }
    '''
    '''
    public int[] maxSlidingWindow(int[] a, int k) {     
        if (a == null || k <= 0) {
            return new int[0];
        }
        int n = a.length;
        int[] r = new int[n-k+1];
        int ri = 0;
        // store index
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < a.length; i++) {
            // remove numbers out of range k
            while (!q.isEmpty() && q.peek() < i - k + 1) {
                q.poll();
            }
            // remove smaller numbers in k range as they are useless
            while (!q.isEmpty() && a[q.peekLast()] < a[i]) {
                q.pollLast();
            }
            // q contains index... r contains content
            q.offer(i);
            if (i >= k - 1) {
                r[ri++] = a[q.peek()];
            }
        }
        return r;
    }
    '''
    '''
    from collections import deque
    class Solution(object):
        def maxSlidingWindow(self, nums, k):
            if not nums: return []
            res = []
            dq = deque()  # store index
            for i in xrange(len(nums)):
                if dq and dq[0]<i-k+1:  # out of the window
                    dq.popleft()
                while dq and nums[dq[-1]]<nums[i]:  # remove impossible candidate
                    dq.pop()
                dq.append(i)
                if i>k-2:
                    res.append(nums[dq[0]])
            return res
    '''
    '''
    public int[] maxSlidingWindow(int[] a, int k) {
        if (a == null || a.length == 0 || k == 0) {
            return new int [0];
        }
        int [] result = new int [a.length - k + 1];
        int ri = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < k - 1; i++) {
            pq.add(a[i]);
        }
        
        for (int i = k - 1; i < a.length; i++) {
            pq.add(a[i]);
            result[ri++] = pq.peek();
            pq.remove(a[i - k + 1]);
        }
        return result;
    }
    '''

