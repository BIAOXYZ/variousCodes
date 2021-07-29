class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """

        i, level = 1, 1
        lis = [[0]]
        currLevel = collections.deque([])
        while i <= label:
            if i > 2**level - 1:
                lis.append(list(currLevel))
                currLevel = collections.deque([])
                level += 1
            if level % 2 == 1:
                currLevel.append(i)
                i += 1
            else:
                currLevel.appendleft(i)
                i += 1
        
        index = 0
        if level % 2 == 1:
            index = len(currLevel) - 1
        else:
            index = 2**(level-1) - len(currLevel)
        
        res = [label]
        level -= 1
        while level > 0:
            nextInd = index / 2
            nextElem = lis[level][nextInd]
            res.append(nextElem)
            level -= 1
            index = nextInd
        res.reverse()
        return res
        
"""
https://leetcode-cn.com/submissions/detail/201193505/

44 / 44 个通过测试用例
状态：通过
执行用时: 832 ms
内存消耗: 45.6 MB

执行用时：832 ms, 在所有 Python 提交中击败了10.00%的用户
内存消耗：45.6 MB, 在所有 Python 提交中击败了10.00%的用户
"""
