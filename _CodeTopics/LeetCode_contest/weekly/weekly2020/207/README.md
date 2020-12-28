
# 2020.09.20

第 207 场周赛 https://leetcode-cn.com/contest/weekly-contest-207
- 5519. 重新排列单词间的空格 https://leetcode-cn.com/contest/weekly-contest-207/problems/rearrange-spaces-between-words/
- 5520. 拆分字符串使唯一子字符串的数目最大 https://leetcode-cn.com/contest/weekly-contest-207/problems/split-a-string-into-the-max-number-of-unique-substrings/
- 5521. 矩阵的最大非负积 https://leetcode-cn.com/contest/weekly-contest-207/problems/maximum-non-negative-product-in-a-matrix/
- 5522. 连通两组点的最小成本 https://leetcode-cn.com/contest/weekly-contest-207/problems/minimum-cost-to-connect-two-groups-of-points/

# 笔记

## (2)

回溯完恢复状态的时候，想着用“新的”当前字符串“减去”这一次加上的部分，就等于“旧的”当前字符串了。也就是涉及两个字符串相减。然后好像没有类似的库函数，当时先灵机一动直接每次用个`tmp`变量把`currSubStr`存一下，然后恢复状态时再覆盖回去，但是实际直接这么写就完了：

```py
s1 = 'abcxy'
s2 = 'xy'

def stringsubtract(s1, s2):
  return s1[:len(s1)-len(s2)]

print stringsubtract(s1,s2)
--------------------------------------------------
abc
```

### （TODO）语法点：

[`207_2.py`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode_contest/weekly/207/207_2.py)里用了一个非常别扭/丑陋的做法，也就是第10行这句：`res = [1]`。按理说我是想让`res`在子函数里也能用，但是如果是普通变量（比如这里用`res = 1`）是不行的。如果是python3用`nonlocal`关键字应该可以，python2这种还不知道怎么办——除了这种定义成一个list然后取第一个变量的丑陋做法外。。。
