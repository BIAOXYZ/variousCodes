
# 中国时间：2022-06-11 22:30

第 80 场双周赛 https://leetcode.cn/contest/biweekly-contest-80
- 6095. 强密码检验器 II https://leetcode.cn/contest/biweekly-contest-80/problems/strong-password-checker-ii/
- 6096. 咒语和药水的成功对数 https://leetcode.cn/contest/biweekly-contest-80/problems/successful-pairs-of-spells-and-potions/
- 6097. 替换字符后匹配 https://leetcode.cn/contest/biweekly-contest-80/problems/match-substring-after-replacement/
- 6098. 统计得分小于 K 的子数组数目 https://leetcode.cn/contest/biweekly-contest-80/problems/count-subarrays-with-score-less-than-k/

# 其他

终于第一次AC（全国排名：`429 / 3949`，全球排名：`981 / 21910`）！此外，前三题用的 Python2；第四题想试试前缀和的板子，为了用 `itertools.accumulate()`，用了 Python3。

有点突然，因为第二题稍有点不顺（代码写得挺顺，但是低级错误把 `cur * potions[mid]` 写成了 `cur * spells[mid]`，并且一时没看出来，还本地debug单步调试了下才发现的），本没有想到能全做完的。第三题也不是第一眼就有思路那种。并且这次第三题也是 `Hard`（但是相应的第三题和第四题都算相对简单的 `Hard`，也就是 `Hard-`？因为都是 6 分），按理说两道 `Hard` 更不好搞的。但是没想到后面三、四两题想出来思路后写完都没问题。所以不但是首次AC，而且是首次四题均无 BUG 的情况下 AC（并且是不到一个小时就 AC）。打算把四个题的用例都记一下，顺便排名也截个图，小纪念一把～

昨天，是我最近这段时间里最倒霉的一天了吧：微软和Hulu同时挂，我真是服了。。。微软两次都是面完aa面然后挂了，早干嘛去了，浪费了我好多时间。。。第一次面 WebXT 题做得不太好我也不说啥了（这里面真的既有手风不顺的问题，也有面试官的锅）；第二次面 Azure 就三面差了一点点，没 bug free，结果还是挂（那干嘛不早点挂了我，还继续后面的流程干啥）。。。希望这次AC，是时来运转的开始！！！

# (1)

```
"IloveLe3tcode!"
"Me+You--IsMyDream"
"1aB!"
"aA12345678!!"
```

# (2)

```
[5,1,3]
[1,2,3,4,5]
7
[3,1,2]
[8,5,8]
16
```

# (3)

```
"fool3e7bar"
"leet"
[["e","3"],["t","7"],["t","8"]]
"fooleetbar"
"f00l"
[["o","0"]]
"Fool33tbaR"
"leetd"
[["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
```

# (4)

```
[2,1,4,3,5]
10
[1,1,1]
5
```
