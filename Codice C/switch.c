#include <stdio.h>

int main()
{
    int scelta;
    printf("\nBuongiorno, qui il manicomio:\n1 se schizofrenico\n2 se panoico\n3 se hai bassa autostima\n");
    scanf("%d", &scelta);
    switch(scelta)
    {
        case 1:
            printf("\nVorremmo parlare con una altra delle tue personalita'");
            break;
        case 2:
            printf("\nTi avvisiamo che questa chimata e' condivisa con i poteri forty");
            break;
        case 3:
            printf("\nI nostri operatori stanno parlando con persone piu' importanti di te");
            break;
        default:
            printf("Grazie Artur per averci contattato");
    }
    return 0;
}