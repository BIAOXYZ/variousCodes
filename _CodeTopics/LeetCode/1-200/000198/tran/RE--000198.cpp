class Solution {
public:
    int rob(vector<int>& nums) {

        // https://leetcode-cn.com/submissions/detail/106465470/
        int length = nums.size();
        if (length == 0)
            return 0;
        else if (length <= 2)
            return max(nums[0], nums[1]);
        
        vector<int> dp(length, 0);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        for (int i = 2; i < length; ++i)
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]);
        return dp[length-1];
    }
};

/*
执行出错
2 / 70 个通过的测试用例

=================================================================
==20==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6020000001b4 at pc 0x000000367505 bp 0x7fff37e86a90 sp 0x7fff37e86a88
READ of size 4 at 0x6020000001b4 thread T0
    #2 0x7f20e5989082  (/lib/x86_64-linux-gnu/libc.so.6+0x24082)
0x6020000001b4 is located 0 bytes to the right of 4-byte region [0x6020000001b0,0x6020000001b4)
allocated by thread T0 here:
    #6 0x7f20e5989082  (/lib/x86_64-linux-gnu/libc.so.6+0x24082)
Shadow bytes around the buggy address:
  0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c047fff8000: fa fa fd fa fa fa fd fa fa fa fd fa fa fa fd fa
  0x0c047fff8010: fa fa fd fd fa fa fd fd fa fa fd fa fa fa fd fa
  0x0c047fff8020: fa fa fd fa fa fa fd fa fa fa fd fd fa fa fd fa
=>0x0c047fff8030: fa fa fd fa fa fa[04]fa fa fa fa fa fa fa fa fa
  0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8070: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff8080: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
  Shadow gap:              cc
==20==ABORTING
*/
