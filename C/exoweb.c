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

// you can not use "sizeof b" inside find_largest
// and this post clarified this :
// http://bytes.com/topic/c/answers/519368-how-know-size-integer-array
//
// ===POST=== 
// In either of the prototypes
//
// int count(int thearray[])
// int Max(int thearray[])
//
// thearray is declared as a pointer, you are probably getting confused
// because you are using the [] notation but this does not declare an array
// this is just another way of writting
//
// int Max(int *thearray)
//
// and a fairly confusing one as you have found out. sizeof(int *) == 4 on a
// lot of systems (and so it seems on yours).
//
// You can not find the size of an array from a pointer to it, it is
// impossible, you have to have access to the array it self to find it's size.
// This means that if you are goinf to pass an array by passing a pointer to
// it (a normal thing to do) then you need to pass the size of the array as
// well. The one acception to this is char array where it is being use to
// store a string because you can use the NULL terminator '\0' to locate the
// end of the string (but not the size of the array).
//
// What you should do is change your prototype of Max to
//
// int Max(int *thearray, int number_of_ints)
//
// and in main (where thearray is defined) call Max as
//
// max = Max(thearray, (sizeof thearray)/(sizeof thearry[0]));
//
// This will work because you are using the sizeof opertor in the same context
// that the array is declared in. 
