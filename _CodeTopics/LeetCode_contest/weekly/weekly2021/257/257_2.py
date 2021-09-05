class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        
        n = len(properties)
        dic = {}
        for p in properties:
            if dic.has_key(p[0]):
                dic[p[0]] = max(dic[p[0]], p[1])
            else:
                dic[p[0]] = p[1]
        ##print dic
        
        keys = dic.keys()
        keys.sort(reverse=True)
        dic2 = {}
        m = len(keys)
        for i in range(m):
            currKey, prevKey = keys[i], keys[i-1]
            if i == 0:
                dic2[currKey] = dic[currKey]
            else:
                dic2[currKey] = max(dic[prevKey], dic2[prevKey])
        ##print dic2
        
        maxKey = max(keys)
        properties.sort()
        res = 0
        for i in range(n-1):
            p = properties[i]
            if p[0] == maxKey:
                return res
            if p[1] < dic2[p[0]]:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/215334740/

44 / 44 个通过测试用例
状态：通过
执行用时: 760 ms
内存消耗: 59.6 MB
"""
