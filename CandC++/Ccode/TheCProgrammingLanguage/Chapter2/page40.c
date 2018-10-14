#if 0

/* getbits：获取从位置 p 起始的 n 个比特位 */
unsigned getbits(unsigned x, int p, int n)
{
    return (x >> (p+1-n)) & ~(~0 << n);
}

#endif // 0


/* getbits：获取从位置 p 起始的 n 个比特位 */
unsigned getbits(unsigned x, int p, int n)
{
    return (x >> (p+1-n)) & ~(~0 << n);
}
