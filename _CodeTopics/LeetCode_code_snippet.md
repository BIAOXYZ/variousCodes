
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

# C++

```

```

# Python3

```py
# https://github.com/BIAOXYZ/variousCodes/blob/master/_CodeTopics/LeetCode/2001-2200/002038/002038.py3
# 输入一个字符串 s 和字符 ch，输出 s 内所有的全部为 ch 的子串位置和长度。 s = "AAABABB", ch = 'A' 时，输出 {0: 3, 4: 1}
def get_start_pos_and_len(s, ch):
    dic = {}
    state = [False, -1, -1]
    for i in range(len(s)):
        if s[i] == ch:
            if not state[0]:
                state = [True, i, 1]
            else:
                state[2] += 1
        else:
            if not state[0]:
                continue
            else:
                dic[state[1]] = state[2]
                state = [False, -1, -1]
    if state[0]:
        dic[state[1]] = state[2]
    return dic
```

```py
# 获取所有小写字母
alphabeta = [chr(i) for i in range(ord('a'), ord('z')+1)]
print(alphabeta)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

```py
# `LC1332. 删除回文子序列` 里还有等价的 C++ 和 C 版本。

def is_palindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def is_palindrome_v2(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
    return True
```

```py
# 前缀和
# from：https://gist.github.com/WhiteRobe/a27fae02a337a8391533155bad0f535c

class PreSum:  # 标准前缀和模板
    def __init__(self, data):
        self.s = list(accumulate(data))
        self.data = data

    def query(self, i, j):  # 查询的是双闭区间[i, j]的区间和
        assert 0 <= i <= j < len(self.data)
        return self.s[j] - self.s[i] + self.data[i]

# 如果用 accumulate() 计算前缀和，参数 initial 带不带其实挺关键的（不只是影响前缀和数组每个元素的值，更主要是元素个数）
from itertools import accumulate
nums = [1,2,3]
prefixSum1 = list(accumulate(nums))
print("prefixSum1:", prefixSum1)   # prefixSum1: [1, 3, 6]
prefixSum2 = list(accumulate(nums, initial=0))
print("prefixSum2:", prefixSum2)   # prefixSum2: [0, 1, 3, 6]

# https://stackoverflow.com/questions/32925418/incremental-sum-a-list-of-numbers-in-python-2-7/32925755#32925755
# 上面的帖子里也提到了类似下面的一行写法，但是我怀疑可能python不会自己“缓存”，所以复杂度可能是 O(n^2) 的，一般还是别用吧。。。
>>> nums = [1,2,3,4,5]
>>> prefixSum = [sum(nums[:i]) for i in range(1, len(nums)+1)]
>>> prefixSum
[1, 3, 6, 10, 15]
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
def list_to_dic_v3(lis):
    dic = {}
    for elem in lis:
        dic[elem] = dic.get(elem, 0) + 1
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

## `000030.py3` 字典遍历中删除key
### Python字典遍历删除特定值 https://blog.csdn.net/zhangyuexiang123/article/details/101581035
for k in list(diff.keys()):
    if diff[k] == 0:
        diff.pop(k)
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
