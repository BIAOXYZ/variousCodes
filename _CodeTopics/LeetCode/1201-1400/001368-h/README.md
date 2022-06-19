
`1368. 使网格图至少有一条有效路径的最小代价` https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solution/shi-wang-ge-tu-zhi-shao-you-yi-tiao-you-xiao-lu-2/
- [ ] 方法一：Dijkstra 算法
- [x] 方法二：0-1 广度优先搜索

【[:star:][`*`]】 最短路径算法：Dijkstra, BFS, SPFA, 0-1 BFS（本题最佳方法） https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solution/zui-duan-lu-jing-suan-fa-bfs0-1bfsdijkstra-by-luci/
>> //notes：其实 0-1 BFS 这个还是在第 295 场周赛的讨论区看到的： https://leetcode.cn/circle/discuss/E0MOm0/view/H6Uk7Z/

```
[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
[[1,1,3],[3,2,2],[1,1,4]]
[[1,2],[4,3]]
[[2,2,2],[2,2,2]]
[[4]]
```
