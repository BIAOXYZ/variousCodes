/* 练习 1-12. 写一个程序把输入的单词打印出来，每行一个。 */

/*
思路：
当输入为空格，制表或回车时，如果是首次遇到的就立刻换行。如果不是首次遇到
的就什么也不做。当输入为非空格，制表和回车时，原样输出这个输入值。
1.初始状态设为OUTWORD，也就是就算来了空制回三种符号，程序也只是忽略掉（从
而保证第一行也是从最左边开始）。
2.当第一个非空制回的符号出现时，立即输出这个字符，并把状态变为INWORD。
3.当在INWORD状态下出现了空制回时（也就是这个空制回是继前面的字符后的第一个
空格制表或回车），忽略这个符号，但是输出一个换行（因此达到了另起一行的目的）。
同时把状态变为OUTWORD。
4.当在OUTSPACE状态下出现了空制回时（也就是至少是第二个空格制表或回车了），
忽略这个符号。
*/

#include<stdio.h>

#define INWORD 1
#define OUTWORD 0

int main()
{
    int c;
    int state = OUTWORD;

    while ( (c = getchar()) != EOF ){
        if ( c == ' ' || c == '\t' || c == '\n' ){
            if (state == INWORD){
                state = OUTWORD;
                printf("\n");
            }
        }
        else
        {
            state = INWORD;
            putchar(c);
        }
    }
    return 0;
}


/*
这个是最开始写的程序，有个问题就是每个空格和制表符都会引起一个换行。开始
老是从逻辑上入手，怎么都觉得我的思路没问题啊。后来他妹的发现是第二个if括
号里的判断条件该用等号(==)的用成赋值了(=)。加了一个等号后一切正常，还真是
一个等号引发的惨案呀~囧。。。
*/

#if 0

#include<stdio.h>

#define INWORD 1
#define OUTWORD 0

int main()
{
    int c;
    int state = OUTWORD;

    while ( (c = getchar()) != EOF ){
        if ( c == ' ' || c == '\t' || c == '\n' ){
            if (state = INWORD){                  //此时相当于if( 1 ), 然后state状态已经起不到任何作用了。所以只要来一个空制回，就输出个回车。
                state = OUTWORD;
                printf("\n");
            }
        }
        else
        {
            state = INWORD;
            putchar(c);
        }
    }
    return 0;
}

#endif // 0


/*
这段程序更有趣了，我只是把最开始那段程序的宏定义里01值互换了一下，结果
程序变成了"将输入中的所有空格，制表符和换行删除并打印出其他所有输入值。"
然而exercise1-9里的那个程序交换宏定义变量里的01值似乎没有什么影响。
*/

/* 呃，原因已经明白了。就因为少了个等号(=)呗。这样if括号里的判断条件就
跟INWORD和OUTWORD的具体值有关了。而实际上正确的程序是和它俩的值无关的————也
就是它俩不管谁取0谁取1都不影响程序正确性。*/

#if 0

#include<stdio.h>

#define INWORD 0
#define OUTWORD 1

int main()
{
    int c;
    int state = OUTWORD;

    while ( (c = getchar()) != EOF ){
        if ( c == ' ' || c == '\t' || c == '\n' ){
            if (state = INWORD){                 //此时相当于if( 0 ), state状态起不到任何作用。并且输出回车（也就是另起一行）操作永远不会执行了。
                state = OUTWORD;
                printf("\n");
            }
        }
        else
        {
            state = INWORD;
            putchar(c);
        }
    }
    return 0;
}

#endif // 0
