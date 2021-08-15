class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_beautiful(num, i):
            return (num >=i and num % i == 0) or (i >= num and i % num == 0)

        def backtrack_is_beautiful(currArr, nextPos, leftArr):
            if not leftArr:
                res[0] += 1
                return
            for num in leftArr:
                if is_beautiful(num, nextPos):
                    currArr.append(num)
                    index = leftArr.index(num)
                    leftArr.remove(num)
                    backtrack_is_beautiful(currArr, nextPos+1, leftArr)
                    currArr.pop()
                    leftArr.insert(index, num)
        
        res = [0]
        backtrack_is_beautiful([], 1, range(1, n+1))
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/207363239/

15 / 15 个通过测试用例
状态：通过
执行用时: 1012 ms
内存消耗: 13.2 MB

执行用时：1012 ms, 在所有 Python 提交中击败了44.44%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了37.04%的用户
"""
