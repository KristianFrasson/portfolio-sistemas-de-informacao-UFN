#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

// Exercício 5: Espaço de Endereçamento de Processos
// Este programa demonstra que cada processo tem seu próprio espaço de endereçamento.

int s = 0;

int main() {
    if (fork() == 0) {
        // Processo Filho
        s = 10;
        printf("Processo filho, s = %d\n", s);
    } else {
        // Processo Pai
        wait(NULL); // Espera o filho terminar
        printf("Filho terminou a execução!\n");
        printf("Processo pai, s = %d\n", s);
    }
    return 0;
}

/*
Explicação:
- O processo filho altera o valor da variável s para 10.
- O processo pai espera o término do processo filho usando wait().
- O processo pai imprime o valor da variável s, que permanece 0.
- Cada processo tem seu próprio espaço de endereçamento, então as alterações feitas pelo filho não afetam o pai.
*/