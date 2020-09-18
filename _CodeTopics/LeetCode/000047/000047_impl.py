class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def backtrace(currArr, leftArr):
            if not leftArr:
                tmpArr = currArr[:]
                if tmpArr not in res:
                    res.append(tmpArr)
                return
            for ind in range(len(leftArr)):
                # 这里还必须申请个临时变量 num 把 leftArr[ind] 存一下。不然最后insert那句就报错了。
                # 相当于往 leftArr 的下标为 ind 的位置插入 leftArr[ind] 所以报错？
                num = leftArr[ind]
                currArr.append(num)
                # 这里不能用 del leftArr[ind] ， 因为del的语法要求。
                # 删list的指定index的元素的时候就得这么用。但是应该也可以用带index参数的pop()，一会再试下。
                del leftArr[ind]
                backtrace(currArr, leftArr)
                currArr.pop()
                leftArr.insert(ind, num)

        backtrace([], nums)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/109356448/

30 / 30 个通过测试用例
状态：通过
执行用时: 984 ms
内存消耗: 12.8 MB

执行用时：984 ms, 在所有 Python 提交中击败了18.07%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了16.10%的用户
"""
