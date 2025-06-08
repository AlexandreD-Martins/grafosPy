import classes

def menu():
    g = classes.Grafo()
    g.readCSV()

    while True:
        print("\nMENU GRAFOS DE CIDADES")
        print("1. Cadastrar cidade")
        print("2. Cadastrar conexão")
        print("3. Listar cidades")
        print("4. Listar conexões")
        print("5. Listar vizinhos de uma cidade")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da cidade: ")
            cidade, criada = g.regCity(nome)
            if criada:
                print("Irrul!!!")
            else: print("bah chefe ja tinha essa!!!")

        elif opcao == "2":
            name1 = input("Cidade 1: ")
            name2 = input("Cidade 2: ")
            try:
                dist = float(input("Distância entre as cidades (km): ").replace(",", "."))
                criada = g.regConn(name1, name2, dist)
                if criada:
                    print("Irrul!!!")
                else: print("bah chefe ja tinha essa!!!")

            except ValueError:
                print("Distância inválida.")

        elif opcao == "3":
            g.infoCity()

        elif opcao == "4":
            g.infoConn()

        elif opcao == "5":
            nome = input("Digite o nome da cidade: ")
            g.neighbors_of(nome)

        elif opcao == "6":
            print("é nois cpx.")
            break

        else:
            print("Não tenha pai, ratiou, ve a lista ai.")

if __name__ == "__main__":
    menu()
