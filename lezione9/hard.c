#include <stdio.h>
#include <stdlib.h>

void stampaArray(int *array, int size) {
    printf("Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main() {
    int *array = malloc(10 * sizeof(int));
    int dimensione_corrente_array = 0;
	int dimensione_massima_array=10;

    if (array == NULL) {
        fprintf(stderr, "Errore nell'allocazione di memoria.\n");
        return 1;
    }

    printf("Inserisci numeri interi. Inserisci un carattere non numerico per uscire.\n");

    while (1) {
        int input;
        printf("Inserisci un numero intero: ");
        if (scanf("%d", &input) != 1) {
            printf("Input non valido. Uscita dal programma.\n");
            break;
        }

        if (dimensione_corrente_array == dimensione_massima_array) {
            // Rialloca l'array se la dimensione massima è raggiunta
            dimensione_massima_array += 5;
            array = realloc(array, 10 * sizeof(int));

            if (array == NULL) {
                fprintf(stderr, "Errore nell'allocazione di memoria.\n");
                return 1;
            }
        }

        // Aggiunge il numero all'array e incrementa la dimensione
        array[dimensione_corrente_array] = input;
        dimensione_corrente_array++;

        // Stampa l'array
        stampaArray(array, dimensione_corrente_array);
    }

    // Libera la memoria allocata dinamicamente
    free(array);

    return 0;
}

