#include <stdio.h>

int n_blank = 0;
int n_tab = 0;
int n_newline = 0;

int main(int argc, const char *argv[])
{
    while (1) {
        char c = getchar();
        switch(c)
        {
            case ' ':    n_blank++; break;
            case '\t':   n_tab++; break;
            case '\n':   n_newline++; break;
            case EOF:    goto PR;
            default:     break;
        }
    }
    PR:
    printf("\nThe result:\n");
    printf("\n n_blank is: %d", n_blank);
    printf("\n n_tab is: %d", n_tab);
    printf("\n n_newline is: %d\n", n_newline);
    return 0;
}
