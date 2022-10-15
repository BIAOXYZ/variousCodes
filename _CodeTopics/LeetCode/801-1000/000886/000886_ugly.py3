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
            if not currLevel:
                for person in keys:
                    if person not in groups[0] and person not in groups[1]:
                        currLevel.append(person)
                        break
        return False if groups[0] & groups[1] != set() else True
        
"""
https://leetcode.cn/submissions/detail/373386290/

执行用时：
144 ms
, 在所有 Python3 提交中击败了
36.57%
的用户
内存消耗：
18.8 MB
, 在所有 Python3 提交中击败了
67.23%
的用户
通过测试用例：
70 / 70
"""
