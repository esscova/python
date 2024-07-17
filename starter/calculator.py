
def calculator():
    print("Bem-vindo à calculadora Python!")
    print("Selecione qual operação deseja:")
    
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = input('Digite sua escolha: 1 - 2 - 3 - 4\n')


    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))

    if operacao == '1':
        print(f"{num1} + {num2} = {num1+num2}")
    
    elif operacao == '2':
        print(f"{num1} - {num2} = {num1-num2}")
    
    elif operacao == '3':
        print(f"{num1} x {num2} = {num1*num2}")

    elif operacao == '4':
            if num2 == 0:
                print('Erro: Divisão por zero')
            else:
                print(f"{num1} / {num2} = {num1/num2}")
    else:
         print("Opção inválido")

calculator()