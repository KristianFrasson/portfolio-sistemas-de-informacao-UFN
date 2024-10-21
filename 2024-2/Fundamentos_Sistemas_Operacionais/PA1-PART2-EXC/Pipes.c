/**
 * @file Pipes.c
 * @brief Demonstra comunicação entre processos usando pipes em um sistema tipo Unix.
 *
 * Este programa cria um pipe e usa fork() para criar um processo filho. O processo filho
 * escreve uma mensagem no pipe, e o processo pai lê a mensagem do pipe.
 *
 * @detalhes
 * - A função pipe() é usada para criar um pipe, que é um array de dois descritores de arquivo.
 * - A função fork() é usada para criar um novo processo. O processo filho escreve no pipe,
 *   e o processo pai lê do pipe.
 * - A função close() é usada para fechar as extremidades não utilizadas do pipe em ambos os processos,
 *   pai e filho.
 * - A função write() é usada pelo processo filho para enviar uma mensagem através do pipe.
 * - A função read() é usada pelo processo pai para receber a mensagem do

 *
 * @author Kristian
 * @date 2024-2
 */
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    int fd[2];
    if (pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    pid_t pid = fork();
    if (pid == -1) {
        perror("fork");
        return 1;
    }

    if (pid == 0) { // Processo filho
        close(fd[0]); // Fecha leitura
        const char *msg = "Mensagem";
        write(fd[1], msg, strlen(msg) + 1); // Inclui o terminador nulo
        close(fd[1]);
    } else { // Processo pai
        close(fd[1]); // Fecha escrita
        char buffer[100];
        read(fd[0], buffer, sizeof(buffer));
        printf("Recebido: %s\n", buffer);
        close(fd[0]);
    }

    return 0;
}
