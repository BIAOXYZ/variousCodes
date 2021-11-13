class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
        # 0:0 是个 dummy 的 k-v pair，方便后面的二分查找操作。
        dic = {0:0}
        for price, beauty in items:
            if price in dic:
                dic[price] = max(dic[price], beauty)
            else:
                dic[price] = beauty
        
        keys = dic.keys()
        dic2 = {0:0}
        currMax = 0
        for i in range(1, len(keys)):
            k = keys[i]
            currMax = max(currMax, dic[k])
            dic2[k] = currMax
        
        res = []
        for q in queries:
            ind = bisect.bisect_right(keys, q)
            ##print keys[ind-1]
            res.append(dic2[keys[ind-1]])
        return res
    
"""
https://leetcode-cn.com/submissions/detail/238383521/

15 / 35 个通过测试用例
状态：解答错误

输入：
[[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]
输出：
[962,962,962,962,962,962,962,962,962,962,962,962,0,0,962,962,962,962,962]
预期：
[962,962,962,962,746,962,962,962,946,962,962,919,746,746,962,962,962,919,962]
"""
