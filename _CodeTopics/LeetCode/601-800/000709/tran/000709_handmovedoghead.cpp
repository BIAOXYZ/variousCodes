#include <cctype>

class Solution {
public:
    string toLowerCase(string s) {
        for (char& ch : s) {
            ch = tolower(ch);
        }
        return s;
    }
};

/*
https://leetcode-cn.com/submissions/detail/247606536/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.1 MB, 在所有 C++ 提交中击败了7.59%的用户
通过测试用例：
114 / 114
*/
