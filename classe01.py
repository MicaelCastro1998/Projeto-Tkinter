import tkinter as tk
from tkinter import messagebox, ttk

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

    def salvar_pessoa(self, nome, idade, altura, genero, aceita_termos):
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
