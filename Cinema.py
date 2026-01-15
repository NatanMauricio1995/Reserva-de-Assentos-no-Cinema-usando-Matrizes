"""
Sistema de Reserva de Poltronas de Cinema
Permite visualizar e reservar poltronas em um cinema com 5 fileiras e 10 poltronas cada.
"""

# Variável global para armazenar o estado do cinema
cinema = []

def zerar_cinema():
    """
    Inicializa o cinema com todas as poltronas disponíveis.
    Limpa a lista global e cria uma matriz 5x10.
    """
    global cinema
    cinema.clear()  # Limpa a lista para reinicializar
    
    for fileira in range(5):
        linha_poltronas = []
        for poltrona in range(10):
            linha_poltronas.append("Disponível")
        cinema.append(linha_poltronas)

def menu():
    """Exibe o menu principal do sistema."""
    print("-" * 80)
    print(" " * 32, "SISTEMA DE CINEMA")
    print("-" * 80)
    print()
    print("Opções:")
    print("  1 - Exibir poltronas")
    print("  2 - Reservar poltrona")
    print("  3 - Cancelar reserva")
    print("  4 - Sair")
    print()

def definir_escolha():
    """
    Obtém e valida a escolha do usuário no menu principal.
    
    Returns:
        int: Opção escolhida pelo usuário (1-4)
    """
    escolha = 0
    
    while (escolha < 1) or (escolha > 4):
        try:
            escolha = int(input("Insira sua escolha (1-4): "))
            if (escolha < 1) or (escolha > 4):
                print("❌ Insira um valor entre 1 e 4!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    return escolha

def exibir_poltronas():
    """
    Exibe o mapa de poltronas do cinema de forma organizada.
    Mostra numeração das fileiras e colunas para facilitar a escolha.
    """
    print("-" * 80)
    print(" " * 30, "MAPA DE POLTRONAS")
    print("-" * 80)
    print()
    
    # Cabeçalho com numeração das colunas
    print("      ", end="")
    for coluna in range(1, 11):
        print(f"{coluna:>11}", end="")
    print()
    print()
    
    # Exibe cada fileira
    for fileira in range(5):
        print(f"F{fileira + 1}   ", end="")
        for poltrona in range(10):
            status = cinema[fileira][poltrona]
            if status == "Disponível":
                print("Disponível ", end=" ")
            else:
                print("Reservada  ", end=" ")
        print()
    
    print()
    print("Legenda: Disponível = Livre | Reservada = Ocupada")
    print("-" * 80)
    print()

def escolha_poltrona():
    """
    Obtém as coordenadas da poltrona e chama a função para reservar.
    Valida se os números estão dentro dos limites do cinema.
    """
    fileira = -1
    coluna = -1
    
    print("--- RESERVAR POLTRONA ---")
    
    # Validação da fileira
    while (fileira < 0) or (fileira > 4):
        try:
            fileira = int(input("Insira o número da fileira (1 a 5): ")) - 1
            if (fileira < 0) or (fileira > 4):
                print("❌ Fileira deve ser entre 1 e 5!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    # Validação da coluna
    while (coluna < 0) or (coluna > 9):
        try:
            coluna = int(input("Insira o número da poltrona (1 a 10): ")) - 1
            if (coluna < 0) or (coluna > 9):
                print("❌ Poltrona deve ser entre 1 e 10!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    mudanca_status(fileira, coluna, "reservar")

def escolha_cancelamento():
    """
    Obtém as coordenadas da poltrona e chama a função para cancelar reserva.
    Valida se os números estão dentro dos limites do cinema.
    """
    fileira = -1
    coluna = -1
    
    print("--- CANCELAR RESERVA ---")
    
    # Validação da fileira
    while (fileira < 0) or (fileira > 4):
        try:
            fileira = int(input("Insira o número da fileira (1 a 5): ")) - 1
            if (fileira < 0) or (fileira > 4):
                print("❌ Fileira deve ser entre 1 e 5!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    # Validação da coluna
    while (coluna < 0) or (coluna > 9):
        try:
            coluna = int(input("Insira o número da poltrona (1 a 10): ")) - 1
            if (coluna < 0) or (coluna > 9):
                print("❌ Poltrona deve ser entre 1 e 10!")
        except ValueError:
            print("❌ Insira apenas números!")
    
    mudanca_status(fileira, coluna, "cancelar")

def mudanca_status(fileira, coluna, acao):
    """
    Altera o status de uma poltrona (reservar ou cancelar).
    
    Args:
        fileira (int): Índice da fileira (0-4)
        coluna (int): Índice da coluna (0-9)  
        acao (str): Tipo de ação ("reservar" ou "cancelar")
    """
    if acao == "reservar":
        if cinema[fileira][coluna] == "Reservada":
            print(f"\n❌ A poltrona F{fileira + 1}-{coluna + 1} já está reservada!")
            print("Escolha outra poltrona disponível.")
        else:
            cinema[fileira][coluna] = "Reservada"
            print(f"\n✅ Poltrona F{fileira + 1}-{coluna + 1} reservada com sucesso!")
    
    elif acao == "cancelar":
        if cinema[fileira][coluna] == "Disponível":
            print(f"\n❌ A poltrona F{fileira + 1}-{coluna + 1} já está disponível!")
        else:
            cinema[fileira][coluna] = "Disponível"
            print(f"\n✅ Reserva da poltrona F{fileira + 1}-{coluna + 1} cancelada!")

def exibir_estatisticas():
    """
    Calcula e exibe as estatísticas de ocupação do cinema.
    """
    total_poltronas = 50
    poltronas_reservadas = 0
    
    for fileira in cinema:
        for poltrona in fileira:
            if poltrona == "Reservada":
                poltronas_reservadas += 1
    
    poltronas_disponiveis = total_poltronas - poltronas_reservadas
    ocupacao = (poltronas_reservadas / total_poltronas) * 100
    
    print(f"\n📊 ESTATÍSTICAS:")
    print(f"   Poltronas reservadas: {poltronas_reservadas}")
    print(f"   Poltronas disponíveis: {poltronas_disponiveis}")
    print(f"   Taxa de ocupação: {ocupacao:.1f}%")

# Programa principal
print("🎬 Bem-vindo ao Sistema de Cinema! 🎬\n")

escolha = 0
zerar_cinema()

while escolha != 4:
    menu()
    escolha = definir_escolha()
    
    if escolha == 1:
        exibir_poltronas()
        exibir_estatisticas()
        
    elif escolha == 2:
        exibir_poltronas()
        escolha_poltrona()
        
    elif escolha == 3:
        exibir_poltronas()
        escolha_cancelamento()
        
    elif escolha == 4:
        print("\n🎬 Obrigado por usar nosso sistema!")
        print("Até mais! 🍿")
    
    # Pausa para visualizar o resultado
    if escolha != 4:
        input("\nPressione ENTER para continuar...")