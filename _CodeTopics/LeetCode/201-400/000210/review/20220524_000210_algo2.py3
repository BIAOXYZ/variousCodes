class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 隔了一阵子后重写，发现和当初写的版本（`000210_algo2.py`）还是很像。

        inDegree = [0] * numCourses
        depDic = defaultdict(list)
        # dependent 依赖于 prerequisite。
        for dependent, prerequisite in prerequisites:
            inDegree[dependent] += 1
            depDic[prerequisite].append(dependent)
        
        res = []
        zeroInDegree = deque([i for i in range(numCourses) if inDegree[i] == 0])
        while zeroInDegree:
            curr = zeroInDegree.popleft()
            res.append(curr)
            for dependent in depDic[curr]:
                inDegree[dependent] -= 1
                if inDegree[dependent] == 0:
                    zeroInDegree.append(dependent)
        
        if all(inDegree[i] == 0 for i in range(numCourses)):
            return res
        return []
        
"""
https://leetcode.cn/submissions/detail/317305212/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
96.31%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
56.60%
的用户
通过测试用例：
45 / 45
"""
