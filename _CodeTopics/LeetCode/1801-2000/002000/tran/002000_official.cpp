class Solution {
public:
    string reversePrefix(string word, char ch) {

        int ind = word.find(ch);
        if (ind != string::npos) {
            reverse(word.begin(), word.begin() + ind + 1);
        }
        return word;
    }
};

/*
https://leetcode-cn.com/submissions/detail/264304325/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.1 MB, 在所有 C++ 提交中击败了31.62%的用户
通过测试用例：
112 / 112
*/
