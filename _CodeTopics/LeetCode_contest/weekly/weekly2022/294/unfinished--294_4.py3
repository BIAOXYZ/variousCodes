# from: 
# [算法]线段树的python实现 https://blog.csdn.net/qq_33935895/article/details/102806357


# 线段树的节点类
class TreeNode(object):
    def __init__(self):
        self.left = -1
        self.right = -1
        self.sum_num = 0
        self.min = 10**9 + 1

# 线段树类
# 以_开头的是递归实现
class Tree(object):
    def __init__(self, n, arr):
        self.n = n
        self.max_size = 4 * n
        self.tree = [TreeNode() for i in range(self.max_size)]  # 维护一个TreeNode数组
        self.arr = arr

    # index从1开始
    def _build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].sum_num = self.arr[left - 1]
            self.tree[index].min = self.arr[left - 1]
        else:
            mid = (left + right) // 2
            self._build(index * 2, left, mid)
            self._build(index * 2 + 1, mid + 1, right)
            self.pushup_sum(index)
            self.pushup_min(index)

    # 构建线段树
    def build(self):
        self._build(1, 1, self.n)

    # 求和
    def pushup_sum(self, k):
        self.tree[k].sum_num = self.tree[k * 2].sum_num + self.tree[k * 2 + 1].sum_num

    def pushup_min(self, k):
        self.tree[k].min = min(self.tree[k * 2].min, self.tree[k * 2 + 1].min)
        
    def _query(self, ql, qr, i, l, r, ):
        if l >= ql and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].sum_num
        else:
            mid = (l + r) // 2
            res_l = 0
            res_r = 0
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query(ql, qr, i * 2 + 1, mid + 1, r, )
            return res_l + res_r

    # 区间查询
    def query(self, ql, qr):
        return self._query(ql, qr, 1, 1, self.n)
        

    def _query_min(self, ql, qr, i, l, r, ):
        if l >= ql and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].min
        else:
            mid = (l + r) // 2
            res_l = float('inf')
            res_r = float('inf')
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query_min(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query_min(ql, qr, i * 2 + 1, mid + 1, r, )
            return min(res_l, res_r)

    # 区间查询
    def query_min(self, ql, qr):
        return self._query_min(ql, qr, 1, 1, self.n)
        
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        
        n = len(strength)
        tree = Tree(n, strength)
        tree.build()
        res = tree.query(2, n)
        print(res)
        res = tree.query_min(2, n)
        print(res)
        res = tree.query(2, 3)
        print(res)
        res = tree.query_min(2, 3)
        print(res)
        
