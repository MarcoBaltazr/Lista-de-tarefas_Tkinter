import tkinter as tk
from tkinter import messagebox
import os 

class GerenciadorTarefas:
    def __init__(self, master):
        self.master = master
        master.title("Meu Gerenciador de Tarefas")
        master.geometry("400x500")

        self.nome_arquivo = "tarefas.txt" 
        self.tarefas = [] 

        self.carregar_tarefas() 
        self.entrada_tarefa = tk.Entry(master, width=40)
        self.entrada_tarefa.pack(pady=10)

        self.btn_adicionar = tk.Button(master, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.btn_adicionar.pack()

        self.lista_tarefas_display = tk.Listbox(master, width=50, height=15)
        self.lista_tarefas_display.pack(pady=10)

        self.btn_concluir = tk.Button(master, text="Marcar como Concluída", command=self.marcar_concluida)
        self.btn_concluir.pack()

        self.btn_remover = tk.Button(master, text="Remover Tarefa", command=self.remover_tarefa)
        self.btn_remover.pack()

        master.protocol("WM_DELETE_WINDOW", self.ao_fechar_janela)

        self.atualizar_lista_display() 

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get().strip() 
        if tarefa:
            self.tarefas.append(tarefa)
            self.atualizar_lista_display()
            self.entrada_tarefa.delete(0, tk.END)
            self.salvar_tarefas() 
        else:
            messagebox.showwarning("Aviso", "Por favor, digite uma tarefa.")

    def atualizar_lista_display(self):
        self.lista_tarefas_display.delete(0, tk.END)
        for tarefa in self.tarefas:
            if "[CONCLUÍDA]" in tarefa:
                self.lista_tarefas_display.insert(tk.END, tarefa)
            else:
                self.lista_tarefas_display.insert(tk.END, tarefa)


    def marcar_concluida(self):
        try:
            indice_selecionado = self.lista_tarefas_display.curselection()[0]
            tarefa_original = self.tarefas[indice_selecionado]

            if not tarefa_original.startswith("[CONCLUÍDA] "):
                self.tarefas[indice_selecionado] = "[CONCLUÍDA] " + tarefa_original
            else: 
                self.tarefas[indice_selecionado] = tarefa_original.replace("[CONCLUÍDA] ", "", 1) 

            self.atualizar_lista_display()
            self.salvar_tarefas() 
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para marcar/desmarcar como concluída.")

    def remover_tarefa(self):
        try:
            indice_selecionado = self.lista_tarefas_display.curselection()[0]
            del self.tarefas[indice_selecionado]
            self.atualizar_lista_display()
            self.salvar_tarefas() 
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")


    def carregar_tarefas(self):
        """Carrega as tarefas de um arquivo de texto."""
        if os.path.exists(self.nome_arquivo): 
            with open(self.nome_arquivo, "r", encoding="utf-8") as f:
                self.tarefas = [linha.strip() for linha in f if linha.strip()]

    def salvar_tarefas(self):
        """Salva as tarefas em um arquivo de texto."""
        with open(self.nome_arquivo, "w", encoding="utf-8") as f:
            for tarefa in self.tarefas:
                f.write(tarefa + "\n")

    def ao_fechar_janela(self):
        """Função chamada quando a janela está prestes a ser fechada."""
        self.salvar_tarefas() 
        self.master.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefas(root)
    root.mainloop()