#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

// Exercício 2: Espera por Processo
// Este programa demonstra o uso de wait() para esperar a conclusão de um processo filho.

int f1(int x) {
    printf("x = %d\n", x);
    return 0;
}

int main() {
    pid_t procID;

    // Cria um novo processo
    procID = fork();

    if (procID < 0) {
        printf("Erro na criação do novo processo\n");
        return -1;
    } else if (procID == 0) {
        // Processo Filho
        printf("Processo filho - PID = %d\n", getpid());
        f1(100);
        printf("Filho executou a função f1 do Pai...\n");
        return 1;
    } else {
        // Processo Pai
        wait(NULL); // Espera o filho terminar
        printf("Processo Pai - PID = %d\n", getpid());
        f1(50);
        printf("Pai executou a função f1...\n");
        return 1;
    }
}

/*
Explicação:
- O processo pai cria um processo filho usando fork().
- O processo pai espera o término do processo filho usando wait().
- O processo filho executa a função f1() com o argumento 100.
- O processo pai executa a função f1() com o argumento 50 após o término do filho.
*/