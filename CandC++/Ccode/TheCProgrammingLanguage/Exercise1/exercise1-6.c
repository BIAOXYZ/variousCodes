/* 练习 1-6. 验证表达式 getchar() != EOF 的值是 0 还是 1. */


#include <stdio.h>
main()
{
    int c;
    if ( c = (getchar() != EOF) == 1)
        printf("(getchar() != EOF) = 1");
    else
        printf("(getchar() != EOF) = 0");
    return 0;
}


/*也可用如下不引入新变量c的代码实现*/

/*
#include <stdio.h>
main()
{
    if ( (getchar() != EOF) == 1)
        printf("The value of \"getchar() != EOF\" is 1.");
    else
        printf("The value of \"getchar() != EOF\" is 0.");
}
*/

/*
笔记：一是EOF=ctrl+z，必须换行后ctrl+z才行。二是这两个程序都可以接受多个字符为输入，但是只有第一个字符有效。
也就是你第一个输入了ctrl+z，后面无论输多少字符，结果都会是0了。
*/
