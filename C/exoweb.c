#include <stdio.h>
//FIXME: how to rm ARRAYSIZE, and handle arbitrary array size ?
//anyway it is common practice to pass size when handle arrays in a founction,
//_the C programming lanaguage_ is loaded with such examples(however, for
//strings is not necessay, since strlen() works well)

#define ARRAYSIZE 5

void init_arrary();
int find_largest(int b[]);
int a[ARRAYSIZE];
int b[ARRAYSIZE];
int main(int argc, const char *argv[])
{
    int j, i;
    init_arrary();
    for (i = 0; i < ARRAYSIZE; i++) {
        for (j = 0; j < ARRAYSIZE-i; j++) {
            if(a[i] == a[i+j])
                b[i]++;
        }
    }

    int k = find_largest(b);
    printf("the largest subscript is %d\n", k );
    printf("so the most frequently showed num is %d, and it is showed %d times\n", a[k], b[k]);
    return 0;
}

void init_arrary()
{
    int i;
    for (i = 0; i < ARRAYSIZE; i++) 
    {
        scanf("%d", &(a[i]));
        printf("a[%d] = %d\n", i, a[i]);
    }
}

// find largest element in the arrary

int find_largest(int b[])
{
    int i; 
    int k = 0;
    int largest_num = b[0];

    for (i = 1; i < ARRAYSIZE; i++) 
    {
        if(largest_num < b[i]) 
        {
            largest_num = b[i];
            k = i; // save the subscript of largest_num
        }
    }
    return k;

}
