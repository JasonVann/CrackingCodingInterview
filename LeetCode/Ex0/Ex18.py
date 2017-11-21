class Ex18(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        dic = {}
        res = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
        #dic2 = dic.copy()
        #print dic2
        for i in range(len(nums) - 3):
            #dic2 = dic.copy()
            first = nums[i]
            #dic2[first] = dic2[first] - 1
            for j in range(i+1, len(nums) - 2):
                second = nums[j] 
                
                for k in range(j+1, len(nums) - 1):
                    
                    third = nums[k]
                    
                    fourth = target - first - second - third
                    #print 41, first, second, third, fourth #dic2[fourth]
                    #print 42, i, j, k, dic2
                    if (fourth) in dic:
                        dic2 = dic.copy()
                        dic2[fourth] = dic2[fourth] - 1
                        dic2[first] =dic2[first] - 1
                        dic2[second] = dic2[second] - 1
                        dic2[third] = dic2[third] - 1
                        if dic2[first] <0 or dic2[second] < 0 or dic2[third] < 0 or dic2[fourth] < 0:
                            continue
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        res[tuple(temp)] = 1
                        #dic2 = dic.copy()
        #print res
        res_l = []
        for k in res:
            res_l.append(list(k))
        return res_l
        
    def fourSum0(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        dic = {}
        res = {}
        for n in nums:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1
        dic2 = dic.copy()
        #print dic2
        for i in range(len(nums) - 3):
            #dic2 = dic.copy()
            first = nums[i]
            dic2[first] = dic2[first] - 1
            for j in range(i+1, len(nums) - 2):
                second = nums[j] 
                if dic2[second] <= 0:
                    if j == len(nums) - 3:
                        dic2[first] = dic2[first] + 1
                    #print 26, dic2
                    continue
                dic2[second] = dic2[second] - 1
                #print 31, first, second, dic2
                                    
                for k in range(j+1, len(nums) - 1):
                    
                    third = nums[k]
                    
                    if dic2[third] <= 0:
                        if j == len(nums) - 3:
                            dic2[first] = dic2[first] + 1
                        if k == len(nums) - 2:
                            dic2[second] = dic2[second] + 1
                        #print 38, dic2
                        continue
                    dic2[third] = dic2[third] - 1
                    fourth = target - first - second - third
                    #print 41, first, second, third, fourth #dic2[fourth]
                    #print 42, i, j, k, dic2
                    if (fourth) in dic:
                        #print 41, fourth, dic2[fourth]
                        if dic2[fourth] <= 0:
                            if j == len(nums) - 3:
                                dic2[first] = dic2[first] + 1
                            if k == len(nums) - 2:
                                dic2[second] = dic2[second] + 1
                            dic2[third] = dic2[third] + 1
                            #print 49, dic2
                            continue
                        #if ((fourth == nums[i] or fourth == nums[j]) and nums[i] != nums[j] and dic[fourth] > 1) or (fourth != nums[i] and fourth != nums[j]) or (fourth == nums[i] and fourth == nums[j] and dic[fourth] > 2):
                            #print 1221, nums[i], nums[j], fourth, dic[fourth]
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        res[tuple(temp)] = 1
                        
                        if j == len(nums) - 3:
                            dic2[first] = dic2[first] + 1
                        if k == len(nums) - 2:
                            dic2[second] = dic2[second] + 1
                        dic2[third] = dic2[third] + 1
                        #dic2[fourth] = dic2[fourth] + 1
                        #print 60, first, second, third, dic2
                    else:
                        if j == len(nums) - 3:
                            dic2[first] = dic2[first] + 1
                        if k == len(nums) - 2:
                            dic2[second] = dic2[second] + 1
                        dic2[third] = dic2[third] + 1
        #print res
        res_l = []
        for k in res:
            res_l.append(list(k))
        return res_l
     
import time
start_time = time.time()
ex18 = Ex18()
nums = [1, 0, -1, 0, -2, 2]
target = 0
#nums = [-494,-474,-425,-424,-391,-371,-365,-351,-345,-304,-292,-289,-283,-256,-236,-236,-236,-226,-225,-223,-217,-185,-174,-163,-157,-148,-145,-130,-103,-84,-71,-67,-55,-16,-13,-11,1,19,28,28,43,48,49,53,78,79,91,99,115,122,132,154,176,180,185,185,206,207,272,274,316,321,327,327,346,380,386,391,400,404,424,432,440,463,465,466,475,486,492]

#target = -1211
print 18, ex18.fourSum(nums, target)
print time.time() - start_time
