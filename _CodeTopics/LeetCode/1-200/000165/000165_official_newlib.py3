import itertools
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # 本以为自己那个就够简练了，官方答案这个更简练。
        # 另外 itertools.zip_longest() 只有 Python3 有。 
        for v1, v2 in itertools.zip_longest(version1.split('.'), version2.split('.'), fillvalue=0):
            x, y = int(v1), int(v2)
            if x != y:
                return 1 if x > y else -1
        return 0
        
"""
https://leetcode-cn.com/submissions/detail/213661334/

81 / 81 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 15 MB

执行用时：28 ms, 在所有 Python3 提交中击败了90.99%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了25.99%的用户
"""
