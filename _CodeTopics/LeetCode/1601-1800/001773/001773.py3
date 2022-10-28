class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        dic = {"type":0, "color":1, "name":2}
        ind = dic[ruleKey]
        return sum(item[ind] == ruleValue for item in items)
        
"""
https://leetcode.cn/submissions/detail/377403379/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
92.98%
的用户
内存消耗：
19.2 MB
, 在所有 Python3 提交中击败了
33.33%
的用户
通过测试用例：
92 / 92
"""
