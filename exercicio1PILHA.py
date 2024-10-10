pilha = []
pilhaAuxiliar = []

while True:
    print ("\n")
    valor = input("Digite a opção 1 para adicionar, 2 para 'Control + Z', 3 para 'Control Y' e 0 para encerrar: ")
    
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