import collections
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        
        # 利用collections自带的Counter，除了函数调用部分，其他和自己手写实现频率统计的字典没啥区别。

        dic1 = collections.Counter(chars)

        res = 0
        for word in words:
            flag = "possible"
            dic = collections.Counter(word)
            for k, v in dic.items():
                if k not in dic1 or v > dic1[k]:
                    flag = "impossible"
                    break
            if flag == "possible":
                res += len(word)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/146262642/

36 / 36 个通过测试用例
状态：通过
执行用时: 432 ms
内存消耗: 13.8 MB

执行用时：432 ms, 在所有 Python 提交中击败了21.95%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了84.76%的用户
"""
