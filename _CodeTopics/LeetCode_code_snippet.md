
# python2

```py
# 倒序遍历数组 -- 分别以`range(length-1`、`range(-1`为关键词在仓库中搜索，能发现不少。比如`000066.py`、`000067_algo2.py`
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
    
## 000026的README里三个链接，以及提交本身采用的倒序for循环
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

