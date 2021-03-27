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
        // for (auto it = dic.begin(); it != dic.end(); ++it) {
        //     if (it->second % 2 == 0) {
        //         res += it->second;
        //     } else {
        //         flag = true;
        //         res += it->second - 1;
        //     }
        // }
        */
        /*
        1. 参照上面注释掉的代码块，这里的 pr 和上面的 it 类型就不一样：it是指针，所以访问成员时用 ->；pr 是引用，所以用点号。
        2. 这里当然也可以用 for (auto &pr : dic)，但是我发现如果用 for (std::pair<char, int> &pr : dic)，也就是
           少了 const，也是不行的。。。
        */
        for (std::pair<const char, int> &pr : dic) {
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
https://leetcode-cn.com/submissions/detail/160686620/

95 / 95 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 6.4 MB

执行用时：4 ms, 在所有 C++ 提交中击败了65.64%的用户
内存消耗：6.4 MB, 在所有 C++ 提交中击败了86.27%的用户
*/
