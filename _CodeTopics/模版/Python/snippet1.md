
# 1

开源一下我的python板子：前缀和、差分数组、线段树、树状数组 https://gist.github.com/WhiteRobe/a27fae02a337a8391533155bad0f535c
- > `前缀和.py`
```py
class PreSum:  # 标准前缀和模板
    def __init__(self, data):
        self.s = list(accumulate(data))
        self.data = data

    def query(self, i, j):  # 查询的是双闭区间[i, j]的区间和
        assert 0 <= i <= j < len(self.data)
        return self.s[j] - self.s[i] + self.data[i]
```
- > `差分数组-区间修改.py`
```py
class Diff:  # 通用加减类的差分数组模板
    def __init__(self, arr):
        self.diff = [arr[0]] * len(arr)
        for i in range(1, len(arr)):
            self.diff[i] = arr[i] - arr[i - 1]

    def modify(self, i: int, j: int, value):  # 取[i~j]的双闭区间进行区间修改
        self.diff[i] += value  # 复原时, arr[i]之后的数都会 + value
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= value

    def recover(self):  # 复原修改后的数组
        res = [self.diff[0]]
        for i in range(1, len(self.diff)):
            res.append(res[-1] + self.diff[i])
        return res
```
- > `树状数组.py`
```py
class BinIndexTree:
    def __init__(self, data: List, need_build=True):  # 由于建树开销较大，在需要动态建树时将need_build置为False
        self.n = len(data)
        self.c = [0] * (self.n + 1)  # 此时维护的是一个差分数组:data[i] = sum(c[1:i])
        self.cp = [0] * (self.n + 1)  # 差分数组:(1*c[1] + 2*c[2] + ... + n*c[n])
        if need_build:
            self.__build([0] + data)

    def __build(self, data: List):
        for i in range(1, len(data)):  # O(NlogN)
            self.__modify(i - 1, data[i] - data[i - 1])

    def __lowbit(self, x: int):
        return x & (-x)  # => n & (~n + 1), 只留下二进制码中最右侧的1

    def update(self, i: int, value: Any):  # 单点修改: 将某点的值设为value | O(logN)
        self.modify(i, i, value - self.query(i, i))

    def modify(self, i: int, j: int, offset: Any):  # 区间修改: 整个区间的每个值都偏移一个幅度 O(logN)
        self.__modify(i, offset) or self.__modify(j + 1, -offset)

    def query(self, i: int, j: int):  # 区间查询 | O(logN)
        return self.__query(j) - self.__query(i - 1)

    def __query(self, i: int):  # 核心API：求data[0~i]的和(闭区间)
        i += 1  # 统一API
        res = 0
        x = i + 1
        while i > 0:
            res += x * self.c[i] - self.cp[i]  # ☆ 仅能用于求区间合
            i -= self.__lowbit(i)
        return res

    def __modify(self, i: int, diff: Any):  # 核心API：差分修改
        i += 1  # 统一API: 由于树状数组中索引必须从1起，因此对应原数组索引从0起，此处要+1
        d_diff = i * diff
        while i <= self.n:
            self.c[i] += diff
            self.cp[i] += d_diff  # ☆ 仅能用于求区间合
            i += self.__lowbit(i)  # 修改其父级
```
- > `线段树.py`
```py
from typing import Callable, Any


class STNode:
    def __init__(self, l: int, r: int, value: Any = None):
        self.l, self.r = l, r  # 左边界和右边界
        self.value = value  # 节点值(区间值)
        self.left = self.right = self.father = None  # 左右儿子及父指针
        self.lazy = None  # 用于区间和问题的延迟更新标记

    def __repr__(self):
        return f'({self.l}~{self.r}:{self.value})'


class SegmentTree:  # class模板
    def __init__(self, fr: int, to: int, when_reach_leaf: Callable[[int], Any],
                 collect: Callable[[Any, Any], Any], lazy_update: Callable[[STNode, Any], None] = None):
        # fr, to 是整个区间的其实和终结，取双闭区间
        # when_reach_leaf 是一个函数，用于向线段树内的叶子赋值；传入叶子的索引所谓参数，返回一个任意值
        # collect 是一个函数，左区间和右区间的聚合方法；传入左区间和右区间，返回一个任意值作为两区间的聚合结果 | 左右区间应具有自反性
        # lazy_update 延迟更新算法，如果需要实现乘法的区间修改，请手动指定，否则默认取None即可
        assert fr <= to
        # 到达叶时的赋值函数, 向上递归时对左右节点值的收集函数(必须为一个自反函数)
        self.cal, self.collect = when_reach_leaf, collect
        self.root = self.__create_tree(fr, to)  # 构建根节点
        # 默认的lazy更新方法
        self.lazy_update = self.__default_lazy_update if lazy_update is None else lazy_update

    def __create_tree(self, fr, to, parent: STNode = None) -> STNode:  # 构建[fr, to]的树
        node = STNode(fr, to)
        node.father = parent  # 构建一个父指针
        if fr == to:
            node.value = self.cal(fr)  # 到达叶节点，根据元线段的值fr构建叶节点
        else:
            mid = (fr + to) >> 1
            # 构建左右子树
            node.left, node.right = self.__create_tree(fr, mid, node), self.__create_tree(mid + 1, to, node)
            node.value = self.collect(node.left.value, node.right.value)  # 后序收集区间值
        return node

    def query(self, fr: int, to: int):  # 区间查询 | O(logN)
        assert self.root.l <= fr <= to <= self.root.r

        def dfs(node, _fr, _to) -> Any:
            if node.lazy is not None:  # 下传懒惰标记，仅适用于区间和问题
                self.__push_down(node)

            l, r = node.l, node.r
            if l == _fr and r == _to:  # 找到对应区间
                return node.value
            else:
                mid = (l + r) >> 1
                if _to <= mid:  # 在左区间
                    return dfs(node.left, _fr, _to)
                elif _fr > mid:  # 在右区间
                    return dfs(node.right, _fr, _to)
                else:  # 跨区间
                    return self.collect(dfs(node.left, _fr, mid), dfs(node.right, mid + 1, _to))

        return dfs(self.root, fr, to)

    def update(self, i: int, value: Any):  # 单点修改: 把元线段[i, i]的值修改为value
        assert self.root.l <= i <= self.root.r

        def dfs(node):
            l, r = node.l, node.r
            if l == i == r:  # 找到对应元线段
                node.value = value
            else:
                mid = (l + r) >> 1
                if i <= mid:  # 在左区间
                    dfs(node.left)
                elif i > mid:  # 在右区间
                    dfs(node.right)
                node.value = self.collect(node.left.value, node.right.value)  # 后序收集区间值

        dfs(self.root)

    # 加强内容 -- push_down及区间修改 -- #
    #   仅适用于区间和

    def modify(self, fr: int, to: int, offset: Any):  # 区间修改: 整个区间的每个值都偏移一个幅度 O(logN)
        assert self.collect(3527, 1007) == 3527 + 1007  # 简单判定是否为区间和问题

        def dfs(node, _fr, _to):
            l, r = node.l, node.r
            if l == _fr and r == _to:  # 找到对应区间
                self.lazy_update(node, offset)
            else:
                mid = (l + r) >> 1
                if _to <= mid:  # 在左区间
                    dfs(node.left, _fr, _to)
                elif _fr > mid:  # 在右区间
                    dfs(node.right, _fr, _to)
                else:  # 跨区间
                    dfs(node.left, _fr, mid)
                    dfs(node.right, mid + 1, _to)
                self.collect(node.left.value, node.right.value)  # 后序收集区间值

        dfs(self.root, fr, to)

    def __default_lazy_update(self, ch: STNode, lazy: Any):
        meta_size = (ch.r - ch.l + 1)  # (r - l + 1)为此区间的元线段数
        ch.value += meta_size * lazy
        ch.lazy = ch.lazy + lazy if ch.lazy is not None else lazy

    def __push_down(self, node: STNode):
        if node.l != node.r:  # 非元线段
            # 给左右子树下传延迟更新标记并更新其值
            self.lazy_update(node.left, node.lazy)
            self.lazy_update(node.right, node.lazy)
        node.lazy = None  # 元线段不用下传lazy标志, 当前节点的lazy标志可清零
```
