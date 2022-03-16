from tkinter import messagebox
from lib.arquivo import *
from tkinter import *

arquivo = '.\contas.txt'  # Arquivo txt.
# Verifica se o arquivo é existente.
verificar_arquivo = verificarArquivo(arquivo)
if not verificar_arquivo:  # Se não existe,
    criarArquivo(arquivo)  # Cria o arquivo txt.


class Aplicativo:
    def __init__(self, master=None, arquivo=arquivo):

        # Container 1 //Título
        self.container1 = Frame(master)
        self.container1['padx'] = 10
        self.container1.pack()
        

        # Container 2 //Descrição
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2['pady'] = 3
        self.container2.pack()

        # Container 3 //Valor
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3['pady'] = 3
        self.container3.pack()

        # Container 4 //Adicionar conta
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4['pady'] = 4
        self.container4.pack()

        # Container 5 //Remover conta
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5['pady'] = 2
        self.container5.pack()

        # Container 6 //Listbox
        self.container6 = Frame(master)
        self.container6['padx'] = 20
        self.container6['pady'] = 30
        self.container6.pack()

        # Texto: GESTOR DE CONTAS
        self.titulo = Label(self.container1, text="GESTOR DE CONTAS")
        self.titulo["font"] = ("Corbel", "14", "italic")
        self.titulo.pack()

        # Campo de texto: Descrição
        self.input_descLabel = Label(self.container2, text='Descrição')
        self.input_descLabel.pack(side=LEFT)
        self.input_desc = Entry(self.container2)
        self.input_desc['width'] = '30'
        self.input_desc['font'] = 'Corbel', '10'
        self.input_desc.pack()

        # Campo de texto: Valor
        self.input_valLabel = Label(self.container3, text='Valor        ')
        self.input_valLabel.pack(side=LEFT)
        self.input_val = Entry(self.container3)
        self.input_val['width'] = '30'
        self.input_val['font'] = 'Arial', '10'
        self.input_val.pack()

        # Botão: Adicionar conta
        self.add_conta = Button(self.container4)
        self.add_conta['text'] = 'Adicionar conta'
        self.add_conta['font'] = 'Corbel', '10'
        self.add_conta['width'] = '15'
        self.add_conta['command'] = self.cadastrarConta
        self.add_conta.pack()

        # Botão: Remover conta
        self.del_conta = Button(self.container5)
        self.del_conta['text'] = 'Remover conta'
        self.del_conta['font'] = 'Corbel', '10'
        self.del_conta['width'] = '15'
        self.del_conta['command'] = self.removerConta
        self.del_conta.pack()

        # Listbox
        self.lista = Listbox(self.container6, height=15, width=40)
        self.lista.pack(side=LEFT)
        self.scrollbar = Scrollbar(self.container6)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.lista.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista.yview)
        # Atualiza os valores da lista, seguindo o arquivo txt
        self.lerConta(arquivo)

    def cadastrarConta(self):
        try:
            # Declara "desc", como str inserido em 'descrição'.
            desc = self.input_desc.get()
            # Declara "valor", como float inserido em 'valor'.
            valor = float(self.input_val.get())
            # Insire valores formatados na lista.
            self.lista.insert(END, f'{desc} - R${valor:.2f}')

        except (ValueError, TypeError):
            messagebox.showwarning(
                title='Aviso!', message='É necessário preencher todos os campos para realizar essa ação.')

        with open(".\contas.txt", 'a', encoding='utf-8') as a:
            # Adiciona conta no arquivo .txt
            a.write(f'{desc.capitalize()};R${valor:.2f}\n')

    def lerConta(self, arquivo):
        with open(arquivo, 'r', encoding='utf-8') as a:
            # Para cada linha do arquivo,
            for linha in a:     
                # Separa os valores entre ';',
                dado = linha.split(';')     
                # Substitue '\n' por '',
                dado[1] = dado[1].replace('\n', '')
                # Formata o conteúdo e
                dados = f'{dado[0]} - {dado[1]}'
                # Insere os valores na lista.
                self.lista.insert(END, dados)

    def removerConta(self):
        try:
            # Indica item da lista selecionado.
            index_lista = self.lista.curselection()[0]

        except:
            messagebox.showwarning(
                title='Aviso!', message='Selecione uma conta.')     # Mensagem de erro caso não selecionar uma conta.

        else:
            # Deleta valor da lista, conforme selecionado.
            self.lista.delete(index_lista)

            with open(".\contas.txt", 'r+', encoding='utf-8') as a:
                # Lê o arquivo txt inteiro.
                listaArquivo = a.readlines()        
                # Copia os valores do arquivo.
                listaManipulacao = listaArquivo[:]

                # Para cada posição (c) e valor (v) em "listaManipulacao",
                for c, v in enumerate(listaManipulacao):
                    # Se a posição for igual a selecionada,
                    if c == index_lista:        
                        # Delete esse valor de "listaManipulacao"
                        del listaManipulacao[c]

            with open(".\contas.txt", 'w', encoding='utf-8') as a:
                # Para cada linha em "listaManipulção",
                for linha in listaManipulacao:      
                    # Escreva (substitua) ela (linha) no arquivo.
                    a.write(linha)


root = Tk()
root.title('Gestor de contas')
root.geometry('300x450')
Aplicativo(root)
root.mainloop()
