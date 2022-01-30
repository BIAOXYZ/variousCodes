class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        
        // 官方答案用到了 stringstream，特地手写一遍。
        // 先写不带任何优化的版本（传引用、move等全都不用），
        // 然后再写带优化的版本，并对比下时间。--> 这个已经是优化后的版本了，注释忘改了- -

        unordered_map<string, int> freq;

        std::function<void(const string&)> str_to_freq_dic = [&](const string& s) -> void {
            stringstream ss(s);
            string w;
            while (ss >> w) {
                ++freq[move(w)];
            }
        };
        str_to_freq_dic(s1);
        str_to_freq_dic(s2);
        
        vector<string> ans;
        for (const auto& [word, occurrence] : freq) {
            if (occurrence == 1) {
                // 这一处 move 还是我自己加的，答案里没加。。。
                ans.push_back(move(word));
            }
        }
        return ans;
    }
};

/*
https://leetcode-cn.com/submissions/detail/263761451/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.3 MB, 在所有 C++ 提交中击败了100.00%的用户
通过测试用例：55 / 55
*/
/*
我去，优化过后就是不一样，直接双百了。。。
*/
