class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        sumA, sumB = sum(A), sum(B)
        if sumA > sumB:
            flag = "A"
            big, small = A, B
        else:
            flag = "B"
            big, small = B, A
        
        diff = abs(sumA - sumB) / 2
        res = []
        setSmall = set(small)
        for num in big:
            if num - diff > 0 and num - diff in setSmall:
                res.append(num)
                res.append(num - diff)
                break
        
        if flag == "B":
            res = res[::-1]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/142695137/

75 / 75 个通过测试用例
状态：通过
执行用时: 316 ms
内存消耗: 15.2 MB

执行用时：316 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：15.2 MB, 在所有 Python 提交中击败了51.76%的用户
"""
"""
注：哎呀，挺吉利的。题号888的题目搞了个100%~
"""
