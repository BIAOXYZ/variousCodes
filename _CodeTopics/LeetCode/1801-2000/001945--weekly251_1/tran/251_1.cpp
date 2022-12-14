class Solution {
public:
    int getLucky(string s, int k) {

        // 第 251 场周赛第一题
        // https://leetcode.cn/submissions/detail/199503647/

        int first = 0;
        for (auto ch : s) {
            int tmp = ch - 'a' + 1;
            if (tmp < 10) {
                first += tmp;
            } else {
                first += tmp % 10 + tmp / 10;
            }
        }
        if (k == 1) {
            return first;
        }

        int res = 0;
        while (k > 1) {
            k--;
            while (first > 0) {
                res += first % 10;
                first /= 10;
            }
            if (k == 1) {
                return res;
            } else {
                first = res;
                res = 0;
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/389169865/

执行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
5.9 MB
, 在所有 C++ 提交中击败了
96.04%
的用户
通过测试用例：
216 / 216
*/
