#include <stdio.h>

/* 统计数字、空白符和其它字符的个数 */
main()
{
    int c, i, nwhite, nother;
    int ndigit[10];

    nwhite = nother = 0;
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0;

    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9')
            ++ndigit[c-'0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;

    printf("digits =");
    for (i = 0; i < 10; ++i)
        printf(" %d", ndigit[i]);
    printf(", white space = %d, other = %d\n",
        nwhite, nother);
}

/* PS: 在cmd中粘贴需要右键命令提示符窗口的标题栏，然后选择"编辑"-"粘贴"
（http://jingyan.baidu.com/article/93f9803fd3a4dde0e46f55f5.html） */
