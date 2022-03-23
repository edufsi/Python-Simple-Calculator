



from tkinter import *

import re


text = ''

def aplication():
    
    raiz = Tk()
    raiz.title('Calculadora')
    raiz.configure(background='blue') # para uma cor mais específica ver código hexadecimal
    raiz.geometry('700x600')
    raiz.resizable(True, True)
    raiz.maxsize(width=900, height=700)
    raiz.minsize(width=500, height=300)
    
    contas = StringVar()
    label = Label(raiz, textvariable=contas) # bd = borda, bg = background,
    # highlightbackground = cor da borda do frame
    # highlightickness = tamanho da borda
    # place, pack, grid
    # pack é mais fácil de usar, mas não permite posicionamento específico
    # grid transforma a tela em várias linhas e colunas, permitindo posicionamento mais específico
    # place (trabalhando com x e y)
    
    label.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.20) # parâmetros aceitam
    # numeros de 0 a 1- 0 é totalmente à esquerda e 1 à direita
    
    
    frame_2 = Frame(raiz)
    frame_2.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)
    
    
    def numero(x):
        global text
        text = text + str(x)
        contas.set(text)
        
    
        
    def igual_a():
        global text
        text = re.sub(r'x', '*')
        total = eval(text)
        text = str(total)
        contas.set(total)
        

    botao_0 = Button(frame_2, text= '0', command=lambda: numero(0))
    botao_0.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.15)

    botao_1 = Button(frame_2, text='1', command=lambda: numero(1))
    botao_1.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_2 = Button(frame_2, text='2',  command=lambda: numero(2))
    botao_2.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_3 = Button(frame_2, text='3',  command=lambda: numero(3))
    botao_3.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.15)

    mais = Button(frame_2, text='+', command=lambda: numero('+'))
    mais.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.15)


    botao_vezes = Button(frame_2, text='x', command=lambda: numero('*'))
    botao_vezes.place(relx=0.1, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_4 = Button(frame_2, text='4',  command=lambda: numero(4))
    botao_4.place(relx=0.26, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_5 = Button(frame_2, text='5', command=lambda: numero(5))
    botao_5.place(relx=0.42, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_6 = Button(frame_2, text='6',  command=lambda: numero(6))
    botao_6.place(relx=0.58, rely=0.27, relwidth=0.15, relheight=0.15)

    menos = Button(frame_2, text='-', command=lambda: numero('-'))
    menos.place(relx=0.74, rely=0.27, relwidth=0.15, relheight=0.15)


    quadrado = Button(frame_2, text='a²')
    quadrado.place(relx=0.1, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_7 = Button(frame_2, text='7',  command=lambda: numero(7))
    botao_7.place(relx=0.26, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_8 = Button(frame_2, text='8',  command=lambda: numero(8))
    botao_8.place(relx=0.42, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_9 = Button(frame_2, text='9',  command=lambda: numero(9))
    botao_9.place(relx=0.58, rely=0.43, relwidth=0.15, relheight=0.15)

    igual = Button(frame_2, text='=', command=lambda: igual_a())
    igual.place(relx=0.74, rely=0.43, relwidth=0.15, relheight=0.15)

    # label = Label(frame_2, text='Teste') LABEL É UM TEXTO SEM INTERAÇÃO
    # label.place(relx=0.1, rely=0.59)






    raiz.mainloop()

if __name__ == '__main__':
    
    aplication()