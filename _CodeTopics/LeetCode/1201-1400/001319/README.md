
`1319. 连通网络的操作次数` https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/solution/lian-tong-wang-luo-de-cao-zuo-ci-shu-by-leetcode-s/
- [x] 方法一：深度优先搜索
- [x] 方法二：并查集

# 测试用例

```
4
[[0,1],[0,2],[1,2]]
6
[[0,1],[0,2],[0,3],[1,2],[1,3]]
6
[[0,1],[0,2],[0,3],[1,2]]
5
[[0,1],[0,2],[3,4],[2,3]]
```

# `001319_impl--(with-flaw).py` 和 `001319_impl2--(with-flaw).py`

这道题是第一次写并查集`union()`函数的时候加上**`按秩合并`**（其实也是第一次把并查集按class来写），结果前两个就写错了。。。因为必须要单独考虑两个father的rank相等的情况，此时还需要给最终当father的那个的rank加上1。
