#if 0

/* lower：将 c 转换为小写形式；仅适用于 ASCII 码 */
int lower(int c)
{
    if (c >= 'A' && c <= 'Z')
        return c + 'a' – 'A';
    else
        return c;
}

#endif // 0



/* 上面是书上原版的例子，没有主函数肯定是没法运行的。
于是加上主函数自己运行下好了。*/


int lower(int c)
{
    if (c >= 'A' && c <= 'Z')
        return c + 'a' – 'A';
    else
        return c;
}


/* 测试标准头文件 <ctype.h>中的tolower()函数和isdigit()函数 */


