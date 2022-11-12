class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        dic = {order[i]:i for i in range(len(order))}
        res = []
        for ch in s:
            if not res or ch not in dic:
                res.append(ch)
                continue
            inserted = False
            for i in range(len(res)):
                if res[i] not in dic:
                    continue
                if dic[ch] < dic[res[i]]:
                    res.insert(i, ch)
                    inserted = True
                    break
            if not inserted:
                res.append(ch)
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/381559581/

执行用时：
24 ms
, 在所有 Python 提交中击败了
17.65%
的用户
内存消耗：
13.3 MB
, 在所有 Python 提交中击败了
5.88%
的用户
通过测试用例：
39 / 39
"""
