
import tkinter as tk
from tkinter import ttk
import json 

checklist = []

#funçoes basicas

def adcionar_item(tarefa):
    checklist.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa ' {tarefa} ' adcioanada à checklist.")

def marcar_concluiuda(indice):
    if 0 <= indice < len(checklist):
        checklist[indice]["concluida"] = True
        print(f"Tarefa ' {checklist[indice]['tarefa']}' marcada como concluida.")

def listar_itens():
    if not checklist:
        print("a checklist esta vazia.")
    else:
        print("checklist:")
        for i, item in enumerate(checklist):
            status = "[x]" if item["concluida"] else "[]"
            print(f"{i}. {status} {item['tarefa']}")

def  excluir_item(indice):
    if 0 <= indice < len(checklist):
        tarefa_excluida = checklist.pop(indice)
        print(f"tarefa '{tarefa_excluida['tarefa']}'excluida da checklist.")
    else:
        print("indice invalido.")

#interface com o usuario(no terminal )

def exibir_menu():
    print("\nopçoes:")
    print("1. adcionar tarefa")
    print("2. marcar tarefa como concluida")
    print("3. listar tarefas")
    print("4. excluiir tarefa")
    print("5. sair")

def executar_checklist():
    while True:
        exibir_menu()
        opcao = input("escolha uma opçao: ")

        if opcao == "1":
            tarefa = input("digite a descrição da tarefa:")
            adcionar_item(tarefa)

        elif opcao == "2":
            listar_itens()
            try:
                indice = int(input("digite o numero da tarefa a ser marcada como concluida: "))
                marcar_concluiuda(indice)
            except ValueError:
                print("entrada invalida. digite um numero.")
        elif opcao == "3":
            listar_itens()
        elif opcao == "4":
            listar_itens()
            try:
                indice = int(input("digite o numero da tarefa a ser excluida: "))
                excluir_item(indice)
            except ValueError:
                print("saindo da checklist.")
                break
            else:
                print("opcao invalida.")

executar_checklist()

#salvar checklist

def salvar_checklist(nome_arquivo="checklist.json"):
    with open(nome_arquivo, 'w') as f:
        json.dump(checklist, f)

def carregar_checklist(nome_arquivo="checklist.json"):
    global checklist
    try:
        with open(nome_arquivo, 'r') as f:
            checklist = json.load(f)
    except FileNotFoundError:
        print("arquivo de checklist não encontrado. criando uma nova checklist.")
        checklist = []

carregar_checklist()

salvar_checklist()



checklist = []

def adicionar_item_gui():
    tarefa = entry_tarefa.get()
    if tarefa:
        adicionar_item(tarefa)
        entry_tarefa.delete(0, tk.END)  # Limpa o campo de texto
        atualizar_lista()

def marcar_concluida_gui():
    try:
        indice = lista_tarefas.curselection()[0] # Pega o índice selecionado
        marcar_concluida(indice)
        atualizar_lista()
    except IndexError:
        print("Selecione uma tarefa para marcar como concluída.")

def excluir_item_gui():
  try:
    indice = lista_tarefas.curselection()[0]
    excluir_item(indice)
    atualizar_lista()
  except IndexError:
      print("Selecione uma tarefa para excluir.")

def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for i, item in enumerate(checklist):
        status = "[x]" if item["concluida"] else "[ ]"
        lista_tarefas.insert(tk.END, f"{status} {item['tarefa']}")

def adicionar_item(tarefa):  # Mantém a mesma lógica
    checklist.append({"tarefa": tarefa, "concluida": False})


def marcar_concluida(indice): # Mantém a mesma lógica
    if 0 <= indice < len(checklist):
        checklist[indice]["concluida"] = True
    else:
        print("Índice inválido.")

def excluir_item(indice):
  if 0 <= indice < len(checklist):
    checklist.pop(indice)
  else:
    print("Indice inválido")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Checklist")

# Frame para os controles
frame_controles = ttk.Frame(janela, padding=10)
frame_controles.pack()

# Campo de Entrada para a Tarefa
label_tarefa = ttk.Label(frame_controles, text="Tarefa:")
label_tarefa.grid(row=0, column=0, sticky=tk.W)
entry_tarefa = ttk.Entry(frame_controles, width=30)
entry_tarefa.grid(row=0, column=1, sticky=tk.EW)

# Botões
botao_adicionar = ttk.Button(frame_controles, text="Adicionar", command=adicionar_item_gui)
botao_adicionar.grid(row=0, column=2, sticky=tk.E)

botao_concluir = ttk.Button(frame_controles, text="Concluir", command=marcar_concluida_gui)
botao_concluir.grid(row=1, column=0, columnspan=3, pady=5)

botao_excluir = ttk.Button(frame_controles, text="Excluir", command=excluir_item_gui)
botao_excluir.grid(row=2, column=0, columnspan=3, pady=5)


# Lista de Tarefas (Listbox)
lista_tarefas = tk.Listbox(janela, width=50, height=10)
lista_tarefas.pack(padx=10, pady=10)

# Atualiza a lista inicialmente
atualizar_lista()

janela.mainloop()