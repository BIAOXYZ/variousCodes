
`911. 在线选举` https://leetcode-cn.com/problems/online-election/solution/zai-xian-xuan-ju-by-leetcode-solution-4835/
- [x] 方法一：预计算 + 二分查找

```
["TopVotedCandidate","q","q","q","q","q","q"]
[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
```

# 语法点

从这题里悟到了为啥 `bisect.bisect()` 默认要用 `bisect.bisect_right()` 而不是 `bisect.bisect_left()`。因为这题要求是：
- 如果待搜索元素在列表里，则返回待搜索元素的index。
- 如果待搜索元素不在列表里，则返回小于且离待搜索元素最近的元素的index。

更详细的举例说明：令 `l = [0,5,10,15,20,25,30]` 为待搜索列表。根据题意，当搜索 `3` 时，希望返回 `ind = 0`；当搜索 `5` 时，希望返回 `ind = 1`。
- 如果用 `bisect.bisect_left()`，不论搜索 `3` 还是 `5`，总是返回 `ind = 1`，没法处理了。
- 但是如果用 `bisect.bisect_right()`，当搜索 `3` 时，返回 `ind = 1`；当搜索 `5` 时，返回 `ind = 2`。只要统一用 `ind - 1` 即可。
```py
>>> import bisect
>>> l = [0,5,10,15,20,25,30]
>>> bisect.bisect_left(l,3)
1
>>> bisect.bisect_left(l,5)
1
>>> 
>>> bisect.bisect(l,3)
1
>>> bisect.bisect(l,5)
2
>>> 
```
