#include <stdio.h>

int power(int m, int n);

/* 测试 power 函数 */
main()
{
    int i;

    for (i = 0; i < 10; ++i)
        printf("%d %d %d\n", i, power(2,i), power(-3,i));
    return 0;
}

/* power: 计算 base 的 n 次幂; n >= 0 */
int power(int base, int n)
{
    int i, p;

    p = 1;
    for (i = 1; i <= n; ++i)
        p = p * base;
    return p;
}


/* 本页说到"（标准库中提供了一个 pow(x,y)函数用于计算 x^y。）"，测试如下：*/
/*
#include<stdio.h>

main()
{
    int c;
    c = pow(2,10);
    printf("%d", c);
}
*/
