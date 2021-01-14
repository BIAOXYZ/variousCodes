
`947. 移除最多的同行或同列石头` https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/947-yi-chu-zui-duo-de-tong-xing-huo-tong-ezha/
- 方法：并查集

`947. 移除最多的同行或同列石头` https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/yi-chu-zui-duo-de-tong-xing-huo-tong-lie-m50r/
- 方法一：深度优先搜索
- 方法二：优化建图 + 深度优先搜索
- 方法三：优化建图 + 并查集

# 测试用例

```
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
[[0,0],[0,2],[1,1],[2,0],[2,2]]
[[0,0]]
```

## 测试用例展开

```
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
1 1 0
1 0 1
0 1 1

[[0,0],[0,2],[1,1],[2,0],[2,2]]
1 0 1
0 1 0
1 0 1
```
