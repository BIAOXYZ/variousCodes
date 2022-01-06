
`913. 猫和老鼠` https://leetcode-cn.com/problems/cat-and-mouse/solution/mao-he-lao-shu-by-leetcode-solution-444x/
- [x] 方法一：动态规划
  * > **结语**
    + > 上述方法为自顶向下的动态规划，也称记忆化搜索。这道题也可以使用自底向上的方法求解，从必胜状态与必败状态开始计算初始状态对应的游戏结果，可以通过广度优先搜索或者拓扑排序实现。感兴趣的读者可以自行尝试。

【代码界的小白】3种方法？揭秘猫鼠大战谁赢了！ https://leetcode-cn.com/problems/cat-and-mouse/solution/dai-ma-jie-de-xiao-bai-3chong-fang-fa-ji-ldjw/

```
[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
[[1,3],[0],[3],[0,2]]
```

# `000913_like_official.py3`

这个和官方答案很类似，但是更想说的是，一般递归都是一个函数，这个函数在内部再调用自己（比如DFS）。第一次见这种两个函数（`get_result()` 和 `get_nex_result()`）互相调用来递归的——虽然严格意义来说 `get_nex_result()` 完全整合到 `get_result()` 内部。
