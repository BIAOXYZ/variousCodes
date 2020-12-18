class Solution {
public:
    unordered_map<char, int> str_to_dic(string s) {
        unordered_map<char, int> dic;
        for (auto ch : s) {
            if (dic.find(ch) != dic.end()) {
                dic[ch]++;
            }
            else {
                dic[ch] = 1;
            }
        }
        return dic;
    }

    char findTheDifference(string s, string t) {
        unordered_map<char, int> dicS, dicT;
        dicS = str_to_dic(s);
        dicT = str_to_dic(t);
        // 使用for循环的范围遍历来代替，更简单且易读。
        for (auto kv : dicT) {
            if (dicS.find(kv.first) == dicS.end()) {
                return kv.first;
            }
            else if (kv.second > dicS[kv.first]) {
                return kv.first;
            }
        }
        return -1;
    }
};

/*
https://leetcode-cn.com/submissions/detail/131982203/

54 / 54 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 7.4 MB

执行用时：12 ms, 在所有 C++ 提交中击败了21.18%的用户
内存消耗：7.4 MB, 在所有 C++ 提交中击败了5.03%的用户
*/
/*
和上一版代码 `000389_impl.cpp` 唯一的区别就是第二个`auto`后面少了`&`——因为不打算在循环时更改对象的值，所以这两种方式没啥区别，符合预期。
*/
