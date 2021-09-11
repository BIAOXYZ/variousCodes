class Solution(object):
    def minimumSwitchingTimes(self, source, target):
        """
        :type source: List[List[int]]
        :type target: List[List[int]]
        :rtype: int
        """
        
        def to_dict_2d(lis):
            dic = {}
            for elem in lis:
                for e in elem:
                    dic[e] = dic.setdefault(e, 0) + 1
            return dic
        
        dic1 = to_dict_2d(source)
        dic2 = to_dict_2d(target)
        print dic1, dic2

        res = 0
        for k, v in dic2.items():
            v1 = dic1.get(k, 0)
            if v > v1:
                res += v - v1
        return res
    
"""
https://leetcode-cn.com/contest/season/2021-fall/submissions/217895716/
"""
