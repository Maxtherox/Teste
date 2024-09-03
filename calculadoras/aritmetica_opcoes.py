import math

def operacoes_aritmeticas():
    while True:
        try:
            operacao = int(input('''
> Qual operação matemática irá usar?
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Radiciação
[6] Potenciação
>>> '''))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    if operacao == 1:
        soma = 0
        while True:
            try:
                n = float(input('''
Digite o valor a ser somado ou [0] para Parar:
>>> '''))
                if n != 0:
                    soma += n
                else:
                    print(f"Soma total: {soma:.2f}")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    elif operacao == 2:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado da subtração: {num1 - num2:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    elif operacao == 3:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado da multiplicação: {num1 * num2:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    elif operacao == 4:
        try:
            num1 = float(input("Digite o dividendo: "))
            num2 = float(input("Digite o divisor: "))
            if num2 != 0:
                print(f"Resultado da divisão: {num1 / num2:.2f}")
            else:
                print("Divisão por zero não é permitida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    elif operacao == 5:
        try:
            num = float(input("Digite o número: "))
            raiz = math.sqrt(num)
            print(f"Raiz quadrada de {num}: {raiz:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    elif operacao == 6:
        try:
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = base ** expoente
            print(f"{base} elevado a {expoente}: {resultado:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    else:
        print("Opção inválida.")
