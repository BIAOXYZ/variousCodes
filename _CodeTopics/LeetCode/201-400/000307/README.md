
`307. 区域和检索 - 数组可修改` https://leetcode-cn.com/problems/range-sum-query-mutable/solution/qu-yu-he-jian-suo-shu-zu-ke-xiu-gai-by-l-76xj/
- [x] 方法一：分块处理
- [ ] 方法二：线段树
  * > 线段树 `segmentTree` 是一个二叉树，***每个结点保存数组 `nums` 在区间 `[s,e]` 的最小值、最大值或者总和等信息***。线段树可以用`树`也可以用`数组`（堆式存储）来实现。***对于数组实现，假设根结点的下标为 `0`，如果一个结点在数组的下标为 `node`，那么它的左子结点下标为 `node×2+1`，右子结点下标为 `node×2+2`***。
- [ ] 方法三：树状数组
  * > 关于树状数组的详细介绍可以参考百度百科「[树状数组](https://baike.baidu.com/item/%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84)」，本文不作过多介绍。
  * > 树状数组是一种可以***动态维护序列前缀和的数据结构***（序列下标从 `1` 开始），它的功能是：
    + > 单点修改 `add(index,val)`：把序列第 `index` 个数增加 `val`；
    + > 区间查询 `prefixSum(index)`：查询前 `index` 个元素的前缀和。

```
["NumArray","sumRange","update","sumRange"]
[[[1,3,5]],[0,2],[1,2],[0,2]]

["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
[[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]
```
