class MyTreeNode:
    def __init__(self, ind, val):
        self.ind = ind
        self.val = val
        self.fa = None
        self.sons = []

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:

        # 先写一个 trivial 的，肯定超时的。原因是最差情况下，如果这个树退化为一个链表，
        # 则每个节点在最差情况下可能都需要回溯到 root，于是就是 O(n^2) 的复杂度了。

        def generate_tree(nums, edges):
            nodeLis = [MyTreeNode(ind, num) for ind, num in enumerate(nums)]
            dummyNode = MyTreeNode(-1, -1)
            nodeLis[0].fa = dummyNode
            for fa, son in edges:
                faNode, sonNode = nodeLis[fa], nodeLis[son]
                faNode.sons.append(sonNode)
                sonNode.fa = faNode
            return nodeLis

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b!=0:
                a, b = b, a%b
            return a
        
        def reverse_find_nearest_co_prime_ancestor(node):
            val = node.val
            faNode = node.fa
            while faNode:
                if gcd(val, faNode.val) == 1:
                    return faNode.ind
                faNode = faNode.fa
            return -1

        def dfs_and_find_ancestors_for_all(node):
            if not node:
                return
            coPrimeAncestorInd = reverse_find_nearest_co_prime_ancestor(node)
            res[node.ind] = coPrimeAncestorInd
            for son in node.sons:
                dfs_and_find_ancestors_for_all(son)

        n = len(nums)
        res = [-1] * n
        nodeLis = generate_tree(nums, edges)
        root = nodeLis[0]
        dfs_and_find_ancestors_for_all(root)
        return res
        
"""
https://leetcode.cn/problems/tree-of-coprimes/submissions/529699054?envType=daily-question&envId=2024-04-11

解答错误
5 / 37 个通过的测试用例

输入
nums =
[9,16,30,23,33,35,9,47,39,46,16,38,5,49,21,44,17,1,6,37,49,15,23,46,38,9,27,3,24,1,14,17,12,23,43,38,12,4,8,17,11,18,26,22,49,14,9]
edges =
[[17,0],[30,17],[41,30],[10,30],[13,10],[7,13],[6,7],[45,10],[2,10],[14,2],[40,14],[28,40],[29,40],[8,29],[15,29],[26,15],[23,40],[19,23],[34,19],[18,23],[42,18],[5,42],[32,5],[16,32],[35,14],[25,35],[43,25],[3,43],[36,25],[38,36],[27,38],[24,36],[31,24],[11,31],[39,24],[12,39],[20,12],[22,12],[21,39],[1,21],[33,1],[37,1],[44,37],[9,44],[46,2],[4,46]]

输出
[17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
预期结果
[-1,21,17,43,10,42,7,13,29,44,17,31,39,10,10,29,32,0,40,23,12,39,12,40,25,35,15,38,40,40,17,24,5,1,19,14,17,21,25,24,14,17,40,25,37,17,10]
"""
