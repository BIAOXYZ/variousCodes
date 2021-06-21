class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 典型的回溯算法，类似 `LC47 全排列 II`：也就是可以有重复元素的全排列。
        
        length = len(s)
        res = set()

        def backtrack(currInds, leftInds):
            if len(leftInds) == 0:
                tmpStr = ''
                for ind in currInds:
                    tmpStr += s[ind]
                res.add(tmpStr)
            else:
                for i, ind in enumerate(leftInds):
                    currInds.append(ind)
                    leftInds.pop(i)
                    backtrack(currInds, leftInds)
                    currInds.pop()
                    leftInds.insert(i, ind)

        backtrack([], range(length))
        return list(res)
        
"""
https://leetcode-cn.com/submissions/detail/188628711/

52 / 52 个通过测试用例
状态：通过
执行用时: 448 ms
内存消耗: 22.3 MB

执行用时：448 ms, 在所有 Python 提交中击败了14.18%的用户
内存消耗：22.3 MB, 在所有 Python 提交中击败了6.05%的用户
"""
