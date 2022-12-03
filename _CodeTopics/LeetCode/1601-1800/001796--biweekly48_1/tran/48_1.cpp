class Solution {
public:
    int secondHighest(string s) {

        // 第 48 场双周赛第一题
        // https://leetcode.cn/submissions/detail/157679832/

        vector<int> stk(10, 0);
        for (char ch : s) {
            if (isdigit(ch)) {
                // 也可以用： stk[ch-48] = 1;
                stk[ch-'0'] = 1;
            }
        }

        bool flag = false;
        for (int i = 9; i > -1; --i) {
            if (stk[i] > 0) {
                if (!flag) {
                    flag = true;
                } else {
                    return i;
                }
            }
        }
        return -1;
    }
};

/*
https://leetcode.cn/submissions/detail/386802962/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
65.94%
的用户
内存消耗：
6.6 MB
, 在所有 C++ 提交中击败了
62.86%
的用户
通过测试用例：
301 / 301
*/
