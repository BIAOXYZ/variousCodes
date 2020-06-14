class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """    
        
        length = len(arr)
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
https://leetcode-cn.com/contest/weekly-contest-193/submissions/detail/78798394/

41 / 43 个通过测试用例
	状态：解答错误
  

输入： [1]
       1
输出： null
预期： 0
"""
