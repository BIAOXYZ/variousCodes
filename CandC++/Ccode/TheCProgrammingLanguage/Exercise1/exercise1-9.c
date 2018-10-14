/* 练习 1-9. 写一个程序，将输入拷贝到输出，并且将输入中连续的多个空格替换为单个空格。*/


/*
思路：碰到非空格直接输出，并进入OUTSPACE状态；碰到空格分情况讨论。
1.一旦遇到非空格，就立刻输出这个非空格的字符，并进入OUTSPACE状态。
2.如果是在OUTSPACE状态下碰到空格（也就是从字符出来后的第一个空格），就输出这个空格，
  同时标示进入了一个INSPACE的状态。
3.如果是在INSPACE状态下碰到空格（也就是至少是第二个空格了），就什么也不做。
*/

// /*
#include <stdio.h>

# define OUTSPACE 0
# define INSPACE 1

int main()
{
    int c;
    int state = OUTSPACE; // 如果这里改成INSPACE会怎样？————在第一个非空格字符之前出现的所以空格都无法显示，也就是不可能出现空格在开头（一定是非空格开头）

    while ( (c = getchar()) != EOF ){
        if (c != ' '){
            putchar(c);
            state = OUTSPACE;
        }
        else if (c == ' ' && state == OUTSPACE){
            putchar(c);
            state = INSPACE;
        }
        else if (c == ' ' && state == INSPACE){
            ;
        }
    }
    return 0;
}
// */

/* 简化版程序如下：写的时候就意识到了，上面程序中第二个else if完全多余，
因为那个分支反正不做任何事情。*/

/*
#include <stdio.h>

# define OUTSPACE 0
# define INSPACE 1

int main()
{
    int c;
    int state = OUTSPACE;

    while ( (c = getchar()) != EOF ){
        if (c != ' '){
            putchar(c);
            state = OUTSPACE;
        }
        else if (c == ' ' && state == OUTSPACE){
            putchar(c);
            state = INSPACE;
        }
    }
    return 0;
}
*/

/*更简化版*/

/*
#include <stdio.h>

# define OUTSPACE 0
# define INSPACE 1

int main()
{
    int c;
    int state = OUTSPACE;

    while ( (c = getchar()) != EOF ){
        if (c != ' '){
            putchar(c);
            state = OUTSPACE;
        }
        else if (state == OUTSPACE){    //这里的这个"else"千万不能少。否则第二个if和第一个if成并列的关系了。于是输入一个a，输出了aa。
            putchar(c);
            state = INSPACE;
        }
    }
    return 0;
}
*/
