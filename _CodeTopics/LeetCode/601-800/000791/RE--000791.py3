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
                if dic[ch] < dic[res[i]]:
                    res.insert(i, ch)
                    inserted = True
                    break
            if not inserted:
                res.append(ch)
        return ''.join(res)
        
"""
https://leetcode.cn/submissions/detail/381559448/

3 / 39 个通过测试用例
状态：执行出错

执行出错信息：
KeyError: u'w'
    if dic[ch] < dic[res[i]]:
Line 17 in customSortString (Solution.py)
    ret = Solution().customSortString(param_1, param_2)
Line 50 in _driver (Solution.py)
    _driver()
Line 60 in <module> (Solution.py)
最后执行的输入：
"exv"
"xwvee"
"""
