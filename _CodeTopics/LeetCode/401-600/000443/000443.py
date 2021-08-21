class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        res = []
        stk = []
        for ch in chars:
            if not stk or stk[-1] == ch:
                stk.append(ch)
            else:
                res.append(stk[-1])
                tmpLength = len(stk)
                if tmpLength > 1:
                    for digit in str(tmpLength):
                        res.append(digit)
                stk = [ch]
        
        res.append(stk[-1])
        tmpLength = len(stk)
        if tmpLength > 1:
            for digit in str(tmpLength):
                res.append(digit)
        
        # 艹了，为什么这句直接赋值不行啊。虽然知道是想考察原地算法，但是我只想先取个巧而已。
        ## --> 自己试了下，用两个 list 模拟，然后查 id(l1), id(l2)，发现直接赋值两个id就一样了，所以只能一个元素一个元素拷贝
        for i in range(min(len(chars), len(res))):
            chars[i] = res[i]
        if len(chars) > len(res):
            for j in range(len(chars)-1, len(res)-1, -1):
                del chars[j]
        return len(res)
        
"""
https://leetcode-cn.com/submissions/detail/209561010/

70 / 70 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了82.42%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了76.92%的用户
"""
