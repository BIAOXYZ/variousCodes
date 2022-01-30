class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        
        // 官方答案用到了 stringstream，特地手写一遍。
        // 先写不带任何优化的版本（传引用、move等全都不用），
        // 然后再写带优化的版本，并对比下时间。

        unordered_map<string, int> freq;

        std::function<void(string)> str_to_freq_dic = [&](string s) -> void {
            stringstream ss(s);
            string w;
            while (ss >> w) {
                ++freq[w];
            }
        };
        str_to_freq_dic(s1);
        str_to_freq_dic(s2);
        
        vector<string> ans;
        for (auto [word, occurrence] : freq) {
            if (occurrence == 1) {
                ans.push_back(word);
            }
        }
        return ans;
    }
};

/*
https://leetcode-cn.com/submissions/detail/263758027/

执行用时：4 ms, 在所有 C++ 提交中击败了53.15%的用户
内存消耗：6.5 MB, 在所有 C++ 提交中击败了80.19%的用户
通过测试用例：55 / 55
*/
