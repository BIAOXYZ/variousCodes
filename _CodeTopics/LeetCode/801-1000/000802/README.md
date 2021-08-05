
`802. 找到最终的安全状态` https://leetcode-cn.com/problems/find-eventual-safe-states/solution/zhao-dao-zui-zhong-de-an-quan-zhuang-tai-yzfz/
- [ ] 方法一：深度优先搜索 + 三色标记法
- [ ] 方法二：拓扑排序

【GTAlgorithm】5分钟干掉拓扑排序 https://leetcode-cn.com/problems/find-eventual-safe-states/solution/gtalgorithm-san-ju-hua-jiao-ni-wan-zhuan-xf5o/
- > 如果你仍然想更多地了解拓扑排序，可以阅读我们写的[拓扑排序专题](https://mp.weixin.qq.com/s/24wIzDXN_NQuK1ICRmEtbw)。在这之后，你可能会想拿下面几道题练练手：
  ```console
  LeetCode 207.课程表 (中等)
  LeetCode 210.课程表II (中等)
  LeetCode 329.矩阵中的最长递增路径 (困难)
  LeetCode 1203.项目管理 （困难）
  ```

# 测试用例

```
[[1,2],[2,3],[5],[0],[5],[],[]]
[[1,2,3,4],[1,2],[3,4],[0,4],[]]

[[],[0,2,3,4],[3],[4],[]]

[[1,3,4,5,7,9],[1,3,8,9],[3,4,5,8],[1,8],[5,7,8],[8,9],[7,8,9],[3],[],[]]

[[2,3,4,7,9],[12,13,15,19],[9],[3,13],[2,9,14,15,19],[6,15,18],[13],[13,14,17,18,19],[10,15],[16],[15],[13,15,16,17,19],[5,14,15,16,17],[9,18,19],[13,15,16,17,18,19],[1,16,17,18,19],[17,19],[18,19],[],[]]
```
