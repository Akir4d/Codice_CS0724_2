#include <stdio.h>

void scriviVettore(int *ptr)
{
    for(int i=0; i < 10; i++){
        printf("\nInserisci n[%d]: ", i);
        scanf("%d", ptr);
        ptr++;
    }
}

void leggiVettore(int *ptr)
{
    for (int i=0; i<10; i++){
        printf("\nn[%d] = mem[0x%x] = %d", i, ptr, *ptr);
        ptr++;
    }
}

int main(){
    int n[10] = {0};
    int *n_ptr;

    n_ptr = &n[0];

    scriviVettore (n_ptr);
    leggiVettore (n_ptr);
}