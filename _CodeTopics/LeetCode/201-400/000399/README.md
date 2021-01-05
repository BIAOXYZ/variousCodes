
`399. 除法求值` https://leetcode-cn.com/problems/evaluate-division/solution/399-chu-fa-qiu-zhi-nan-du-zhong-deng-286-w45d/
- > 这道题是在「力扣」第 990 题（[等式方程的可满足性](https://leetcode-cn.com/problems/satisfiability-of-equality-equations/)）的基础上，在变量和变量之间有了倍数关系。由于 变量之间的倍数关系具有传递性，处理有传递性关系的问题，可以使用「并查集」，我们需要在并查集的「合并」与「查询」操作中 维护这些变量之间的倍数关系。
- [ ] 方法：并查集
- > **练习**
  ```console
  「力扣」第 547 题：省份数量（中等）；
  「力扣」第 684 题：冗余连接（中等）；
  「力扣」第 1319 题：连通网络的操作次数（中等）；
  「力扣」第 1631 题：最小体力消耗路径（中等）；
  「力扣」第 959 题：由斜杠划分区域（中等）；
  「力扣」第 1202 题：交换字符串中的元素（中等）；
  「力扣」第 947 题：移除最多的同行或同列石头（中等）；
  「力扣」第 721 题：账户合并（中等）；
  「力扣」第 803 题：打砖块（困难）；
  「力扣」第 1579 题：保证图可完全遍历（困难）;
  「力扣」第 778 题：水位上升的泳池中游泳（困难）。
  ```

`399. 除法求值` https://leetcode-cn.com/problems/evaluate-division/solution/chu-fa-qiu-zhi-by-leetcode-solution-8nxb/
- 方法一：广度优先搜索
- 方法二：Floyd 算法
- 方法三：带权并查集
