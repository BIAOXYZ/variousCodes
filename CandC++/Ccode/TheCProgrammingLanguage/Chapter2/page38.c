#if 0

/* 标准库包含有一个可移植的伪随机数生成器以及一个用于初始化其种子的函数；前者给出
了一个强制转换的示例：*/

unsigned long int next = 1;

/* rand：返回一个伪随机整数，其值域为 0..32767 */
int rand(void)
{
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}

/* srand：为 rand()设置种子 */
void srand(unsigned int seed)
{
    next = seed;
}

#endif


unsigned long int next = 1;

/* rand：返回一个伪随机整数，其值域为 0..32767 */
int rand(void)
{
    next = next * 1103515245 + 12345;
    return (unsigned int)(next/65536) % 32768;
}

/* srand：为 rand()设置种子 */
void srand(unsigned int seed)
{
    next = seed;
}
