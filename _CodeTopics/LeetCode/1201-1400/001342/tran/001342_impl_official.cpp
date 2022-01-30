class Solution {
public:
    int numberOfSteps(int num) {

        int ans = 0;
        while (num) {
            // 官方答案用的是 `0x01`：
            // ret += (num > 1 ? 1 : 0) + (num & 0x01);
            // 我感觉直接就用 1 也没问题吧？
            ans += (num > 1 ? 1 : 0) + (num & 1);
            num >>= 1;
        }
        return ans;
    }
};

/*
https://leetcode-cn.com/submissions/detail/263853116/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了35.62%的用户
通过测试用例：204 / 204
*/
