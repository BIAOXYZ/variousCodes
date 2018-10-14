#include <stdio.h>

/* 统计输入中字符的个数；版本 1 */
main()
{
    long nc;

    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);
}
