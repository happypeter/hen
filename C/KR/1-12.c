#include <stdio.h>

int main(int argc, const char *argv[])
{
    int c;
    while ((c = getchar()) != '\n') 
    {
        if (c == '\t' || c == ' ') 
        {
            putchar('\n');
            continue;
        }
        putchar(c);
    }
    putchar('\n');
    return 0;
}
