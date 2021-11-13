class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        """
        前面提交会错还是因为假定python字典的key是有序的（被某些帖子误导了!）
        """
        
        # 0:0 是个 dummy 的 k-v pair，方便后面的二分查找操作。
        dic = {0:0}
        for price, beauty in items:
            if price in dic:
                dic[price] = max(dic[price], beauty)
            else:
                dic[price] = beauty
        
        keys = dic.keys()
        keys.sort()
        vals = [0]
        for i in range(1, len(keys)):
            k = keys[i]
            vals.append(max(vals[-1], dic[k]))
        ##print keys, vals
        
        res = []
        for q in queries:
            ind = bisect.bisect_right(keys, q)
            res.append(vals[ind-1])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/238385295/

35 / 35 个通过测试用例
状态：通过
执行用时: 208 ms
内存消耗: 55.7 MB
"""
