import tkinter as tk
from tkinter import messagebox, ttk

class AgendamentoConsulta:
    def __init__(self):
        self.agendamentos = []

    def mostrar_tabela(self):
        tabela = tk.Toplevel()
        tabela.title("Consultas Agendadas")
        
        colunas = ("Nome", "Data", "Hora", "Especialidade")
        tree = ttk.Treeview(tabela, columns=colunas, show="headings")
        
        for coluna in colunas:
            tree.heading(coluna, text=coluna)
        
        for consulta in self.agendamentos:
            tree.insert("", tk.END, values=consulta)
        
        tree.pack(expand=True, fill=tk.BOTH)

    def agendar_consulta(self):
        nome = entry_nome.get()
        data = entry_data.get()
        hora = entry_hora.get()
        especialidade = combo_especialidade.get()

        if nome and data and hora and especialidade:
            consulta = (nome, data, hora, especialidade)
            self.agendamentos.append(consulta)
            messagebox.showinfo("Sucesso", "Consulta agendada!")
            self.mostrar_tabela()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

# Interface
root = tk.Tk()
root.title("Agendamento de Consultas")

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

tk.Label(root, text="Especialidade").pack()
combo_especialidade = ttk.Combobox(root, values=["Clínico Geral", "Pediatra", "Dermatologista", "Cardiologista"])
combo_especialidade.pack()

btn_agendar = tk.Button(root, text="Agendar", command=lambda: agendamento.agendar_consulta())
btn_agendar.pack()

agendamento = AgendamentoConsulta()

root.mainloop()