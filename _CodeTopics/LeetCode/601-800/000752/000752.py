class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        # 应该就是带剪枝的 BFS 就可以了。

        visited = set(deadends)
        
        def get_next_eigth_strings(s):
            if s in visited:
                return []
            visited.add(s)
            res = []
            for i in range(len(s)):
                newCh1, newCh2 = (int(s[i])-1) % 10, (int(s[i])+1) % 10
                s1 = s[:i] + str(newCh1) + s[i+1:]
                s2 = s[:i] + str(newCh2) + s[i+1:]
                if s1 not in visited:
                    res.append(s1)
                if s2 not in visited:
                    res.append(s2)
            return res
        
        stk = ["0000"]
        depth = 0
        while stk:
            nextLevel = []
            for i in range(len(stk)-1, -1, -1):
                elem = stk.pop()
                if elem == target:
                    return depth
                nextLevel.extend(get_next_eigth_strings(elem))
            stk = nextLevel[:]
            depth += 1
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/189547122/

48 / 48 个通过测试用例
状态：通过
执行用时: 856 ms
内存消耗: 14.6 MB

执行用时：856 ms, 在所有 Python 提交中击败了40.82%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了5.30%的用户
"""
