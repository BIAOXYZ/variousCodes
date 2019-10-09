
/*
https://leetcode.com/problems/power-of-three/

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true

Example 2:

Input: 0
Output: false

Example 3:

Input: 9
Output: true

Example 4:

Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
*/
/*
https://leetcode.com/submissions/detail/50171518/
*/

// 待补充：一套完整程序+简单的测试框架。

bool isPowerOfThree(int n) {    
    if (n == 1 || n == 3)
        return true;
    if (n == 0 || n == 2) 
        return false;
        
    for (; n > 3 && (n % 3 == 0) ; n = n/3)
        ;
    if (n == 3)
        return true;
    else 
        return false;
}
