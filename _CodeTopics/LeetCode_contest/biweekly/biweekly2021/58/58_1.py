class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        tmp = []
        flag = 0
        for ch in s:
            if not tmp:
                tmp.append(ch)
                flag = 1
            else:
                if tmp[-1] != ch:
                    tmp.append(ch)
                    flag = 1
                else:
                    if flag >= 2:
                        continue
                    else:
                        tmp.append(ch)
                        flag += 1
        return ''.join(tmp)
    
"""
https://leetcode-cn.com/submissions/detail/204391681/

306 / 306 个通过测试用例
状态：通过
执行用时: 360 ms
内存消耗: 15.8 MB
"""
