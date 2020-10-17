class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        length = len(s)

        res = 0
        # 还是用类似补间隔符的方式来做普通的中心扩散，但这次跟答案的做法类似（可能细节还是有点小差别）：
        # 并不实际插入间隔符，只是脑补有那些（`length-1`个）间隔符的存在。。。
        # 当然，看官方答案的描述，其实它的思想更像我的第一个实现（`000647_algo2.py `）：对于每一个位置i
        # （最后一个位置除外），都有两个回文中心，i和i+1。最后一个字符只有一个回文中心，所以一共2n-1个。
        for i in range(2*length - 1):
            # 此时是字符为中心，或者说奇数回文中心。
            if i % 2 == 0:
                left = right = i/2
            # 此时是脑补的分隔符为中心，或者说偶数回文中心。
            else:
                left, right = i/2 , i/2 + 1
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    res += 1
                    left -= 1
                    right += 1
                else:
                    break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/116484964/

130 / 130 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 13.2 MB

执行用时：80 ms, 在所有 Python 提交中击败了86.99%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了42.23%的用户
"""
