#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

// Exercício 4: Quantidade de Processos Criados
// Este programa demonstra a criação de múltiplos processos usando fork().

int main() {
    fork();
    fork();
    printf("PID = %d\n", getpid());
    return 1;
}

/*
Explicação:
- O primeiro fork() cria um novo processo, totalizando 2 processos.
- O segundo fork() é executado por ambos os processos, criando mais 2 processos, totalizando 4 processos.
- Cada processo imprime seu PID.
*/