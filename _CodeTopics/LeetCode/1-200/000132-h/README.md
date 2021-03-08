
`132. 分割回文串 II` https://leetcode-cn.com/problems/palindrome-partitioning-ii/solution/fen-ge-hui-wen-chuan-ii-by-leetcode-solu-norx/
- [x] 方法一：动态规划

# 测试用例

```
"aab"
"a"
"ab"
"x"
"xx"
"xxx"
"xxxx"
"aabc"
"cabababcbc"
```

# `WA--000132.py` and `000132.py`

这俩的差距就是第一次dp的时候第一个for循环，我的是正序，答案是倒序。但是我的有用例过不去，对错误用例 `"cabababcbc"` 来说，第一重dp完成后 `print dp` 的结果分别如下：
```console
我的：
[[True, False, False, False, False, False, False, True, False, True], 
 [True, True, False, True, False, True, False, False, False, False], 
 [True, True, True, False, True, False, True, False, True, False], 
 [True, True, True, True, False, True, False, False, False, False], 
 [True, True, True, True, True, False, True, False, True, False], 
 [True, True, True, True, True, True, False, False, False, False], 
 [True, True, True, True, True, True, True, False, True, False], 
 [True, True, True, True, True, True, True, True, False, True], 
 [True, True, True, True, True, True, True, True, True, False], 
 [True, True, True, True, True, True, True, True, True, True]
]

答案的：
[[True, False, False, False, False, False, False, False, False, False], 
 [True, True, False, True, False, True, False, False, False, False], 
 [True, True, True, False, True, False, True, False, False, False], 
 [True, True, True, True, False, True, False, False, False, False], 
 [True, True, True, True, True, False, True, False, False, False], 
 [True, True, True, True, True, True, False, False, False, False], 
 [True, True, True, True, True, True, True, False, True, False], 
 [True, True, True, True, True, True, True, True, False, True], 
 [True, True, True, True, True, True, True, True, True, False], 
 [True, True, True, True, True, True, True, True, True, True]
]
```

想了想确实***第一层for循环必须用倒序***，原因如下：假定字符串是`"abcdef"`。

如果第一重for循环是正序，那么我们看下过程：
- 首先是`a`开头的子串的回文性：长度为1的`a` 和长度为2的 `ab` 都不依赖dp已有的格子，可以靠默认值或直接计算来解决。
- 但是`abc`（对应的dp格子为`dp[0][2]`，也就是对应子串`s[0,...,2]`————注意这里不是冒号，而是`...`，也就是其实表示***左闭右闭***）需要依赖其他格子。具体来说，需要依赖`dp[0+1][2-1] = dp[1][1]`。可是如果是正序遍历这些被依赖的格子还没计算呢。
- 更明显的例子是这样的：如果你想用dp的方式计算`abcd`的回文性，那么你得知道除去开头和末尾的两个字母后的子串`bc`的回文性，但是`bc`是以`b`开头的，这时候还没算呢。

反之，倒序遍历就不会有这个问题。
- 首先是`f`开头的子串，就一个字母所以不用算；
- 然后是`e`开头的子串，一个长度为1的不用算，一个长度为2的不依赖别的直接判断。
- 对于后面遍历到的任何子串`s[i,...,j]`，由于是倒序遍历计算，此时`s[i+1, ..., j-1]`肯定已经被计算过并存到dp数组里了，也就是其依赖的dp格子有了。所以可以正确计算。
