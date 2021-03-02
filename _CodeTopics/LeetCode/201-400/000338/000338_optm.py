class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        def number_of_one(n):
            res = 0
            while n:
                """
                if n % 2 == 1:
                    res += 1
                    n = (n-1)/2
                else:
                    n /= 2
                """
                # 下面是参考答案里的实现，和LC1178里的穷举子集的位运算相似，但是有一点不同：
                # 那里是一直和原始的数按位&，这里是不断更新原始的数。
                n &= n - 1
                res += 1
            return res
        
        res = [0]
        for i in range(1, num+1):
            res.append(number_of_one(i))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/150392732/

15 / 15 个通过测试用例
状态：通过
执行用时: 88 ms
内存消耗: 17 MB

执行用时：88 ms, 在所有 Python 提交中击败了22.01%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了24.60%的用户
"""
