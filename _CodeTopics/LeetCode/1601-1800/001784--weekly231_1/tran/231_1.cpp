class Solution {
public:
    bool checkOnesSegment(string s) {

        // 第 231 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/151989679/

        bool flagZero = false;
        for (int i = 1; i < s.size(); ++i) {
            if (!flagZero && s[i] == '0') {
                flagZero = true;
            }
            if (flagZero && s[i] == '1') {
                return false;
            }
        }
        return true;
    }
};

/*
https://leetcode.cn/submissions/detail/369397150/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
17.44%
的用户
内存消耗：
6.1 MB
, 在所有 C++ 提交中击败了
18.22%
的用户
通过测试用例：
191 / 191
*/
