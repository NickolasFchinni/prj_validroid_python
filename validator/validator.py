if __name__ == "__main__":
    try:
        with open("build_log.txt", "r") as log:
            content = log.read()
            if "ERROR" in content:
                print("Build com erros. Verifique os logs.")
            else:
                print("Build gerada com sucesso!")
    except FileNotFoundError:
        print("Arquivo de log não encontrado. Execute o build.")