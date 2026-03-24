import subprocess
import os

totalAssentos = 10
assentos = [None] * (totalAssentos + 1)

def limparTela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)

while True:
    limparTela()

    print("\n" * 2)
    print("=== CINEMA ===")
    print("1 - Entrada")
    print("2 - Saída")
    print("3 - Ver assentos")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "4":
        print("Saindo")
        break

    elif opcao == "1":

        cpf = input("Informe seu CPF: ").upper()
        if not cpf:
            print("CPF inválido.")
            continue

        estacionado = False

        for a in assentos:
            if a is not None and a[0] == cpf:
                estacionado = True
                break
        if estacionado:
            print("Veículo já estacionado.")
            continue

        livres = []
        for assento in range(1, totalAssentos + 1):
            if assentos[assento] is None:
                livres.append(assento)

        if not livres:
            print("Cinema lotado!")
            continue

        print(f"Assentos livres: {livres}")

        while True:
            assento = int(input("Escolha o assento: "))
            if assento < 1 or assento > totalAssentos:
                print("Assento inválido.")
            elif assentos[assento] is not None:
                print("Assento ocupado.")
            else:
                break

        entrada = input("Hora entrada (hh:mm): ")
        assentos[assento] = [cpf, entrada]

    elif opcao == "2":
        print("Saída")

    elif opcao == "3":
        ocupados = 0

        for indice in range(1, totalAssentos + 1):
            if assentos[indice] is None:
                print(f"Assento {indice}: LIVRE")
            else:
                print(f"Assentos {assento}: ({assentos[assento][0]} - {assentos[assento][1]})")
                ocupados += 1
    
    else:
        print("Opçao inválida!")

    input("ENTER para continuar...")