class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """    
        
        length = len(arr)
        if length == k:
            return 0
        
        numdic = dict()
        for i in range(length):
            if numdic.has_key(arr[i]):
                numdic[arr[i]] += 1
            else:
                numdic[arr[i]] = 1
        
        # valuelist = numdic.values().sort()
        # 这里用上面这句返回的是None
        valuelist = sorted(numdic.values())
        valuetypes = len(valuelist)
        
        for i in range(valuetypes):
            k -= valuelist[i]
            if k >= 0:
                continue
            else:
                return valuetypes - i
            
"""
https://leetcode-cn.com/submissions/detail/78802539/

43 / 43 个通过测试用例
	状态：通过
执行用时：112 ms
内存消耗：29.4 MB
"""
