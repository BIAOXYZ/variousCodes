class Solution {
public:
    int countEven(int num) {
        
        // 第 281 场周赛第一题
        // https://leetcode.cn/submissions/detail/270589104/

        int res = 0;
        for (int i = 2; i < num + 1; ++i) {
            int sum = 0;
            string s = to_string(i);
            for (auto ch : s) {
                sum += ch - '0';
            }
            if (sum % 2 == 0) {
                res += 1;
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/393273765/

执行用时：
12 ms
, 在所有 C++ 提交中击败了
0.50%
的用户
内存消耗：
5.8 MB
, 在所有 C++ 提交中击败了
56.44%
的用户
通过测试用例：
71 / 71
*/
