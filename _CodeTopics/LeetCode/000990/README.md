
第四次错（WA--000990_4.py）后调试，终于发现我算法本身有漏洞。
```
输入: ["a!=b","b!=c","c!=a"]
输出 false
预期结果 true

djs changed in 2 is:  {u'a': u'a', u'!a': u'b', u'!b': u'a', u'b': u'b'}
djs changed in 2 is:  {u'a': u'a', u'!a': u'b', u'!c': u'b', u'!b': u'a', u'c': u'a', u'b': u'b'}
djs changed in 2 is:  {u'a': u'a', u'!a': u'a', u'!c': u'a', u'!b': u'a', u'c': u'a', u'b': u'a'}
```
错误的原因在于：按我的算法，只要`a!=b`，就会往字典djs里插入`"!a":"b"`，也就是意味着`!a等于b`（后来又来个`!c等于b`，那就意味着`!a等于!c, a等于c`，然后就会和最后一个`c!=a`矛盾，导致输出false。但其实a、b、c分别取1、2、3，明显应该是true）。错的根源在于把字母的取值区间限定在了0，1。但实际并不是这样。
