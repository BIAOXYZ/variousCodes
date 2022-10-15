class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        ddic = defaultdict(list)
        for e1, e2 in dislikes:
            ddic[e1].append(e2)
            ddic[e2].append(e1)

        groups = [set(), set()]
        round = 0
        keys = list(ddic.keys())
        currLevel, nextLevel = [keys[0]], set()
        while currLevel:
            for person in currLevel:
                groups[round].add(person)
                for notLiked in ddic[person]:
                    if notLiked not in groups[round^1]:
                        nextLevel.add(notLiked)
            currLevel = list(nextLevel)
            nextLevel.clear()
            round ^= 1
        return False if groups[0] & groups[1] != set() else True
        
"""
https://leetcode.cn/submissions/detail/373385731/

4 / 70 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    currLevel, nextLevel = [keys[0]], set()
Line 12 in possibleBipartition (Solution.py)
    ret = Solution().possibleBipartition(param_1, param_2)
Line 49 in _driver (Solution.py)
    _driver()
Line 60 in <module> (Solution.py)
最后执行的输入：
1
[]
"""
