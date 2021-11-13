
# 中国时间：2021-11-13 22:30

第 65 场双周赛 https://leetcode-cn.com/contest/biweekly-contest-65
- 5910. 检查两个字符串是否几乎相等 https://leetcode-cn.com/contest/biweekly-contest-65/problems/check-whether-two-strings-are-almost-equivalent/
- 5911. 模拟行走机器人 II https://leetcode-cn.com/contest/biweekly-contest-65/problems/walking-robot-simulation-ii/
- 5912. 每一个查询的最大美丽值 https://leetcode-cn.com/contest/biweekly-contest-65/problems/most-beautiful-item-for-each-query/
- 5913. 你可以安排的最多任务数目 https://leetcode-cn.com/contest/biweekly-contest-65/problems/maximum-number-of-tasks-you-can-assign/

# (1)

python3----输出所有大小写字母及数字 https://www.cnblogs.com/jonm/p/8448118.html
- > 1.用一行输出所有大（小）写字母，以及数字
  ```py
  print([chr(i) for i in range(65, 91)])  # 所有大写字母
  print([chr(i) for i in range(97, 123)])  # 所有小写字母
  print([chr(i) for i in range(48, 58)])   # 所有数字
  ####################
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  ```
  ```py
  import string   # 导入string这个模块
  print(string.digits)  # 输出包含数字0~9的字符串
  print(string.ascii_letters)  # 包含所有字母(大写或小写)的字符串
  print(string.ascii_lowercase)  # 包含所有小写字母的字符串
  print(string.ascii_uppercase)  # 包含所有大写字母的字符串
  ##############
  0123456789
  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
  abcdefghijklmnopqrstuvwxyz
  ABCDEFGHIJKLMNOPQRSTUVWXYZ
  ```

# (2)

干TM的第二题，连错两次，第三次没有提示错误用例（这也不是季赛啊，搞那么严肃干吗），想不到哪错了。关键这题浪费太多时间，导致第三题没时间写了。

# (3)

```
[[1,2],[3,2],[2,4],[5,6],[3,5]]
[1,2,3,4,5,6]
[[1,2],[1,2],[1,3],[1,4]]
[1]
[[10,1000]]
[5]

[[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]
```
