#include<stdio.h>

int main()
{
    int state = 0;
    char c;
    int midlen, finallen;
    midlen = finallen = 0;
    while ((c = getchar()) != '\n'){
        if (c != ' '){
            if (state = 0){
                state = 1;
                midlen++;
            }
            else
                midlen++;
        }
        else {
            if (state = 1){
                state = 0;
                finallen = midlen;
                midlen = 0;
            }
        }
    }
    if (state = 1)
        printf("state = %d, len = %d", state, midlen);
    else
        printf("state = %d, len = %d", state, finallen);
    return 0;
}

