class Solution {
public:
    bool squareIsWhite(string coordinates) {

        // 手动狗头题
        return ((coordinates[1] - '0') + (coordinates[0] - 'a' + 1)) % 2 == 1;
    }
};

/*
https://leetcode.cn/submissions/detail/387773556/

行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
5.7 MB
, 在所有 C++ 提交中击败了
66.33%
的用户
通过测试用例：
64 / 64
*/
