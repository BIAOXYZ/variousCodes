
# 2020.05.02

第 25 场双周赛 https://leetcode-cn.com/contest/biweekly-contest-25
- 5384. 拥有最多糖果的孩子 https://leetcode-cn.com/contest/biweekly-contest-25/problems/kids-with-the-greatest-number-of-candies/
- 5385. 改变一个整数能得到的最大差值 https://leetcode-cn.com/contest/biweekly-contest-25/problems/max-difference-you-can-get-from-changing-an-integer/
- 5386. 检查一个字符串是否可以打破另一个字符串 https://leetcode-cn.com/contest/biweekly-contest-25/problems/check-if-a-string-can-break-another-string/
- 5387. 每个人戴不同帽子的方案数 https://leetcode-cn.com/contest/biweekly-contest-25/problems/number-of-ways-to-wear-different-hats-to-each-other/

# 笔记

## (2)

第二题写的还是挺丑陋的，但是也是因为各种破情况比较多。
- 首次是注释掉的很长的那部分，最早的时候是想提高时间复杂度，一边遍历一边替换，但是因为python的字符串是immutable的原因，比较麻烦，遂作罢。
  * > 字符串的某个字符不能直接赋值修改：
    ```py
    s = 'HELLOWORLD'
    s[3] = 'a'
    --------------------------------------------------
    Traceback (most recent call last):
        File "Main.py", line 2, in <module>
            s[3] = 'a'
    TypeError: 'str' object does not support item assignment
    ```
  * > 后来在该帖子里（[间接修改Python字符串元素的三种方法](https://blog.csdn.net/songyunli1111/article/details/76932441)）发现其实可以先修改成一个新字符串，然后把新字符串**整体赋给**这个旧字符串是可以的。
    ```py
    s = 'HELLOWORLD'
    s1 = s[:3] + 'a' + s[4:]
    print "s is not changed:", s
    print "The new string s1 is:", s1
    s = s1
    print "But s can as a whole get value from s1 as:", s
    --------------------------------------------------
    s is not changed: HELLOWORLD
    The new string s1 is: HELaOWORLD
    But s can as a whole get value from s1 as: HELaOWORLD
    ```
    甚至用切片法的话可以直接给旧的赋值：
    ```py
    s = 'HELLOWORLD'
    s = s[:3] + 'a' + s[4:]
    print s
    --------------------------------------------------
    HELaOWORLD
    ```
- 然后大的思路很清晰：首先遍历找到需要被替换的数字，然后用str的replace方法直接替换，但是边缘情况比较多（并且叠加python的语言特性），导致看起来会有些费解。

>> 求最终的变换后的大数时，预期的主要分支是这个`big2 = big.replace(replacestr,'9')`。但是前面加那个if分支是因为，假如输入是9，replacestr就是空字符，我们试试看`把空字符换成'9'`会是啥情况：
```py
if replacestr == '':
    big2 = big
else:
    big2 = big.replace(replacestr,'9')
```
```py
num = 9
strform = str(num)
a = strform.replace('','9')
print strform
print a
--------------------------------------------------
9
999
```

>> 求小数的时候就更复杂了。预期的主要分支是这个`small2 = small.replace(replacestr,'0')`。
```py
if replacestr == '':
    replacestr = small[0]
    small2 = small.replace(replacestr,'1')
else:
    if replacefirst == False:
        small2 = small.replace(replacestr,'0')
    else:
        small2 = small.replace(replacestr,'1')
```
