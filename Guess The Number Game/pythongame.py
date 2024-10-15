import customtkinter as ctk
import random

numero_aleatorio=random.randint(0,100)

def advinhar(event=None):
   p = int(palpite.get())
    
   if p>numero_aleatorio:
       contador = contador+1
       resultado.configure(text = 'O número secreto é menor.\nTente novamente.')
       
   elif p<numero_aleatorio:
       contador=contador+1
       resultado.configure(text = 'O número secreto é maior.\nTente novamente.')
       
   elif p == numero_aleatorio:
       contador=contador+1
       resultado.configure(text = f'Você acertou o número secreto em {contador} tentativas.\nParabéns!')


#========== JANELA ==========
ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.minsize(400,300)
janela.maxsize(400,300)
janela.title('𝗚𝗨𝗘𝗦𝗦 𝗧𝗛𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 - 𝗣𝗬𝗧𝗛𝗢𝗡')
janela.iconbitmap('minigame_python_logo.ico')


#========== LABEL 1 ==========
ctk.CTkLabel(
    janela,
    text='Advinhe o número!',
    text_color='#4682B4',
    font=('impact',40)
).pack(pady=10)


#========== LABEL 2 ==========
ctk.CTkLabel(
    janela,
    text='Insira o seu palpite. (0-100)',
    font=('arial',23)
).pack(pady=10)


#========== ENTRY PALPITE ==========
palpite = ctk.CTkEntry(
    janela,
    placeholder_text='',
    border_width=0,
    width=300,
    height=35
)
palpite.pack(pady=10)


#========== BOTÃO PALPITE ==========
botao_palpite=ctk.CTkButton(
    janela,
    text='OK',
    font=('impact',25),
    width=250,
    height=40,
    fg_color='#4682B4',
    hover_color='darkblue',
    command=advinhar,
)
botao_palpite.pack(pady=10)

#========== LABEL RESULTADO ==========
resultado = ctk.CTkLabel(
    janela,
    text='',
    font=('arial',20)
)
resultado.pack(pady=5)






janela.bind('<Return>', advinhar)
janela.mainloop()