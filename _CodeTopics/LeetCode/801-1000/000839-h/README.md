
`839. 相似字符串组` https://leetcode-cn.com/problems/similar-string-groups/solution/xiang-si-zi-fu-chuan-zu-by-leetcode-solu-8jt9/
- [x] 方法一：并查集

# 测试用例

```
["tars","rats","arts","star"]
["omv","ovm"]
["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]
```

# `WA--000839.py`

这个错误的原因是对某些输入来说，产生的组需要合并，但是根本就不会合并。。。

```console
输入：
["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]

最后形成的tmp：
['kccomwcgcs', 'kgcomwcccs']
['socgcmcwkc']
['sgckwcmcoc', 'sgmkwcccoc']
['coswcmcgkc', 'coswmccgkc']
['cowkccmsgc', 'kowcccmsgc']
['cosgmccwkc', 'coswmccgkc']
你会发现第四行和最后一行的两个list有个公共的元素 'coswmccgkc'，所以这俩其实算一个。但是`WA--000839.py`是不会合并它们的。
```
