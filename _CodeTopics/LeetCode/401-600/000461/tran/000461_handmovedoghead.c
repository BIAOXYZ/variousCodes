int hammingDistance(int x, int y){
    // C++（或C）手动狗头题——Python的这个统计1的个数的函数还真不知道。。。
    return __builtin_popcount(x ^ y);
}

/*
https://leetcode-cn.com/submissions/detail/181183093/

149 / 149 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 5.5 MB

执行用时：0 ms, 在所有 C 提交中击败了100.00%的用户
内存消耗：5.5 MB, 在所有 C 提交中击败了10.00%的用户
*/
