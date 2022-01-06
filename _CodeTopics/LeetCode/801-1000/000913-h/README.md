
`913. 猫和老鼠` https://leetcode-cn.com/problems/cat-and-mouse/solution/mao-he-lao-shu-by-leetcode-solution-444x/
- [x] 方法一：动态规划

```
[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
[[1,3],[0],[3],[0,2]]
```

# `000913_like_official.py3`

这个和官方答案很类似，但是更想说的是，一般递归都是一个函数，这个函数在内部再调用自己（比如DFS）。第一次见这种两个函数（`get_result()` 和 `get_nex_result()`）互相调用来递归的——虽然严格意义来说 `get_nex_result()` 完全整合到 `get_result()` 内部。
