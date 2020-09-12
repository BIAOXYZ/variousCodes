
# 2020-09-12 15:00

力扣杯 秋季编程大赛 LCCUP'20 https://leetcode-cn.com/contest/season/2020-fall/
```console
大赛规则
1. 个人赛于 2020-09-12 15:00 开赛，共计 5 题，比赛时长 150 分钟。
2. 个人赛于 2020-09-11 23:59 报名截止，逾期将无法报名参赛。
```

https://leetcode-cn.com/contest/season/2020-fall/ranking/solo/
- `1. 速算机器人` https://leetcode-cn.com/contest/season/2020-fall/problems/nGK0Fy/
- `2. 早餐组合` https://leetcode-cn.com/contest/season/2020-fall/problems/2vYnGI/
- `3. 秋叶收藏集` https://leetcode-cn.com/contest/season/2020-fall/problems/UlBDOe/
- `4. 快速公交` https://leetcode-cn.com/contest/season/2020-fall/problems/meChtZ/
- `5. 追逐游戏` https://leetcode-cn.com/contest/season/2020-fall/problems/Za25hA/

# 笔记

## (2)

比赛时TLE的一个和WA的两个无视吧，忘了最后除掉`1000000007`这个大模数了，低级错误。

### `2_impl.py`

这个相当于用了标准库`bisect`里的函数去做二分查找，但是最开始其实没彻底用对。参照下面官方文档里的描述就知道了：`bisect`里这些查找，返回的是“***如果要把目标元素插入数组，应该插入的位置的index***”，而不是我原来想的（也就是标准的提法）“***如果在数组里的话，返回数组里对应元素的index，否则返回-1***”。但是其实这个题用`bisect_right`正好。

`8.5. bisect — 数组二分查找算法` https://docs.python.org/zh-cn/2.7/library/bisect.html
- > bisect.bisect_left(a, x, lo=0, hi=len(a))
  * > 返回的插入点 i 可以将数组 a 分成两部分。左侧是 `all(val < x for val in a[lo:i])` ，右侧是 `all(val >= x for val in a[i:hi])` 。
- > bisect.bisect(a, x, lo=0, hi=len(a))
  * > 类似于 bisect_left()，但是返回的插入点是 a 中已存在元素 x 的右侧。
  * > 返回的插入点 i 可以将数组 a 分成两部分。左侧是 all(val <= x for val in a[lo:i])，右侧是 all(val > x for val in a[i:hi]) for the right side。

一个有趣的python排序模块：bisect https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html

```py
import bisect
l = [1,2,3,4,4,4,6,6,7]
print l

ind = bisect.bisect_right(l, 4)
print ind
ind = bisect.bisect_right(l, 5)
print ind
ind = bisect.bisect_right(l, 6)
print ind

ind1 = bisect.bisect_left(l, 4)
print ind1
ind1 = bisect.bisect_left(l, 5)
print ind1
ind1 = bisect.bisect_left(l, 6)
print ind1

ind2 = bisect.bisect(l, 4)
print ind2
ind2 = bisect.bisect(l, 5)
print ind2
ind2 = bisect.bisect(l, 6)
print ind2
--------------------------------------------------
[1, 2, 3, 4, 4, 4, 6, 6, 7]
6
6
8
3
6
6
6
6
8
```

### `2_impl2.py`

相当于自己实现了上面`bisect_right`的功能。其实就是在原来[`000704.py`](https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/000704/000704.py)的基础上改了下：***如果查找目标不在数组中***，直接返回最后的那个`left`（注意，此时`left`恰好比`right`多1，因为`right`刚移到`left`左边），符合该题要求；反之，***如果查找目标在数组中***，那么我们必须考虑有多个目标时，要返回最右边的那个的index，下面的写法也做了相应处理。

```py
def binary_search(arr, target):
    length = len(arr)
    left, right = 0, length - 1
    while left <= right:
        mid = (right + left) / 2
        print "left, right and mid is: ", left, right, mid
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            while arr[mid+1] == target:
                mid += 1
            return mid + 1
    return left
print binary_search([1,2,3,3,3,3,3,3,5],3)
print binary_search([1,2,3,3,3,3,3,3,5],4)
--------------------------------------------------
left, right and mid is:  0 8 4
8
left, right and mid is:  0 8 4
left, right and mid is:  5 8 6
left, right and mid is:  7 8 7
left, right and mid is:  8 8 8
8
```
