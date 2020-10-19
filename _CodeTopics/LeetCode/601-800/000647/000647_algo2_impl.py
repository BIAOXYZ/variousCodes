class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        len1 = len(s)

        # 构造插入了“#”间隔符的新字符串。但这里不是要用马拉车，而只是准备纯粹用中心扩散。
        lis = list(s)
        for i in range(len1 + 1):
            lis.insert(i*2, "#")
        s = "".join(lis)

        res = 0
        len2 = len1 * 2 + 1
        # 首尾的分隔符肯定不会形成回文子串，所以直接跳过。
        for i in range(1, len2 - 1):
            if s[i] != "#":
                left = right = i
            else:
                left, right = i-1, i+1 
            while left >= 1 and right <= len2 - 2:
                if s[left] == s[right]:
                    res += 1
                    left -= 2
                    right += 2
                else:
                    break
        return res
        
"""
https://leetcode-cn.com/submissions/detail/116475180/

130 / 130 个通过测试用例
状态：通过
执行用时: 96 ms
内存消耗: 13.1 MB

执行用时：96 ms, 在所有 Python 提交中击败了73.64%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了42.32%的用户
"""
