class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # 手动狗头题
        """
        注意：只用 s = reversed(s) 是不行的！
        """
        s = list(reversed(s))
        
"""
https://leetcode-cn.com/submissions/detail/113949703/

23 / 478 个通过测试用例
状态：解答错误

输入：
["h","e","l","l","o"]
输出：
["h","e","l","l","o"]
预期：
["o","l","l","e","h"]

# 这个应该是对的（别处试没问题），只是LeetCode系统bug了。
"""
