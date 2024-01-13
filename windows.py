import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


janela = customtkinter.CTk()
janela.geometry("600x400")

def clique():
    print("Começar o jogo")

text = customtkinter.CTkLabel(janela, font=("Arial", 22), text="Pense em um personagem do universo dos Incríveis, \n e eu vou tentar adivinhar")
text.pack(padx=10, pady=10)


nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome", width=300, height=40)
nome.pack(padx=10, pady=10)


checkbox = customtkinter.CTkCheckBox(janela, text="Ligar som")
checkbox.pack(padx=10, pady=10)


botao = customtkinter.CTkButton(janela, text="Start", width=200, height=40, command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()

