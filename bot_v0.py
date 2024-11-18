import os
import tkinter as tk
import selenium
from time import sleep
from tkinter import filedialog
from pandas import read_excel, DataFrame
import selenium.webdriver

# Funções
def escolher_arquivo():
    file = filedialog.askopenfilename(initialfile="Arquivo_Numeros.xlsx", title="Selecione Arquivo_Numeros.xlsx")
    global e_arquivo
    global arquivo
    if file:
        filename = os.path.basename(file)
        while filename != "Arquivo_Numeros.xlsx" and filename != "":
            filename = ""
            file = filedialog.askopenfilename(initialfile="Arquivo_Numeros.xlsx", title="Selecione Arquivo_Numeros.xlsx")
            filename = os.path.basename(file)
        if file == "":
            return
        else:
            e_arquivo.delete(0, tk.END)
            e_arquivo.insert(tk.END, filename)
            arquivo = file
            botao_iniciar.configure(bg='#00cc66',   state='normal')

def iniciar_automacao():
    global botao_iniciar
    global t_log
    global continuar
    global dados
    temp = []
    df = read_excel(arquivo)
    if list(df.columns) == ['Nome', 'Telefone', 'Texto']:
        t_log.delete("1.0", tk.END)
        t_log.insert("1.0", 'Iniciar Automação')
        botao_iniciar.configure(state='disabled', text="Continuar", bg='#a6a6a6', command=enviar_mensagens)
        enviar_mensagens(df)
        print(dados)
    else:
        t_log.delete("1.0", tk.END)
        t_log.insert("1.0", "Verifique o nome das colunas do arquivo\nAs colunas devem ser: Nome, Telefone, Texto")

def enviar_mensagens(df):
    nomes = []
    numeros = []
    mensagens = []
    for value in df.values:
        nomes += [list(value)[0]]
        numeros += [list(value)[1]]
        mensagens += [list(value)[2]]
    return 0

# Variáveis
arquivo = ""
continuar = False
dados = 0

# Interface
root = tk.Tk()
root.title('Bot WhatsApp')
root.geometry('310x500')
root.configure(background='#282828')
root.resizable(False, False)

# Configurando o layout do grid
root.grid_rowconfigure(4, weight=4)  # Log ocupa mais espaço
root.grid_rowconfigure(5, weight=1)  # Botões ocupam menos
root.grid_columnconfigure(0, weight=1)

# Declarando os elementos
label_inicial = tk.Label(
    root,
    text="Bot de WhatsApp",
    bg="#282828",
    fg="white",
    font=("Arial", 12),  # Texto menor
    anchor="center"
)

label_arquivo = tk.Label(root, text="Arquivo:", bg="#282828", fg="white", font=("Arial", 10))
label_log = tk.Label(root, text="Log de Execução", bg="#282828", fg="white", font=("Arial", 10))

e_arquivo = tk.Entry(root, width=40, borderwidth=2, relief="solid")  # Nome do Arquivo
t_log = tk.Text(root, wrap=tk.WORD, borderwidth=2, relief="solid", height=10)  # Log ocupa 40% da tela

botao_iniciar = tk.Button(root, text="Iniciar Automação", command=iniciar_automacao, bg="#a6a6a6", fg="black", font=("Arial", 10), state='disabled')
botao_arquivo = tk.Button(root, text="Escolher Arquivo Excel", command=escolher_arquivo, bg="#007acc", fg="white", font=("Arial", 10))

# Adicionando os elementos na tela
label_inicial.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")
label_arquivo.grid(row=1, column=0, padx=10, pady=5, sticky="w")
e_arquivo.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")
botao_arquivo.grid(row=2, column=2, padx=10, pady=5, sticky="e")
label_log.grid(row=3, column=0, padx=10, pady=5, sticky="w")
t_log.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
botao_iniciar.grid(row=5, column=0, columnspan=3, padx=10, pady=15)

root.mainloop()
