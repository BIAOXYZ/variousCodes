class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        
        dic1, dic2 = {}, {}
        for i, pair in enumerate(adjacentPairs):
            dic1[pair[0]] = dic1.setdefault(pair[0], 0) + 1
            dic1[pair[1]] = dic1.setdefault(pair[1], 0) + 1
            if dic2.has_key(pair[0]):
                dic2[pair[0]].append(i)
            else:
                dic2[pair[0]] = [i]
            if dic2.has_key(pair[1]):
                dic2[pair[1]].append(i)
            else:
                dic2[pair[1]] = [i]
        
        res = []
        for k, v in dic1.items():
            if v == 1:
                res.append(k)
                break
        
        resFast = set(res)
        currLen = 1
        while currLen < len(adjacentPairs) + 1:
            currElem = res[-1]
            for ind in dic2[currElem]:
                pair = adjacentPairs[ind]
                if pair[0] not in resFast:
                    res.append(pair[0])
                    resFast.add(pair[0])
                    break
                if pair[1] not in resFast:
                    res.append(pair[1])
                    resFast.add(pair[1])
                    break
            currLen += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/142480473/

46 / 46 个通过测试用例
状态：通过
执行用时: 640 ms
内存消耗: 68.8 MB
"""
