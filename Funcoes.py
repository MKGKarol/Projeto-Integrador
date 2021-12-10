import Lista

def criarMenu():
    linha = "*"*50
    titulo = "Urna Eletrônica 1.0"
    print(linha.center(50)) #linha 4 5 e 6 referentes ao cabeçalho do programa
    print(titulo.center(50))
    print(linha.center(50))
    print("\n")
    print("[1] Lista de candidatos a Governador e Presidente")
    print("[2] Votar para Governador e Presidente")
    print("[3] Apurar votos")
    print("[4] Desligar a Urna")
    print("\n")
    return int(input("Digite sua opção: "))

def votacao_governador():
    while True:
        voto = int(input("\nDigite o número do canditado a Governador: "))
        if voto in Lista.Governadores:
            print(
                "Essa opção você votára em " +
                Lista.Governadores[voto]['Nome'], "para Governador")
            confirma = input("Confirmar o voto? (s ou n): ")
            if confirma == 's':
                Lista.Governadores[voto]['votos'] = Lista.Governadores[voto]['votos'] + 1
                print("Voto registrado.", end=" ")
                break
            else :
                print("Votação Reiniciada.", end=" ")
                continue

        else:
            print("Candidato não encontrado seu voto será anulado!")
            confirma = input("Confirma o voto? (s ou n): ")
            if confirma == 's':
                voto = 6
                Lista.Governadores[voto]['votos'] = Lista.Governadores[voto]['votos'] + 1
                print("Voto registrado.", end=" ")
                break
            else :
                print("Votação Reiniciada.", end=" ")
                continue

def votacao_presidente():
    while True:
        voto = int(input("\nDigite o número do canditado a Presidente: "))
        if voto in Lista.Presidentes:
            print(
                "Essa opção você votára em " +
                Lista.Presidentes[voto]['Nome'], "para Governador")
            confirma = input("Confirmar o voto? (s ou n): ")
            if confirma == 's':
                Lista.Presidentes[voto]['votos'] = Lista.Presidentes[voto]['votos'] + 1
                print("Voto registrado.", end=" ")
                break
            else :
                print("Votação Reiniciada.", end=" ")
                continue

        else:
            print("Candidato não encontrado seu voto será anulado!")
            confirma = input("Confirma o voto? (s ou n): ")
            if confirma == 's':
                voto = 6
                Lista.Presidentes[voto]['votos'] = Lista.Presidentes[voto]['votos'] + 1
                print("Voto registrado.", end=" ")
                break
            else :
                print("Votação Reiniciada.", end=" ")
                continue
