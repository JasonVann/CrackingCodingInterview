class Ex347(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        res = []
        for k1, v in dic.items():
            res.append((v, k1))
        res.sort(reverse=True)
        res2 = []
        #print res
        for i in range(k):
            (v, k1) = res[i]
            res2.append(k1)
        return res2
    '''
    public List<Integer> topKFrequent(int[] nums, int k) {
        List<Integer>[] bucket = new List[nums.length + 1];
        Map<Integer, Integer> frequencyMap = new HashMap<Integer, Integer>();

        for (int n : nums) {
            frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
        }

        for (int key : frequencyMap.keySet()) {
            int frequency = frequencyMap.get(key);
            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }

        List<Integer> res = new ArrayList<>();

        for (int pos = bucket.length - 1; pos >= 0 && res.size() < k; pos--) {
            if (bucket[pos] != null) {
                res.addAll(bucket[pos]);
            }
        }
        return res;
    }
    '''
    '''
    class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
            unordered_map<int, int> cnt;
            for (auto num : nums) cnt[num]++;
            for (auto kv : cnt) {
                pq.push({kv.second, kv.first});
                while (pq.size() > k) pq.pop();
            }
            vector<int> res;
            while (!pq.empty()) {
                res.push_back(pq.top().second);
                pq.pop();
            }
            return res;
        }
    };
    '''

