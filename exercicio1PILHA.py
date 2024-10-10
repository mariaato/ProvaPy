pilha = []
pilhaAuxiliar = []

while True:
    print ("\n")
    valor = input("Digite a opção: \n1) Para adicionar \n2) Para 'Control + Z' \n3) para 'Control + Y' \n0) Para encerrar\n ")
    
    match valor:
        case "0":
            break
        case "1":
            print ("\n")
            entrada = input("Digite um valor que deseja adicionar na pilha: ")
            pilha.append(entrada)
            print ("\n")
            print(pilha)
        case "2":
            if pilha:
                print ("\n")
                controlZ = pilha.pop()
                pilhaAuxiliar.append(controlZ)
                print(pilha)
            else:
                print ("\n")
                print("Você não pode desfazer algo que não foi feito")
        case "3":
            if pilhaAuxiliar:
                print ("\n")
                controlY = pilhaAuxiliar.pop()
                pilha.append(controlY)
                print(pilha)
            else:
                print ("\n")
                print ("Você não pode refazer algo que não foi desfeito")
        case _:
            print("Valor não correspondente com as opções ")
print ("\n")    
print("FIM")
