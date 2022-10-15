class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        if not dislikes:
            return True
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
https://leetcode.cn/submissions/detail/373385779/

69 / 70 个通过测试用例
状态：解答错误

输入：
5
[[1,2],[3,4],[4,5],[3,5]]
输出：
true
预期结果：
false
"""
