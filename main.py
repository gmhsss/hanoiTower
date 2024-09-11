# importa sys para encerrar o programa
import sys

#variaveis para armazenar estado do jogo
ndiscos = 0  #num de discos
iniciarjogo = False  #indicador do inicio do jogo
movimentos = 0  #contador de movimento
torreA = []  # lista para armazenar os discos na torre A
torreB = []  # lista para armazenar os discos na torre B
torreC = []  # lista para armazenar os discos na torre C


# função para obter a quantidade de discos e validar a entrada
def quantDisco():
    global iniciarjogo
    global ndiscos
    ndiscos = 0


# Função recursiva para resolver o problema das Torres de Hanói
def torre(n, origem, destino, auxiliar):
    # Caso base da recursão: se n for maior que 0, procede com a lógica
    if n > 0:
        # Passo 1: Move n-1 discos da torre de origem para a torre auxiliar usando a torre de destino como auxiliar
        torre(n - 1, origem, auxiliar, destino)

        # Passo 2: Imprime a instrução para mover o disco n da torre de origem para a torre de destino
        print("Mova o disco", n, "de", origem, "para", destino)

        # Passo 3: Move n-1 discos da torre auxiliar para a torre de destino usando a torre de origem como auxiliar
        torre(n - 1, auxiliar, destino, origem)


# Solicita ao usuário o número de discos
num = int(input("Digite o número de discos: "))

# Chama a função torre para iniciar o processo de mover 'num' discos da torre 'A' para a torre 'C' usando a torre 'B' como auxiliar
torre(num, 'A', 'C', 'B')
