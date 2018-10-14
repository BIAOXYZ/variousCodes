/* 练习 1-16. 对 longest-line 程序的 main 函数进行修改，使之能够处理任意长度的输入行，
以及尽可能多的输入文本。 */

#include<stdio.h>

int main()
{
    int c;
    while ( (c = getchar()) != EOF ){
        putchar(c);
    }
}
