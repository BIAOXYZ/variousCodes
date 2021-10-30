class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        l = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        se = [set(elem) for elem in l]
        
        def is_in_same_line(w):
            w = set(w.lower())
            for elem in se:
                if w.issubset(elem):
                    return True
            return False

        res = []
        for word in words:
            if is_in_same_line(word):
                res.append(word)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/233915102/

执行用时：12 ms, 在所有 Python 提交中击败了89.08%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了12.61%的用户
通过测试用例：
22 / 22
"""
