class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:

        res = [0] * (n + 1)
        adjacencyMatrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for coordinate1, coordinate2 in edges:
            adjacencyMatrix[coordinate1][coordinate2] = 1
            adjacencyMatrix[coordinate2][coordinate1] = 1
        ## print(adjacencyMatrix)

        def all_nodes_are_connected(nodes):
            def dfs(node):
                if node in visited:
                    return
                tmpNodes.append(node)
                visited.add(node)
                for nextNode, val in enumerate(adjacencyMatrix[node]):
                    if val > 0 and nextNode in nodes:
                        dfs(nextNode)
            tmpNodes = []
            visited = set()
            dfs(nodes[0])
            return True if sorted(tmpNodes) == sorted(nodes) else False

        # 这个函数参考了 `LC543. 二叉树的直径` 里我的这个提交：
        # https://leetcode.cn/submissions/detail/121917537/
        def calculate_tree_diameter(nodes):
            visited = set()
            dic = {}
            def dfs_and_calculate_max_subtree_depth(node):
                distances = []
                if node in visited:
                    return 1
                visited.add(node)
                for nextNode, val in enumerate(adjacencyMatrix[node]):
                    if val > 0 and nextNode in nodes:
                        distances.append(dfs_and_calculate_max_subtree_depth(nextNode))
                distances.sort()
                dic[node] = distances[-1] + distances[-2] if len(distances) > 1 else distances[-1]
                return distances[-1]
            dfs_and_calculate_max_subtree_depth(nodes[0])
            return max(dic.values())

        for bitmap in range(2**n):
            nodes = []
            for j in range(1, n+1):
                if bitmap & 2**(j-1):
                    nodes.append(j)
            ## print(nodes)
            if len(nodes) < 2:
                continue
            if all_nodes_are_connected(nodes):
                diameter = calculate_tree_diameter(nodes)
                res[diameter] += 1
        return res[1:n]
        
"""
https://leetcode.cn/submissions/detail/412412079/

4 / 31 个通过测试用例
状态：解答错误

输入：
4
[[1,3],[1,4],[2,3]]
输出：
[3,3,0]
预期结果：
[3,2,1]
"""
