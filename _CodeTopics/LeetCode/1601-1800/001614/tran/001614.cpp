class Solution {
public:
    int maxDepth(string s) {
        
        int currMaxDepth = 0;
        int currLeftBracket = 0;
        for (char ch : s) {
            if (ch == '(') {
                ++currLeftBracket;
                currMaxDepth = max(currMaxDepth, currLeftBracket);
            } else if (ch == ')') {
                --currLeftBracket;
            }
        }
        return currMaxDepth;
    }
};

/*
https://leetcode-cn.com/submissions/detail/255789618/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.1 MB, 在所有 C++ 提交中击败了70.64%的用户
通过测试用例：
167 / 167
*/
