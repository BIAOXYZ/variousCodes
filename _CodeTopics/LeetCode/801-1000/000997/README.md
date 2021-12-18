
`997. 找到小镇的法官` https://leetcode-cn.com/problems/find-the-town-judge/solution/zhao-dao-xiao-zhen-de-fa-guan-by-leetcod-0dcg/
- [ ] 方法一：计算各节点的入度和出度

```
2
[[1,2]]
3
[[1,3],[2,3]]
3
[[1,3],[2,3],[3,1]]
3
[[1,2],[2,3]]
4
[[1,3],[1,4],[2,3],[2,4],[4,3]]
```

# 语法点

## `000997.py`

原来 Python 的 `set` 也有 `.pop()` 方法，只不过因为是随机pop出元素，所以基本用不到而已。
