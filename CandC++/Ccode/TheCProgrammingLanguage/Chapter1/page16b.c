#include <stdio.h>

/* ͳ���������ַ��ĸ������汾 1 */
main()
{
    long nc;

    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);
}
