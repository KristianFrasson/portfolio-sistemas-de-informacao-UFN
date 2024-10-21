#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

// Exercício 1: Criação de Processos
// Este programa demonstra a criação de processos usando fork() e exibe os PIDs dos processos pai e filho.

int main() {
    pid_t procID;

    // Cria um novo processo
    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        // Processo Filho
        printf("Processo filho - para o FILHO o fork devolveu %d\n", procID);
        printf("Processo filho - PID = %d\n", getpid());
        return 1;
    } else {
        // Processo Pai
        printf("Processo Pai - para o PAI o fork devolveu %d\n", procID);
        printf("Processo Pai - PID = %d\n", getpid());
        return 1;
    }
}

/*
Explicação:
- O comando fork() cria um novo processo.
- Para o processo pai, fork() retorna o PID do processo filho.
- Para o processo filho, fork() retorna 0.
- Em caso de erro, fork() retorna -1.
*/