class Solution(object):
    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
        
        while 0 in vat:
            ind = vat.index(0)
            vat.pop(ind)
            bucket.pop(ind)
        n = len(vat)
        if n == 0:
            return 0 
        
        def cal_num(num1, num2):
            if num1 % num2 == 0:
                return num1 / num2
            else:
                return (num1 / num2) + 1
        
        resZero = 0
        for i in range(n):
            if bucket[i] == 0:
                bucket[i] = 1
                resZero += 1
        if n == 1:
            res = cal_num(vat[0], bucket[0])
            bucket[0] += 1
            diff = 1 - res + cal_num(vat[0], bucket[0])
            while diff < 0:
                res += diff
                bucket[0] += 1
                diff = 1 - res + cal_num(vat[0], bucket[0])
            return res
                
        nums = [cal_num(vat[i], bucket[i]) for i in range(n)]
        maxnum, minnum = max(nums), min(nums)
        if minnum == maxnum:
            return minnum + resZero
        
        nums2 = [[-cal_num(vat[i], bucket[i]), i] for i in range(n)]
        heapq.heapify(nums2)
        for delta in range(1, maxnum - minnum + 1):             
            elem = heapq.heappop(nums2)
            ind = elem[1]
            elem[0] = -cal_num(vat[ind], bucket[ind]+1)
            heapq.heappush(nums2, elem)
            if -nums2[0][0] <= -nums2[-1][0]:
                return -nums2[-1][0] + delta + resZero
            
"""
https://leetcode-cn.com/contest/season/2021-spring/submissions/166127501/
"""
