class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        res = set()
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    num = [digits[i], digits[j], digits[k]]
                    inds = [[0, 1, 2],[0, 2, 1],[1, 0, 2],[1, 2, 0],[2, 0, 1],[2, 1, 0]]
                    for ind in inds:
                        tmp = num[ind[0]] * 100 + num[ind[1]] * 10 + num[ind[2]]
                        if tmp % 2 == 0 and tmp >= 100:
                            res.add(tmp)
        return sorted(list(res))
    
"""
https://leetcode-cn.com/submissions/detail/245373433/

79 / 79 个通过测试用例
状态：通过
执行用时: 6336 ms
内存消耗: 13 MB
"""
