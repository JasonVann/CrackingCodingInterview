class Ex134(object):       
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        from collections import deque
        if sum(gas) < sum(cost):
            return -1
            
        Diff = []
        path = deque()
        max_i, max_v = 0, 0
        for i in range(len(gas)):
            temp = gas[i] - cost[i]
            Diff.append(temp)
            if temp > max_v:
                max_v = temp
                max_i = i
        #path = []
        #cur = max(Diff)
        #cur = Diff.index(cur)
        cur = max_i
        #print 71, gas, Diff, cur
                
        path.append(cur)
        path_set = set(path)
        while len(path) < len(gas):
            p_l = path[0]
            p_r = path[-1]
            #print 79, p_l, p_r, Diff
            if p_l == 0 and len(gas) - 1 in path_set:
                p1 = 1                
                #earliest += 1
            elif p_l == 0 and len(gas) - 1 not in path_set:
                p1 = len(gas) - 1
            else:
                p1 = p_l - 1
                #earliest += 1
                
            if p_r == len(gas) - 1 and 0 in path_set:
                p2 = p_r - 1
            elif p_r == len(gas) - 1 and 0 not in path_set:
                p2 = 0
            else:
                p2 = p_r + 1
                
            #print 84, p_l, p_r, (p1, p2), Diff
            
            if Diff[p1] > Diff[p2]:
                path.appendleft(p1)
                path_set.add(p1)
            else:              
                path.append(p2)
                path_set.add(p2)
            '''
            elif p_l-1 not in path:
                has_add = True
                path.append(p_l-1)
            elif p_r + 1 not in path:                
                path.append(p_r+1)
            else:
                return -1
            '''
            #print 95, path
            
        return path[0]
        
    def canCompleteCircuit_list(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
            
        Diff = []
        path = []
        max_i, max_v = 0, 0
        for i in range(len(gas)):
            temp = gas[i] - cost[i]
            Diff.append(temp)
            if temp > max_v:
                max_v = temp
                max_i = i
        path = []
        #cur = max(Diff)
        #cur = Diff.index(cur)
        cur = max_i
        #print 71, gas, Diff, cur
                
        path.append(cur)
        
        while len(path) < len(gas):
            p_l = path[0]
            p_r = path[-1]
            #print 79, p_l, p_r, Diff
            if p_l == 0 and len(gas) - 1 in path:
                p1 = 1                
                #earliest += 1
            elif p_l == 0 and len(gas) - 1 not in path:
                p1 = len(gas) - 1
            else:
                p1 = p_l - 1
                #earliest += 1
                
            if p_r == len(gas) - 1 and 0 in path:
                p2 = p_r - 1
            elif p_r == len(gas) - 1 and 0 not in path:
                p2 = 0
            else:
                p2 = p_r + 1
                
            #print 84, p_l, p_r, (p1, p2), Diff
            
            if Diff[p1] > Diff[p2]:
                path.insert(0, p1)
            else:              
                path.append(p2)
            '''
            elif p_l-1 not in path:
                has_add = True
                path.append(p_l-1)
            elif p_r + 1 not in path:                
                path.append(p_r+1)
            else:
                return -1
            '''
            #print 95, path
            
        return path[0]
    '''
    class Solution {
    public:
        int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
            int start(0),total(0),tank(0);
            //if car fails at 'start', record the next station
            for(int i=0;i<gas.size();i++) 
                if((tank=tank+gas[i]-cost[i])<0) 
                {start=i+1;total+=tank;tank=0;}
            return (total+tank<0)? -1:start;
        }
    };
    '''
    
ex134 = Ex134()
gas = [1,2,3,3]
cost = [2,1,5,1]
gas = [2,4]
cost = [3,4]
gas = [2,0,1,2,3,4,0]
cost = [0,1,0,0,0,0,11]
gas = [6,1,4,3,5]
cost = [3,8,2,4,2]
print 134, ex134.canCompleteCircuit(gas, cost)

