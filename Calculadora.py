# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *



def play():

    raiz = Tk()
    raiz.title('Jogo da Forca')
    raiz.configure(background='blue') # para uma cor mais específica ver código hexadecimal
    raiz.geometry('700x600')
    raiz.resizable(True, True)
    raiz.maxsize(width=900, height=700)
    raiz.minsize(width=500, height=300)

    frame_1 = Frame(raiz) # bd = borda, bg = background,
    # highlightbackground = cor da borda do frame
    # highlightickness = tamanho da borda

    # place, pack, grid
    # pack é mais fácil de usar, mas não permite posicionamento específico
    # grid transforma a tela em várias linhas e colunas, permitindo posicionamento específico
    # place (x e y)
    frame_1.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.20) # parâmetros aceitam
    # numeros de 0 a 1- 0 é totalmente à esquerda e 1 à direita

    frame_2 = Frame(raiz)
    frame_2.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

    botao_0 = Button(frame_2, text= '0')
    botao_0.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.15)

    botao_1 = Button(frame_2, text='1')
    botao_1.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_2 = Button(frame_2, text='2')
    botao_2.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_3 = Button(frame_2, text='3')
    botao_3.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.15)

    mais = Button(frame_2, text='+')
    mais.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.15)


    variavel = Button(frame_2, text='y')
    variavel.place(relx=0.1, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_4 = Button(frame_2, text='4')
    botao_4.place(relx=0.26, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_5 = Button(frame_2, text='5')
    botao_5.place(relx=0.42, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_6 = Button(frame_2, text='6')
    botao_6.place(relx=0.58, rely=0.27, relwidth=0.15, relheight=0.15)

    menos = Button(frame_2, text='-')
    menos.place(relx=0.74, rely=0.27, relwidth=0.15, relheight=0.15)


    quadrado = Button(frame_2, text='a²')
    quadrado.place(relx=0.1, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_7 = Button(frame_2, text='7')
    botao_7.place(relx=0.26, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_8 = Button(frame_2, text='8')
    botao_8.place(relx=0.42, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_9 = Button(frame_2, text='9')
    botao_9.place(relx=0.58, rely=0.43, relwidth=0.15, relheight=0.15)

    igual = Button(frame_2, text='=')
    igual.place(relx=0.74, rely=0.43, relwidth=0.15, relheight=0.15)

    # label = Label(frame_2, text='Teste') LABEL É UM TEXTO SEM INTERAÇÃO
    # label.place(relx=0.1, rely=0.59)

    entry = Entry(frame_2)
    entry.place(relx=0.25, rely=0.9, relwidth=0.5)




    raiz.mainloop()


play()