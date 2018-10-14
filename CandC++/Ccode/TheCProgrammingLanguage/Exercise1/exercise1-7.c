/* 练习 1-7. 写一个程序，将 EOF 的值打印出来。*/

// /*
#include <stdio.h>

main()
{
    /* 这里之所以是4而不是5，是因为在while里"c = getchar()"这句已经被执行一次了。可以使用测试输入实验。
    如果是5的话，会发现依次输入"1回车2回车3回车4回车5回车6回车"才会提示次数超过并自动返回。*/
    int upperRunTime = 4;

    int realRunTime = 1;
    int c;

    while ( (c = getchar()) != EOF )
    {
        if (realRunTime <= upperRunTime)
        {
            c = getchar();
            realRunTime++;
        }
        else
        {
            printf("Poor guy! You've tried more than 5 times. Please stop!");
            return 0;  //这里曾试过用"break;"或是"exit(0);"，但似乎都不太好。
        }
    }

    printf("The value of EOF is %d", c);

    return 0;
}

// */

/* 第二个程序比较简单，不限制可以尝试的次数。 */

/*
#include <stdio.h>

main()
{
    int c;

    while ( (c=getchar()) != EOF )
    {
        c=getchar();
    }
    printf("EOF=%d",c);
}
*/

/*下面这个是网上（http://bbs.chinaunix.net/thread-836784-1-1.html）的例子。
可见EOF已经被定义，可以直接用。*/

/*
#include <stdio.h>
int main(int argc,char *argv[])
{
        printf("%d\n",EOF);
        return 0;
}
*/
