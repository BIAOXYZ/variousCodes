
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

这个相当于二分查找用了``

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
