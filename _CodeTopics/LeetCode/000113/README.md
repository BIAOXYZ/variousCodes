
`113. 路径总和 II` https://leetcode-cn.com/problems/path-sum-ii/solution/lu-jing-zong-he-ii-by-leetcode-solution/
- [x] 方法一：深度优先搜索
- 方法二：广度优先搜索

# `RE--000113.py`

这题提交时一直以为是对的，因为在提交前就发现了自己代码中回溯时的一个问题：多pop了。下面是代码里的print开了以后看到的，注意倒数第二行和倒数第三行输出（也就是 `333 [5, 4, 11, 2]` 到 `222 [5, 4]`）。所以注释掉了代码中子函数`backtrack_dfs()`原来的最后两行（也就是 `#currSum -= node.val` 和 `#currArr.pop()`）。
```console
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22


IndexError: pop from empty list
    currArr.pop()
Line 30 in backtrack_dfs (Solution.py)
    backtrack_dfs(root, [], 0)
Line 39 in pathSum (Solution.py)
    ret = Solution().pathSum(param_1, param_2)
Line 70 in _driver (Solution.py)
    _driver()
Line 80 in <module> (Solution.py)


stdout
111 [5]
111 [5, 4]
111 [5, 4, 11]
111 [5, 4, 11, 7]
222 [5, 4, 11, 7]
111 [5, 4, 11, 2]
333 [5, 4, 11, 2]
222 [5, 4]
222 []
```

# `WA--000113.py`

```console
输入
[-2,null,-3]
-5

输出
[]

预期结果
[[-2,-3]]

stdout
111 [-2]
```
