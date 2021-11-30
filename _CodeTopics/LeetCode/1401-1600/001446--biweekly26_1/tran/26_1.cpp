class Solution {
public:
    int maxPower(string s) {

        // 第 26 场双周赛第一题
        // https://leetcode-cn.com/submissions/detail/71312850/

        int maxenergy = 1;
        int length = s.size();
        for (int i = 0; i < length - 1; ++i) {
            int currenergy = 1;
            for (int j = i + 1; j < length; ++j) {
                if (s[j] == s[i]) {
                    currenergy += 1;
                    maxenergy = max(maxenergy, currenergy);
                } else {
                    break;
                }
            }
        }
        return maxenergy;
    }
};

/*
https://leetcode-cn.com/submissions/detail/244008655/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.7 MB, 在所有 C++ 提交中击败了22.74%的用户
通过测试用例：
333 / 333
*/
