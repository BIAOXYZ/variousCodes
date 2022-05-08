class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        n = len(num)
        flag = 1
        curr = num[0]
        i = 1
        res = -1
        while i < n:
            if num[i] == curr:
                flag += 1
                if flag == 3:
                    res = max(res, int(curr))
            else:
                curr = num[i]
                # 日了，竟然是这里。。。
                # flag == 1
                flag = 1
            i += 1
        return "" if res == -1 else str(res)*3
    
"""
https://leetcode-cn.com/submissions/detail/310667811/

140 / 140 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB
"""
