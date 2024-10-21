#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>

int main() {
    // Gerar chave única
    key_t key = ftok("shmfile", 65);
    if (key == -1) {
        perror("ftok");
        exit(1);
    }

    // Criar segmento de memória compartilhada
    int shmid = shmget(key, 1024, 0666 | IPC_CREAT);
    if (shmid == -1) {
        perror("shmget");
        exit(1);
    }

    // Anexar segmento de memória compartilhada ao espaço de endereço do processo
    char *str = (char*) shmat(shmid, (void*)0, 0);
    if (str == (char*) -1) {
        perror("shmat");
        exit(1);
    }

    // Solicitar entrada do usuário
    printf("Escreva algo: ");
    if (fgets(str, 1024, stdin) == NULL) {
        perror("fgets");
        shmdt(str);
        shmctl(shmid, IPC_RMID, NULL);
        exit(1);
    }

    // Remover nova linha do final da string, se presente
    str[strcspn(str, "\n")] = '\0';

    // Exibir o que foi escrito
    printf("Escrito: %s\n", str);

    // Desanexar segmento de memória compartilhada
    if (shmdt(str) == -1) {
        perror("shmdt");
        exit(1);
    }

    // Destruir segmento de memória compartilhada
    if (shmctl(shmid, IPC_RMID, NULL) == -1) {
        perror("shmctl");
        exit(1);
    }

    return 0;
}