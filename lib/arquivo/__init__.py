from tkinter import messagebox

def verificarArquivo(name):
    try:
        a = open(name, 'r')  # Tenta abrir o arquivo name, no modo leitura.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# // Cria o arquivo seguindo o bool da função "verificarArquivo".
def criarArquivo(name):
    # Escreve (wt) o arquivo name, e caso não exista, o cria (+).
    a = open(name, 'r+')
    a.close()
    