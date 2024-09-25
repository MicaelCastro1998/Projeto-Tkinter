import tkinter as tk
from tkinter import messagebox, ttk

class ControleAtendimento:
    def __init__(self):
        self.atendimentos = []

    def mostrar_tabela(self):
        tabela = tk.Toplevel()
        tabela.title("Atendimentos Realizados")
        
        colunas = ("Nome", "Data", "Hora", "Status")
        tree = ttk.Treeview(tabela, columns=colunas, show="headings")
        
        for coluna in colunas:
            tree.heading(coluna, text=coluna)
        
        for atendimento in self.atendimentos:
            tree.insert("", tk.END, values=atendimento)
        
        tree.pack(expand=True, fill=tk.BOTH)

    def registrar_atendimento(self):
        nome = entry_nome.get()
        data = entry_data.get()
        hora = entry_hora.get()
        status = combo_status.get()

        if nome and data and hora and status:
            atendimento = (nome, data, hora, status)
            self.atendimentos.append(atendimento)
            messagebox.showinfo("Sucesso", "Atendimento registrado!")
            self.mostrar_tabela()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

# Interface
root = tk.Tk()
root.title("Controle de Atendimento")

# Entradas
tk.Label(root, text="Nome").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Data (DD/MM/AAAA)").pack()
entry_data = tk.Entry(root)
entry_data.pack()

tk.Label(root, text="Hora (HH:MM)").pack()
entry_hora = tk.Entry(root)
entry_hora.pack()

tk.Label(root, text="Status").pack()
combo_status = ttk.Combobox(root, values=["Atendido", "Não Atendido"])
combo_status.pack()

btn_registrar = tk.Button(root, text="Registrar Atendimento", command=lambda: controle.registrar_atendimento())
btn_registrar.pack()

controle = ControleAtendimento()

root.mainloop()
