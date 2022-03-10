class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        n = len(parents)
        fatherSonsDic = {i:[] for i in range(n)}
        for i in range(1, n):
            father, son = parents[i], i
            fatherSonsDic[father].append(son)

        nodeSizeDic = {i:1 for i in range(n)}
        def dfs_and_count_total_nodes(node: int) -> int:
            if not fatherSonsDic[node]:
                return 1
            else:
                for son in fatherSonsDic[node]:
                    nodeSizeDic[node] += dfs_and_count_total_nodes(son)
                return nodeSizeDic[node]
        
        dfs_and_count_total_nodes(0)
        ## print(fatherSonsDic, nodeSizeDic)
        scores = [1 for _ in range(n)]
        for i in range(n):
            sons = fatherSonsDic[i]
            if sons == []:
                scores[i] = n - 1
            else:
                # 其实和 if 分支可以合并，但是还是先分开吧，回头看的时候容易读。
                subTree1Nodes = subTree2Nodes = otherNodes = 0
                subTree1Nodes = nodeSizeDic[sons[0]]
                subTree2Nodes = nodeSizeDic[sons[1]] if len(sons) == 2 else 0
                otherNodes = n - nodeSizeDic[i]
                for num in [subTree1Nodes, subTree2Nodes, otherNodes]:
                    if num > 0:
                        scores[i] *= num
        return scores.count(max(scores))
        
"""
https://leetcode-cn.com/submissions/detail/281043946/

执行用时：796 ms, 在所有 Python3 提交中击败了47.37%的用户
内存消耗：115.3 MB, 在所有 Python3 提交中击败了58.95%的用户
通过测试用例：
206 / 206
"""
