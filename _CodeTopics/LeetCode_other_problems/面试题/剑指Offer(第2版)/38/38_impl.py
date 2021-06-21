class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 典型的回溯算法，类似 `LC47 全排列 II`：也就是可以有重复元素的全排列。
        # 主体思路不变，换一些写法。
        
        res = []

        def backtrack(currInds, leftInds):
            if not leftInds:
                tmpStr = ''
                for ind in currInds:
                    tmpStr += s[ind]
                if tmpStr not in res:
                    res.append(tmpStr)
                return
            for i, ind in enumerate(leftInds):
                currInds.append(ind)
                del leftInds[i]
                backtrack(currInds, leftInds)
                currInds.pop()
                leftInds.insert(i, ind)

        backtrack([], range(len(s)))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/188628929/

52 / 52 个通过测试用例
状态：通过
执行用时: 9092 ms
内存消耗: 20.3 MB

执行用时：9092 ms, 在所有 Python 提交中击败了5.92%的用户
内存消耗：20.3 MB, 在所有 Python 提交中击败了12.83%的用户
"""
