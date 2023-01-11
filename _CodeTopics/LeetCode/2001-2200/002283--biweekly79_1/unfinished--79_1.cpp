
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

    ~Counter();
};

class Solution {
public:
    bool digitCount(string num) {

        // 第 79 场双周赛第一题
        // https://leetcode.cn/submissions/detail/319178335/

        int n = num.size();
        Counter myCtr = Counter(num);
        for (int i = 0; i < n; ++i) {
            char ch = num[i];
            char i_char;
            // 就下面这句，想把 int 1 转成 char '1'，一时查不到，凌晨3点半多了，累死我了。CNMCNMCNM！！！
            if (myCtr._ctr[std::sprintf(i_char, "%d", i)] != atoi(ch)) {
                return false;
            }
        }
        return true;
    }
};


/*
https://stackoverflow.com/questions/53055563/what-is-the-c-equivalent-of-python-collections-counter
*/
