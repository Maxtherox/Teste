from calculadoras.aritmetica_opcoes import operacoes_aritmeticas

def main():
    escolha = int(input("> Escolha uma opção: "))
    
    if escolha == 1:
        operacoes_aritmeticas()
    # Adicione outras opções aqui

main()