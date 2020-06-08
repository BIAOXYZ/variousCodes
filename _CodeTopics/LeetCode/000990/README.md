
# 1.

第四次错（`WA--000990_4.py`）后调试，终于发现我算法本身有漏洞。
```
输入: ["a!=b","b!=c","c!=a"]
输出 false
预期结果 true

djs changed in 2 is:  {u'a': u'a', u'!a': u'b', u'!b': u'a', u'b': u'b'}
djs changed in 2 is:  {u'a': u'a', u'!a': u'b', u'!c': u'b', u'!b': u'a', u'c': u'a', u'b': u'b'}
djs changed in 2 is:  {u'a': u'a', u'!a': u'a', u'!c': u'a', u'!b': u'a', u'c': u'a', u'b': u'a'}
```
错误的原因在于：按我的算法，只要`a!=b`，就会往字典djs里插入`"!a":"b"`，也就是意味着`!a等于b`（后来又来个`!c等于b`，那就意味着`!a等于!c, a等于c`，然后就会和最后一个`c!=a`矛盾，导致输出false。但其实a、b、c分别取1、2、3，明显应该是true）。错的根源在于把字母的取值区间限定在了0，1。但实际并不是这样。

# 2.

- `000990_algo2.py`里`union`函数else分支那里比较大小后再决定谁当father其实也可以省略，不影响。但是某些更复杂的场景可以提高效率。
- [官方答案](https://leetcode-cn.com/problems/satisfiability-of-equality-equations/solution/deng-shi-fang-cheng-de-ke-man-zu-xing-by-leetcode-/)里是直接在Solution类下定义了一个`class UnionFind:`，这样每次find和union的时候就不用多一个参数了（因为`self.parent`直接可以用）。我感觉应该是我写的还不熟，标准的并查集算法的两个函数find和union一般都是一个参数。
- 其实可以把那个字典定义成全局变量（或者至少find和union都可见的范围）即可——`000990_algo2_2.py`就是这样把两个函数的参数个数都变为了一个。
