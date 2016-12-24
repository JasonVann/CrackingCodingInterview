class Ex47(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        res = []
        nums.sort()
        n = len(nums)
        max_n = nums[-1]
        temp = set([str(nums[0])])
        for i in range(1, n):
            num = str(nums[i])
            new_temp = set()
            for block in temp:
                block = list(block)
                j = 0
                has_add = False
                while j <= len(block):
                    
                    block2 = ''.join(block[:j]) + str(num) + ''.join(block[j:])
                    #print 77, block, block2, temp
                    #block2 = str(block2)
                    #print 79, block2
                    if block2 not in temp:
                        new_temp.add(block2)
                    if i == n-1:
                        #if block2 not in res:
                        res.append(block2)
                    '''
                    if j < len(block) and num == block[j]:
                        print 80, block, num
                        while j < len(block) and num == block[j]:
                            j += 1
                    else:
                    '''
                    j += 1
            temp = new_temp
         
        res2 = []
                
        for r in res:
            if r not in res2:
                res2.append(r)
        print 93, len(res), len(res2)
        
ex47 = Ex47()
nums = [1,2,1]
nums = [1,1,0,0,1,-1,-1,1]
#nums = [1,1,1,2,3,4,2]

print 47, ex47.permuteUnique(nums)

