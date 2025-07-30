cinema = []

def zerar_cinema():
    global cinema
    for i in range(5):
        fileira = []
        
        for x in range(10):
            fileira.append("Disponível")
        
        cinema.append(fileira)
        
def menu():
    print("-" * 128)
    print(" " * 62, "MENU")
    print("-" * 128)
    print()
    print("Opções:")
    print("  1 - Exibir poltronas;")
    print("  2 - Reservar poltrona;")
    print("  3 - Sair.")
    
def definir_escolha():
    escolha = 0
    
    while ((escolha < 1) or (escolha > 3)):
        try:
            escolha = int(input("Insira sua escolha: "))
            if((escolha < 1) or (escolha > 3)):
                print("Insira um valor numérico válido!")
        except ValueError:
            print("Insira um valor numérico válido!")
    
    return escolha
        
        
def exibir_poltronas():
    print("-" * 128)
    print(" " * 59, "POLTRONAS")
    print("-" * 128)
    for i in range(5):
        print()
        for j in range (10):
            print(cinema[i][j], end = "   ")
        print()
    print("-" * 128,"\n\n")
    
def escolha_poltrona():
    linha = -1
    coluna = -1
    
    global cinema
    
    while((linha < 0) or (linha > 4)):
        try:
            linha = (int(input("Insira o número da fileira (1 a 5): ")) - 1)
            if((linha < 0) or (linha > 4)):
                print("Insira um valor numérico válido!")
        except ValueError:
            print("Insira um valor numérico válido!")
    
    while((coluna < 0) or (coluna > 9)):
        try:
            coluna = (int(input("Insira o número da poltrona (1 a 10): ")) - 1)
            if((coluna < 0) or (coluna > 9)):
                print("Insira um valor numérico válido!")
        except ValueError:
            print("Insira um valor numérico válido!")
            
    mudanca_status (linha, coluna)

def mudanca_status(linha, coluna):
    if cinema [linha][coluna] == "Bloqueado ":
        print(f"A poltrona {linha}-{coluna} se encontra reservada!")
        escolha_poltrona()
    else:
        cinema [linha][coluna] = "Bloqueado "
        print(f"A poltrona {linha}-{coluna} foi reservada!")
    
    
escolha = 0
zerar_cinema()
while (escolha != 3):
    menu()
    escolha = definir_escolha()
    if(escolha == 1):
        exibir_poltronas()
    elif(escolha == 2):
        escolha_poltrona()
    elif(escolha == 3):
        print("Muito Obrigado! Até mais")
        
    

    