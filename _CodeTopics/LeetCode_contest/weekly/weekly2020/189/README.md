
# 2020.05.17

第 189 场周赛 https://leetcode-cn.com/contest/weekly-contest-189
- 5412. 在既定时间做作业的学生人数 https://leetcode-cn.com/contest/weekly-contest-189/problems/number-of-students-doing-homework-at-a-given-time/
- 5413. 重新排列句子中的单词 https://leetcode-cn.com/contest/weekly-contest-189/problems/rearrange-words-in-a-sentence/
- 5414. 收藏清单 https://leetcode-cn.com/contest/weekly-contest-189/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
- 5415. 圆形靶内的最大飞镖数量 https://leetcode-cn.com/contest/weekly-contest-189/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

# 笔记

## (2)
// 这题真是阴，各种边界情况，我本地调了一阵以为各种都考虑到了，结果第一次还是TLE中招了。忽略了最后一个单词恰好只有一个字母的情况（比如"You and i"），导致陷入死循环。后面又改了一次才对。

Python 字符串大小写转换 https://www.runoob.com/python3/python3-upper-lower.html --> 贴完才发现是python3的，但是至少lower()和capitalize()两个方法对python2也适用。
```py
str1 = "HeLLo"
str1.lower()
str2 = str1.lower()
print "str1 is: ", str1
print "str2 is: ", str2

str3 = "World"
str3 = str3[0].lower() + str3[1:]
print "str3 is: ", str3

str5 = "TEST"
str5.capitalize()
str6 = str5.capitalize()
print "str5 is: ", str5
print "str6 is: ", str6
--------------------------------------------------
str1 is:  HeLLo
str2 is:  hello
str3 is:  world
str5 is:  TEST
str6 is:  Test
```

- Python sorted() 函数 https://www.runoob.com/python/python-func-sorted.html
- Python sorted() function https://www.programiz.com/python-programming/methods/built-in/sorted
- python的sorted函数对字典按key排序和按value排序 https://blog.csdn.net/tangtanghao511/article/details/47810729
- Python排序函数sort()和sorted()详解 https://blog.csdn.net/lyy14011305/article/details/76148512
```py
students = [('jane', 'B', 12), ('john', 'A', 15), ('dave', 'B', 10)]
print sorted(students, key=lambda s: s[2])
print sorted(students, key=lambda s: s[2], reverse=True)
print "But students list has not been changed: ", students

dic = {8:['leetcode'], 2:['is'], 4:['cool']}
print sorted(dic.keys())

a = [2, 1, 4, 9, 6]
a.sort()
print a
c = [2, 1, 4, 9, 6]
d = sorted(c)
print d
print c
--------------------------------------------------
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
But students list has not been changed:  [('jane', 'B', 12), ('john', 'A', 15), ('dave', 'B', 10)]
[2, 4, 8]
[1, 2, 4, 6, 9]
[1, 2, 4, 6, 9]
[2, 1, 4, 9, 6]
```
