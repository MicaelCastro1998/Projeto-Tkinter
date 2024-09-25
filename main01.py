import tkinter as tk
from tkinter import messagebox, ttk
from classe01 import CadastroPacientes

class CadastroPacientes:
    def __init__(self):
        self.pessoas_cadastradas = []

    def mostrar_tabela(self):
        janela_tabela = tk.Toplevel()
        janela_tabela.title("Pessoas Cadastradas")
        
        colunas = ("Nome", "Idade", "Altura", "Gênero")
        tree = ttk.Treeview(janela_tabela, columns=colunas, show="headings")
        
        for coluna in colunas:
            tree.heading(coluna, text=coluna)
        
        for pessoa in self.pessoas_cadastradas:
            tree.insert("", tk.END, values=pessoa[:3])  # Apenas os 3 primeiros campos
        
        tree.pack(expand=True, fill=tk.BOTH)

    def salvar_pessoa(self):
        nome = entry_nome.get()
        idade = entry_idade.get()
        altura = entry_altura.get()
        genero = combo_genero.get()
        aceita_termos = var_termos.get()

        if nome and idade and altura:
            try:
                idade = int(idade)
                altura = float(altura)

                if aceita_termos:
                    pessoa = (nome, idade, altura, genero)
                    self.pessoas_cadastradas.append(pessoa)
                    messagebox.showinfo("Cadastro Concluído", "Pessoa cadastrada com sucesso!")
                    self.mostrar_tabela()
                else:
                    messagebox.showwarning("Erro", "Você deve aceitar os termos.")
            except ValueError:
                messagebox.showerror("Erro", "Idade e altura devem ser numéricos!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

# Configuração da interface
root = tk.Tk()
root.title("Cadastro de Pessoas")

# Entradas
tk.Label(root, text="Nome").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Idade").pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

tk.Label(root, text="Altura").pack()
entry_altura = tk.Entry(root)
entry_altura.pack()

tk.Label(root, text="Gênero").pack()
combo_genero = ttk.Combobox(root, values=["Masculino", "Feminino", "Outro"])
combo_genero.pack()

var_termos = tk.BooleanVar()
check_termos = tk.Checkbutton(root, text="Aceito os termos", variable=var_termos)
check_termos.pack()

btn_salvar = tk.Button(root, text="Salvar", command=lambda: cadastro.salvar_pessoa())
btn_salvar.pack()

cadastro = CadastroPacientes()

root.mainloop()
