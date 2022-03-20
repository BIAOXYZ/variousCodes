class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        
        n = len(directions)
        dic = {'L':[], 'R':[], 'S':[]}
        for i, ch in enumerate(directions):
            dic[ch].append(i)
        
        d = list(directions)
        res = 0
        for i in range(n):
            if d[i] == 'S': continue
            elif d[i] == 'L':
                if (dic['S'] and i > dic['S'][0]) or (dic['R'] and i > dic['R'][0]):
                    res += 1
            else:
                # 这里低级失误了，应该是 -1，不是 0
                if (dic['S'] and i < dic['S'][-1]) or (dic['L'] and i < dic['L'][-1]):
                    res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/286207616/

119 / 119 个通过测试用例
状态：通过
执行用时: 468 ms
内存消耗: 21.3 MB
"""
