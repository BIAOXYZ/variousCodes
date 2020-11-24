class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """

        dic = {}
        for ch in s:
            if dic.has_key(ch):
                dic[ch].append(ch)
            else:
                dic[ch] = [ch]
        l = dic.values()
        l.sort()
        
        res = []
        flag = 1
        while l:
            length = len(l)
            if flag == 1:
                for i in range(length):
                    res.append(l[i].pop())
            else:
                for i in range(length-1, -1, -1):
                    res.append(l[i].pop())
            while [] in l:
                l.remove([])
            flag = -flag
        return ''.join(res)
        
"""
https://leetcode-cn.com/submissions/detail/126040142/

323 / 323 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 13.6 MB

执行用时：52 ms, 在所有 Python 提交中击败了77.84%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了5.42%的用户
"""
