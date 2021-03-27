class Solution {
public:
    int longestPalindrome(string s) {

        unordered_map<char, int> dic;
        for (char ch : s) {
            if (dic.find(ch) != dic.end()) {
                dic[ch]++;
            } else {
                dic[ch] = 1;
            }
        }

        int res = 0;
        bool flag = false;
        /*
        - 这里当然也可以用 for (auto &pr : dic)，但是我发现如果用 for (std::pair<char, int> &pr : dic)，
          也就是少了 const，也是不行的。。。
        - 但是我如果去掉引用符号 &，那么就可以不带 const 了（当然带上 const 也没问题）。
        */
        for (std::pair<char, int> pr : dic) {
            if (pr.second % 2 == 0) {
                res += pr.second;
            } else {
                flag = true;
                res += pr.second - 1;
            }
        }

        if (!flag) {
            return res;
        } else {
            return res + 1;
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/160689487/

95 / 95 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 6.5 MB

执行用时：4 ms, 在所有 C++ 提交中击败了65.64%的用户
内存消耗：6.5 MB, 在所有 C++ 提交中击败了68.28%的用户
*/
