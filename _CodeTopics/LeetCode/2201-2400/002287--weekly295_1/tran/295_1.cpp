class Counter {
public:
    unordered_map<char, int> _ctr;
    Counter(string s) {
        for (char ch : s) {
            if (_ctr.find(ch) != _ctr.end()) {
                _ctr[ch]++;
            } else {
                _ctr[ch] = 1;
            }
        }
    }
    ~Counter() = default;
};

class Solution {
public:
    int rearrangeCharacters(string s, string target) {

        // 第 295 场周赛第一题
        // https://leetcode.cn/submissions/detail/319295358/
        Counter ctr1 = Counter(s);
        Counter ctr2 = Counter(target);
        int res = INT_MAX;
        for (auto it = ctr2._ctr.begin(); it != ctr2._ctr.end(); ++it) {
            char key = it->first;
            res = min(res, ctr1._ctr[key] / ctr2._ctr[key]);
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/394928012/

执行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
6.2 MB
, 在所有 C++ 提交中击败了
34.83%
的用户
通过测试用例：
115 / 115
*/
