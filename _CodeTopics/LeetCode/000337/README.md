
`337. 打家劫舍 III` https://leetcode-cn.com/problems/house-robber-iii/solution/da-jia-jie-she-iii-by-leetcode-solution/

# 笔记

## `000337.py`

如果没有第26行`dp_withnode[node] = dp_withoutnode[node] = 0`时的完整报错：
```py
KeyError: None
    dp_withnode[node] = dp_withoutnode[node.left] + dp_withoutnode[node.right]
Line 29 in dfs (Solution.py)
    dfs(node.left)
Line 27 in dfs (Solution.py)
    dfs(root)
Line 32 in rob (Solution.py)
    ret = Solution().rob(param_1)
Line 56 in _driver (Solution.py)
    _driver()
Line 68 in <module> (Solution.py)
```
