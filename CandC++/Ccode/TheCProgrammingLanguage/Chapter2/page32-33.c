#if 0

/* strlen：返回 s 的长度*/
int strlen(char s[])
{
    int i;
    i = 0;
    while (s[i] != '\0')
        ++i;
    return i;
}

#endif


/* 上面是书上原版的例子，没有主函数肯定是没法运行的。想了想
干脆自己试试标准头文件<string.h> 中同名的strlen()函数好了。*/

#include<stdio.h>
#include<string.h>

int main()
{
   int c,i;
   //i = 0;
   int s[i];
   while( (c = getchar()) != EOF ){
        s[i] = c;
   }
   int length = strlen(s[i]);
   printf( "The length of the input string is %d", length);
   return 0;
}
