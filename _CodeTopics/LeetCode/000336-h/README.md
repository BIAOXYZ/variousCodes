
`336. 回文对` https://leetcode-cn.com/problems/palindrome-pairs/solution/hui-wen-dui-by-leetcode-solution/
- 方法一：枚举前缀和后缀
  * 字典树存储方式
  * [x] 哈希表存储方式

# 笔记

## `deliberate-TLE--000336.py`

这个里面的函数`isPalindrome()`里面那句`while left < right:`确实是有没有等号都一样的，虽然也很容易分析，但是还是记一下吧。
```py
s1 = 'abcba'
s2 = 'abba'
s3 = 'abcbx'
s4 = 'abxa'

def isPalindrome_no_equal(s):
    length = len(s)
    left, right = 0, length-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print isPalindrome_no_equal(s1)
print isPalindrome_no_equal(s2)
print isPalindrome_no_equal(s3)
print isPalindrome_no_equal(s4)

def isPalindrome_has_equal(s):
    length = len(s)
    left, right = 0, length-1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print isPalindrome_has_equal(s1)
print isPalindrome_has_equal(s2)
print isPalindrome_has_equal(s3)
print isPalindrome_has_equal(s4)
--------------------------------------------------
True
True
False
False
True
True
False
False
```

## `000336_algo2.py`

语法点：
```py
words = ["abcd","dcba","lls","s","sssll"]
indices = {word[::-1]: i for i, word in enumerate(words)}
print indices

word = 'xyz'
print word[::-1]
--------------------------------------------------
{'dcba': 0, 'abcd': 1, 's': 3, 'llsss': 4, 'sll': 2}
zyx
```

# 其他链接

老司机开车，教会女朋友什么是「马拉车算法」 https://www.cxyxiaowu.com/2665.html

一文让你彻底明白马拉车算法 - windliang的文章 - 知乎 https://zhuanlan.zhihu.com/p/70532099
