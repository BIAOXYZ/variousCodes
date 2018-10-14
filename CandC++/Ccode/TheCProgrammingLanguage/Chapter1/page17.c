#include <stdio.h>

/* 统计输入字符的个数；版本2 */
main()
{
    double nc;

    for (nc = 0; getchar() != EOF; ++nc)
        ;
    printf("%.0f\n", nc);
}
