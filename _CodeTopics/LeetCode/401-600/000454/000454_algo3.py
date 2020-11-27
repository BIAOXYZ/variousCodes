import bisect
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        # （强行为了）二分查找（而二分查找）。

        """
        # 第一个函数直接照搬官方文档： https://docs.python.org/zh-cn/2.7/library/bisect.html
        --> 『上面的 bisect() 函数对于找到插入点是有用的，但在一般的搜索任务中可能会有点尴尬。
        下面 5 个函数展示了如何将其转变成有序列表中的标准查找函数。』

        # 但是第二个函数官方没有，是自己改编的。说实话还挺容易错的，因此记一下。主要注意下为啥if分支
        # 里的判断条件是那么写的，以及为啥return的是i-1而不是i。
        """
        def binary_search_leftmost_equal(arr, x):
            i = bisect.bisect_left(arr, x)
            if i != len(arr) and arr[i] == x:
                return i
            else:
                return -1
        def binary_search_rightmost_equal(arr, x):
            i = bisect.bisect_right(arr, x)
            if i < len(arr) + 1 and arr[i-1] == x:
                return i-1
            else:
                return -1

        lisAB, lisCD = [], []
        for numa in A:
            for numb in B:
                lisAB.append(numa + numb)
        for numc in C:
            for numd in D:
                lisCD.append(numc + numd)
        lisAB.sort()
        lisCD.sort()
            
        res = 0
        length = len(lisAB)
        for i in range(length):
            if i > 0 and lisAB[i] == lisAB[i-1]:
                res += tmp
            else:
                leftIndex = binary_search_leftmost_equal(lisCD, -lisAB[i])
                if leftIndex != -1:
                    tmp = binary_search_rightmost_equal(lisCD, -lisAB[i]) - leftIndex + 1
                    res += tmp
                else:
                    tmp = 0
        return res
        
"""
https://leetcode-cn.com/submissions/detail/126805891/

48 / 48 个通过测试用例
状态：通过
执行用时: 672 ms
内存消耗: 36 MB

执行用时：672 ms, 在所有 Python 提交中击败了5.36%的用户
内存消耗：36 MB, 在所有 Python 提交中击败了13.13%的用户
"""
