class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        length = len(s)
        lis = list(s)

        slow, fast = 0, k
        while fast < length:
            # 不能简单的通过翻转切片的方式实现部分翻转，比如 lis[slow:fast].reverse() 是不行的。
            # - python reverse反转部分数组 https://blog.csdn.net/weixin_41043240/article/details/79930038
            lis[slow:fast] = reversed(lis[slow:fast])
            slow = fast + k
            fast += 2*k
        
        if slow < length:
            lis[slow:min(slow + k, length)] = reversed(lis[slow:min(slow + k, length)])
        return ''.join(lis)
        
"""
https://leetcode-cn.com/submissions/detail/209033695/

60 / 60 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.2 MB

执行用时：16 ms, 在所有 Python 提交中击败了90.91%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了73.14%的用户
"""
