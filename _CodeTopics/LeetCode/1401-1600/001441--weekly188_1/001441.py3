class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        # 第 188 场周赛第一题
        
        se = set(target)
        res = []
        for i in range(1, n+1):
            if i > target[-1]:
                break
            if i in se:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
        return res
        
"""
https://leetcode.cn/submissions/detail/373095323/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
89.44%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
31.11%
的用户
通过测试用例：
49 / 49
"""
