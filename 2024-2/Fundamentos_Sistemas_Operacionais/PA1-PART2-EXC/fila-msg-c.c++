#include <sys/ipc.h>
#include <sys/msg.h>
#include <iostream>
#include <cstring>
#include <cstdlib>

/**
 * @brief Estrutura para a mensagem da fila.
 */
struct msg_buffer {
    long msg_type;
    char msg_text[100];
};

/**
 * @brief Função principal que demonstra o uso de filas de mensagens no Unix.
 * 
 * Esta função cria uma fila de mensagens, envia uma mensagem para a fila e
 * depois lê a mensagem da fila. Finalmente, a fila de mensagens é removida.
 * 
 * @return int Retorna 0 em caso de sucesso, ou 1 em caso de erro.
 */
int main() {
    key_t key;
    int msgid;
    msg_buffer message;

    // Gera uma chave única para a fila de mensagens
    key = ftok("msgqueue", 65);
    if (key == -1) {
        perror("ftok");
        return 1;
    }

    // Cria uma fila de mensagens ou obtém o ID da fila existente
    msgid = msgget(key, 0666 | IPC_CREAT);
    if (msgid == -1) {
        perror("msgget");
        return 1;
    }

    // Prepara a mensagem para envio
    message.msg_type = 1;
    std::strcpy(message.msg_text, "Hello");

    // Envia a mensagem para a fila
    if (msgsnd(msgid, &message, sizeof(message.msg_text), 0) == -1) {
        perror("msgsnd");
        return 1;
    }
    std::cout << "Mensagem enviada: " << message.msg_text << std::endl;

    // Recebe a mensagem da fila
    if (msgrcv(msgid, &message, sizeof(message.msg_text), 1, 0) == -1) {
        perror("msgrcv");
        return 1;
    }
    std::cout << "Mensagem recebida: " << message.msg_text << std::endl;

    // Remove a fila de mensagens
    if (msgctl(msgid, IPC_RMID, NULL) == -1) {
        perror("msgctl");
        return 1;
    }

    return 0;
}
