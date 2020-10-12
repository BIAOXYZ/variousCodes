
`994. 腐烂的橘子` https://leetcode-cn.com/problems/rotting-oranges/solution/fu-lan-de-ju-zi-by-leetcode-solution/
- 方法一：枚举 + 广度优先搜索
  * > 无疑上面的方法需要枚举每个腐烂橘子，所以时间复杂度需要在原先广度优先搜索遍历的时间复杂度上再乘以腐烂橘子数，这在整个网格范围变大的时候十分耗时，所以需要另寻他路。
- [x] 方法二：多源广度优先搜索

# `WA--000994.py`

这个无视吧，我以为题目里的grid默认是正方形，还专门搞了个新函数`is_legal_coordinate_for_square()`，结果其实也可以是矩形。

# `WA2--000994.py`

修改完上面的失误后，用例就只有一个不过了（`302 / 303 `）。这个属于忽略了corner case，也比较简单。
