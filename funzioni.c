#include <stdio.h>

int somma(int a, int b){
    int c = 0;
    c = a + b;
    return c;
}

float divisione(int a, int b){
    if (b == 0) return 0.0;
    return (float)a/(float)b;
}

int main(){
    char nome[] = "Caio";
    printf("\nSomma: %d", somma(3, 4));
    printf("\nDiviso: %.2f", divisione(3, 4));
    printf("\nStringa %s", nome);
    return 0;
}