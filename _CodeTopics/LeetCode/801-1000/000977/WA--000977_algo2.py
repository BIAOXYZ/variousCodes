from collections import deque
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        length = len(A)

        if A[0] >= 0:
            f = lambda x: x ** 2
            return [f(elem) for elem in A]
            # 上面两句可以用下面一句替代。
            # return [(lambda x: x ** 2)(elem) for elem in A]       
        if A[length-1] < 0:
            # 这里当然可以继续先定义lambda函数，然后代入：
            #     g = lambda x: x ** 2
            #     return [f(elem) for elem in A]
            # 不过下面这种写法才体现了lambda匿名函数的精髓吧。
            return reversed([(lambda x: x ** 2)(elem) for elem in A])

        # 官方答案里有两种双指针，第一种是“方法三 双指针”，也就是传统的从两边向中间。
        # 这是第二种，两个指针从中间向两边移动。
        left = 0
        while A[left] < 0:
            left += 1
        right, left = left, left - 1

        res = []
        while left >= 0 and right <= length-1:
            if abs(A[left]) <= A[right]:
                res.append(A[left]**2)
                left -= 1
            else:
                res.append(A[right]**2)
                right += 1
        # 一个指针到头后，把剩下的元素依次平方后贴到结果数组末尾。
        if left == -1:
            for i in range(right, length):
                res.append(A[right]**2)
        elif right == length:
            for i in range(left, -1, -1):
                res.append(A[left]**2)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/116229748/

103 / 132 个通过测试用例
状态：解答错误

输入：
[-2,2,3]
输出：
[4,4,4]
预期：
[4,4,9]
"""
