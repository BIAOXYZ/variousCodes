
# C

```c
#define MAX( a, b ) ((a) > (b) ? (a) : (b))
#define MIN( a, b ) ((a) < (b) ? (a) : (b))
```

C语言常用宏的使用小结 https://juejin.im/post/6844903950429192200
```c
// 5.返回数组元素的个数
#define ARRAY_SIZE(a) (sizeof((a)) / sizeof((a[0])))

// 15.求最大值
#define MAX2(a,b)  ((a) > (b) ? (a) : (b))
#define MAX3(a,b,c)  ((a) > (b) ? ((a) > (c) ? (a) : (c)) : ((b) > (c) ? (b) : (c)))
```

# Python2

```py
# 列表变频率字典（其实比赛的时候都是直接用 Counter）
def list_to_dict(lis):
    dic = {}
    for num in lis:
        if dic.has_key(num):
            dic[num] += 1
        else:
            dic[num] = 1
    return dic
def list_to_dic(lis):
    dic = {}
    for elem in lis:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1
    return dic
def list_to_dic_v2(lis):
    dic = {}
    for elem in lis:
        dic[elem] = dic.setdefault(elem, 0) + 1
    return dic
```

```py
# 官方bisect库主要是为了查找某个元素 x 如果要插入相应list的话的插入位置，但是其实不方便精准查找某个元素是否在list中。
# 官方文档页面搞了一个包装，但是只有查找最左位置的。在LC454里也写了最右位置的，详情参考那个题的笔记吧。
import bisect
def binary_search_leftmost_equal(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
def binary_search_rightmost_equal(arr, x):
    i = bisect.bisect_right(arr, x)
    if i < len(arr) + 1 and arr[i-1] == x:
        return i-1
    else:
        return -1
```

```py
# 倒序遍历数组 -- 分别以`range(length-1`、`range(-1`为关键词在仓库中搜索，能发现不少。比如`000066.py`、`000067_algo2.py`
# `000415.py`（字符串相加）、`000043.py`（字符串相乘）里面也涉及了倒序循环遍历，不过是分两段。
s = '123'
length = len(s)
for i in range(-1,-length-1,-1):
  print s[i]
for i in range(length-1,-1,-1):
  print s[i]
--------------------------------------------------
3
2
1
3
2
1
```

```py
# 遍历中删除

## `000283.py`用while循环，这里None当然也可以换成0，1之类的具体的某个值。
while None in nums:
    nums.pop(nums.index(None))
    
## 000026的README里三个链接，以及提交本身采用的倒序for循环删除。
##（注意，这里是因为数组是有序的，所以“==”后面是“nums[i-1]”。对于general的情况，把这里的“nums[i-1]”换成0，1之类的具体值即可。）
for i in range(len(nums)-1, 0, -1):
    if nums[i] == nums[i-1]:
        nums.pop(i)
```

```py
# 移除列表中所有值为 2 的元素 -- 周赛195
>>> l = [1,2,3,2,2,2,3,4]
>>> filter(lambda x: x != 2, l)
[1, 3, 3, 4]
```

```py
# 根据字典中的val获取相应的key -- 周赛191
def getKey(dic, val):
    return [k for k, v in dic.items() if v == val]
```

```py
# 最大公约数 -- 双周赛26
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b!=0:
        a, b = b, a%b
    return a

print gcd(9,3)
print gcd(18,24)
print gcd(5,0)
print gcd(0,4)
print gcd(0,0)
--------------------------------------------------
3
6
5
4
0
```

```console
# 各种列表推导式 

• 周赛181
• TLE--000621.py  // 增加了二维列表转一维列表
```
