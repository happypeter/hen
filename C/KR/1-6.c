#include <stdio.h>

int main(int argc, const char *argv[])
{
    while(1)
    {
        if(getchar()!=EOF)
            printf("it is 1\n");
        else
            printf("it is 0\n");
    }
    return 0;
}
