class Solution {
public:
    bool checkPowersOfThree(int n) {

        // 第 47 场双周赛第二题
        // https://leetcode.cn/submissions/detail/151900755/

        while (n > 0) {
            int remainder = n % 3;
            if (remainder == 2) {
                return false;
            }
            n /= 3;
        }
        return true;
    }
};

/*
https://leetcode.cn/submissions/detail/388001448/

执行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
5.8 MB
, 在所有 C++ 提交中击败了
47.14%
的用户
通过测试用例：
129 / 129
*/
