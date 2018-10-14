#include <stdio.h>

/* 将输入拷贝到输出; 版本 2 */
main()
{
    int c;

    while ((c = getchar()) != EOF)
        putchar(c);
}

/*
由于 != 的优先级高于 = ，这意味着如果没有圆括号，比较测试 != 会在赋值操作 = 之前完成。
因此语句c = getchar() != EOF  等价于 c = (getchar() != EOF)
其结果就是根据 getchar 的调用是否遇到文件结束而将变量 c 设置为 0 或 1，这并不是我们希
望达到的效果。
*/

/*
#include <stdio.h>
main()
{
    int c;
    while (c = getchar() != EOF)
        putchar(c);
}
*/
