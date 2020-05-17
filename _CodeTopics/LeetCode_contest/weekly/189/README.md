
# 2020.05.17

第 189 场周赛 https://leetcode-cn.com/contest/weekly-contest-189
- 5412. 在既定时间做作业的学生人数 https://leetcode-cn.com/contest/weekly-contest-189/problems/number-of-students-doing-homework-at-a-given-time/
- 5413. 重新排列句子中的单词 https://leetcode-cn.com/contest/weekly-contest-189/problems/rearrange-words-in-a-sentence/
- 5414. 收藏清单 https://leetcode-cn.com/contest/weekly-contest-189/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
- 5415. 圆形靶内的最大飞镖数量 https://leetcode-cn.com/contest/weekly-contest-189/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

# 笔记

## (2)

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
