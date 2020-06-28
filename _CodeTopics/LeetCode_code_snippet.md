
# python2

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

