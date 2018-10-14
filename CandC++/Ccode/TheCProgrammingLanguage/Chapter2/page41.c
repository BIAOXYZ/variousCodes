#if 0

/* bitcount：统计 x 中为 1 的比特位 */
int bitcount(unsigned x)
{
    int b;

    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}

#endif // 0

/* bitcount：统计 x 中为 1 的比特位 */
int bitcount(unsigned x)
{
    int b;

    for (b = 0; x != 0; x >>= 1)
        if (x & 01)
            b++;
    return b;
}
