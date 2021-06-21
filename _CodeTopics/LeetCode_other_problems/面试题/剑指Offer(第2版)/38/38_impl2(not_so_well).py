class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 典型的回溯算法，类似 `LC47 全排列 II`：也就是可以有重复元素的全排列。
        # 主体思路不变，换一些写法。
        
        # 之前也用过remove，过了；但是我今天想了想感觉remove好像不对啊。。。不过仔细想想还是可以的，
        # 因为虽然删掉的index不一定是当前的（比如"aaab"想着删除第二个或第三个'a'，但用remove永远会删掉第一个
        # ————不过对这道题来说没问题啊，反正保证剩下的是一样的就可以了。）
        
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
                leftInds.remove(ind)
                backtrack(currInds, leftInds)
                currInds.remove(ind)
                leftInds.insert(i, ind)

        backtrack([], range(len(s)))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/188629135/

52 / 52 个通过测试用例
状态：通过
执行用时: 9068 ms
内存消耗: 20.1 MB

执行用时：9068 ms, 在所有 Python 提交中击败了5.92%的用户
内存消耗：20.1 MB, 在所有 Python 提交中击败了13.81%的用户
"""
