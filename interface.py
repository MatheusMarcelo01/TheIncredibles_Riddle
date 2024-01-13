import tkinter as tk
from tkinter import messagebox

class JogoAdivinhacao(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Adivinhe o Personagem")
        self.geometry("600x400")

        self.label = tk.Label(self, text="Pense em um personagem do universo dos Incríveis e eu tentarei adivinhar!")
        self.label.pack(pady=10)

        self.button_start = tk.Button(self, text="Começar", command=self.iniciar_jogo)
        self.button_start.pack(pady=20)

    def iniciar_jogo(self):
        self.destroy()

        self.janela_perguntas = JanelaPerguntas()
        self.janela_perguntas.mainloop()

class JanelaPerguntas(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Perguntas sobre o Personagem")
        self.geometry("600x400")

        self.resposta_var = tk.StringVar()

        self.label_pergunta = tk.Label(self, text="Seu personagem é um super herói? (Sim/Não/Não Sei): ")
        self.label_pergunta.pack(pady=10)

        self.entry_resposta = tk.Entry(self, textvariable=self.resposta_var)
        self.entry_resposta.pack(pady=10)

        self.button_confirmar = tk.Button(self, text="Confirmar", command=self.verificar_resposta)
        self.button_confirmar.pack(pady=20)

    def verificar_resposta(self):
        resposta = self.resposta_var.get().lower()

        if resposta == "sim":
            messagebox.showinfo("Resposta", "Você escolheu um super herói!")
            # Adicione aqui as lógicas para perguntas adicionais
        elif resposta == "não":
            messagebox.showinfo("Resposta", "Você escolheu um personagem que não é super herói!")
            # Adicione aqui as lógicas para perguntas adicionais
        elif resposta == "não sei":
            messagebox.showinfo("Resposta", "Você não sabe??? Só responda se seu personagem tem poderes ou não.")
        else:
            messagebox.showerror("Erro", "Resposta inválida. Por favor, responda com 'Sim', 'Não' ou 'Não Sei'.")

if __name__ == "__main__":
    app = JogoAdivinhacao()
    app.mainloop()
