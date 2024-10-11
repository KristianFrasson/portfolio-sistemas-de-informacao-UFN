import heapq
import random
from collections import deque

# Classe que representa um processador
class Processador:
    def __init__(self, id, taxa_processamento):
        self.id = id  # Identificador do processador
        self.taxa_processamento = taxa_processamento  # Taxa de processamento em processos por segundo
        self.tempo_restante = 0  # Tempo restante para concluir a tarefa atual
        self.tempo_atual = 0  # Tempo atual do processador
        self.tarefas_processadas = 0  # Contador de tarefas processadas
        self.processos_processados = 0  # Contador de processos processados

    # Método para processar uma tarefa
    def processar(self, tarefa):
        # Calcula o tempo necessário para processar a tarefa com base na taxa de processamento
        tempo_processamento = tarefa.quantidade_processos / self.taxa_processamento
        tempo_inicio = self.tempo_atual  # Tempo de início do processamento
        self.tempo_atual += tempo_processamento  # Atualiza o tempo atual do processador
        self.tempo_restante += tempo_processamento  # Atualiza o tempo restante
        self.tarefas_processadas += 1  # Incrementa o contador de tarefas processadas
        self.processos_processados += tarefa.quantidade_processos  # Incrementa o contador de processos processados
        return (tarefa.id, self.id, tempo_inicio, self.tempo_atual, tarefa.quantidade_processos)

    # Método para atualizar o tempo restante do processador
    def atualizar_tempo(self, tempo_decorrido):
        if self.tempo_restante > 0:
            self.tempo_restante = max(0, self.tempo_restante - tempo_decorrido)

    # Método para comparação entre processadores baseado no tempo restante
    def __lt__(self, other):
        return self.tempo_restante < other.tempo_restante

# Classe que representa uma tarefa
class Tarefa:
    def __init__(self, id, quantidade_processos):
        self.id = id  # Identificador da tarefa
        self.quantidade_processos = quantidade_processos  # Quantidade de processos que a tarefa exige

    # Método para comparação entre tarefas baseado na quantidade de processos
    def __lt__(self, other):
        return self.quantidade_processos < other.quantidade_processos

# Classe que representa a simulação
class Simulacao:
    def __init__(self, processadores):
        self.processadores = processadores  # Lista de processadores
        self.fila_tarefas = deque()  # Fila de tarefas
        self.historico = []  # Histórico de processamento
        self.tempo_total = 0  # Tempo total da simulação
        self.linha_do_tempo = []  # Linha do tempo dos eventos de processamento

    # Método para adicionar uma tarefa à fila
    def adicionar_tarefa(self, tarefa):
        self.fila_tarefas.append(tarefa)

    # Método para distribuir tarefas entre os processadores
    def distribuir_tarefas(self):
        while self.fila_tarefas:
            tarefa = self.fila_tarefas.popleft()  # Remove a tarefa da fila
            processador = heapq.heappop(self.processadores)  # Seleciona o processador com menor tempo restante
            detalhes = processador.processar(tarefa)  # Processa a tarefa
            self.historico.append(detalhes)  # Adiciona os detalhes ao histórico
            self.linha_do_tempo.append(
                f"Processador {detalhes[1]} começou a processar a Tarefa {detalhes[0]} às {detalhes[2]:.2f} segundos "
                f"e terminou em {detalhes[3]:.2f} segundos"
            )
            heapq.heappush(self.processadores, processador)  # Reinsere o processador na heap

    # Método para executar a simulação
    def executar(self):
        while self.fila_tarefas or any(p.tempo_restante > 0 for p in self.processadores):
            tempo_decorrido = 1  # 1 segundo
            for processador in self.processadores:
                processador.atualizar_tempo(tempo_decorrido)  # Atualiza o tempo restante de cada processador
            self.distribuir_tarefas()  # Distribui as tarefas
            self.tempo_total += tempo_decorrido  # Incrementa o tempo total da simulação

    # Método para gerar um relatório do processamento
    def gerar_relatorio(self):
        print("\nRelatório de Processamento:")
        for tarefa_id, processador_id, tempo_inicio, tempo_fim, quantidade_processos in self.historico:
            print(
                f"Tarefa {tarefa_id} foi processada pelo Processador {processador_id} "
                f"começando às {tempo_inicio:.2f} segundos e terminando em {tempo_fim:.2f} segundos "
                f"com quantidade de processos {quantidade_processos}"
            )
        print(f"\nTempo total decorrido: {self.tempo_total} segundos")

        print("\nLinha do Tempo de Processos:")
        for evento in self.linha_do_tempo:
            print(evento)

        # Análise adicional
        total_processos = sum(tarefa[4] for tarefa in self.historico)
        processador_mais_processos = max(self.processadores, key=lambda p: p.processos_processados)

        print("\nAnálise Adicional:")
        print(f"Tempo total de processamento das tarefas: {self.tempo_total} segundos")
        print(f"Quantidade total de processos: {total_processos}")
        for processador in self.processadores:
            print(f"Processador {processador.id} - Capacidade de processamento: {processador.taxa_processamento} processos/segundo, "
                  f"Tarefas processadas: {processador.tarefas_processadas}, Processos processados: {processador.processos_processados}")
        print(f"Processador que mais processou processos: Processador {processador_mais_processos.id} "
              f"com {processador_mais_processos.processos_processados} processos")

    # Método para exibir as tarefas atendidas na ordem FIFO
    def exibir_tarefas_atendidas(self):
        print("\nTarefas Atendidas na Ordem FIFO:")
        for tarefa_id, processador_id, tempo_inicio, tempo_fim, quantidade_processos in self.historico:
            print(f"Tarefa {tarefa_id} foi atendida pelo Processador {processador_id}")

# Função principal que inicializa a simulação
def main():
    num_processadores = int(input("Digite o número de processadores: "))  # Solicita o número de processadores
    processadores = []
    for i in range(num_processadores):
        id = i + 1
        taxa_processamento = float(input(f"Digite a taxa de processamento do processador {id} (processos por segundo): "))
        processadores.append(Processador(id, taxa_processamento))  # Cria e adiciona processadores à lista
    heapq.heapify(processadores)  # Organiza os processadores em uma heap

    simulacao = Simulacao(processadores)  # Cria a simulação com os processadores

    num_tarefas = int(input("Digite o número de tarefas: "))  # Solicita o número de tarefas
    for i in range(num_tarefas):
        id = i + 1
        quantidade_processos = random.randint(0, 1000)  # Gera uma quantidade aleatória de processos para a tarefa
        simulacao.adicionar_tarefa(Tarefa(id, quantidade_processos))  # Adiciona a tarefa à simulação

    simulacao.executar()  # Executa a simulação
    simulacao.gerar_relatorio()  # Gera o relatório da simulação
    simulacao.exibir_tarefas_atendidas()  # Exibe as tarefas atendidas

if __name__ == "__main__":
    main()  # Chama a função principal

