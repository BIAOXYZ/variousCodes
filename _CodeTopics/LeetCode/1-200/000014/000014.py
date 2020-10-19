class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if strs == [] or '' in strs:
            return ''
        
        res = ''
        while '' not in strs:
            currstr = strs[0][0]
            strs[0] = strs[0][1:]
            for i in range(1,len(strs)):
                if strs[i][0] != currstr:
                    return res
                else:
                    strs[i] = strs[i][1:]
            res = res + currstr
        return res
        
"""
https://leetcode-cn.com/submissions/detail/79069633/

118 / 118 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.9 MB
"""
