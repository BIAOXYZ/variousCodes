class Solution {
public:
    int maxNumberOfBalloons(string text) {

        unordered_map<char, int> ctr = {};
        for (char ch : text) {
            ++ctr[ch];
        }
        // C++ 的 min() 函数只能有两个元素；如果用 min_element()，倒是能多个元素，
        //// 但是要求的参数是输入开始和结束的迭代器（一般都是vector的迭代器），比如下面的写法：
        //// *min_element(cnt.begin(), cnt.end());
        // 像本题这种就五个元素的情况，看起来既没有办法用 min() 参数填两个元素；
        //// 也没有办法用 *min_element() 里面的参数填上首尾的迭代器。。。
        //// 所以如果是过去碰到了，就只能是写 for 循环一个一个比了。。。
        // 今天偶然看到了可以用下面的方法来实现（其实原理应该也是用大括号把这五个元素搞成了vector）。
        return min({ctr['a'], ctr['b'], ctr['l']/2, ctr['n'], ctr['o']/2});
    }
};

/*
https://leetcode-cn.com/submissions/detail/267621855/

执行用时：4 ms, 在所有 C++ 提交中击败了58.68%的用户
内存消耗：6.5 MB, 在所有 C++ 提交中击败了49.31%的用户
通过测试用例：
25 / 25
*/
