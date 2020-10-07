class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        length = len(s)
        for i in range(length/2):
            s[i], s[length-1-i] = s[length-1-i], s[i]
        
```
https://leetcode-cn.com/submissions/detail/113948698/

478 / 478 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 19.7 MB

执行用时：36 ms, 在所有 Python 提交中击败了96.71%的用户
内存消耗：19.7 MB, 在所有 Python 提交中击败了10.84%的用户
```
