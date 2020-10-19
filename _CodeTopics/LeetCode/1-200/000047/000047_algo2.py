class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrace(currArr, leftArr):
            if not leftArr:
                tmpArr = currArr[:]
                # if tmpArr not in res:
                #     res.append(tmpArr)
                res.append(tmpArr)
                return
            for i in range(len(leftArr)):
                # 因为这里虽然可能有重复数字，但是我先排个序，然后只要在同轮循环里碰到和前面一样的
                # 数字，就直接continue。最后往res贴结果的时候应该连去重的判断都可以省略了。
                if i != 0 and leftArr[i] == leftArr[i-1]:
                    continue
                num = leftArr[i]
                currArr.append(num)
                leftArr.pop(i)
                backtrace(currArr, leftArr)
                currArr.pop()
                leftArr.insert(i, num)

        res = []
        nums.sort()
        backtrace([], nums)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109476521/

30 / 30 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.7 MB

执行用时：20 ms, 在所有 Python 提交中击败了98.45%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了40.41%的用户
"""
