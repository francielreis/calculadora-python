while True:
    print("\n=== CALCULADORA ===")
    print("Digite uma conta (ex: 5+2) ou 'sair'")

    expressao = input(">>> ")

    if expressao.lower() == "sair":
        print("Encerrando...")
        break

    try:
        resultado = eval(expressao)
        print("Resultado:", resultado)
    except:
        print("Erro! Digite uma conta válida.")
