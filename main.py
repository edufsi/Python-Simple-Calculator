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
    
    def backspace():
        try:
            global text
            text = list(text)
            text.pop()
            ''.join(text)
            text = re.sub(r'[\[\]\'\, ]', '', str(text))
            contas.set(text)
        except IndexError:
            text = ''
           
        
       
            
        
    def apertar_botao(x):
        global text
        text = text + str(x)
        contas.set(text)
        
    def parenteses():
        global text
        expressoes = re.findall(r'\(.+\)', text)
        for expressions in expressoes:
            str_exp = str(expressions)
            total = eval(str_exp)
            text = re.sub(r'\(.+\)', '', text)
            text = text + str(total)
            
        
        
        
        
    def igual_a():
        global text
        try:
            text = text.replace('x', '*')
            text = text.replace('^', '**')
            parenteses()
          
            
            total = eval(text)
            text = str(total)
            contas.set(total)
        except SyntaxError:
            text = ''
            contas.set('Erro Aritmético')
            
    
    def clear_all():
        global text
        text = ''
        contas.set(text) 

    botao_0 = Button(frame_2, text= '0', command=lambda: apertar_botao(0))
    botao_0.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.15)

    botao_1 = Button(frame_2, text='1', command=lambda: apertar_botao(1))
    botao_1.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_2 = Button(frame_2, text='2',  command=lambda: apertar_botao(2))
    botao_2.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_3 = Button(frame_2, text='3',  command=lambda: apertar_botao(3))
    botao_3.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.15)

    mais = Button(frame_2, text='+', command=lambda: apertar_botao('+'))
    mais.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.15)


    botao_vezes = Button(frame_2, text='x', command=lambda: apertar_botao('x'))
    botao_vezes.place(relx=0.1, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_4 = Button(frame_2, text='4',  command=lambda: apertar_botao(4))
    botao_4.place(relx=0.26, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_5 = Button(frame_2, text='5', command=lambda: apertar_botao(5))
    botao_5.place(relx=0.42, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_6 = Button(frame_2, text='6',  command=lambda: apertar_botao(6))
    botao_6.place(relx=0.58, rely=0.27, relwidth=0.15, relheight=0.15)

    menos = Button(frame_2, text='-', command=lambda: apertar_botao('-'))
    menos.place(relx=0.74, rely=0.27, relwidth=0.15, relheight=0.15)

    divisão = Button(frame_2, text='/', command= lambda: apertar_botao('/'))
    divisão.place(relx=0.1, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_7 = Button(frame_2, text='7',  command=lambda: apertar_botao(7))
    botao_7.place(relx=0.26, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_8 = Button(frame_2, text='8',  command=lambda: apertar_botao(8))
    botao_8.place(relx=0.42, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_9 = Button(frame_2, text='9',  command=lambda: apertar_botao(9))
    botao_9.place(relx=0.58, rely=0.43, relwidth=0.15, relheight=0.15)

    igual = Button(frame_2, text='=', command=lambda: igual_a())
    igual.place(relx=0.74, rely=0.43, relwidth=0.15, relheight=0.15)
    
    abre_parenteses = Button(frame_2, text='(', command=lambda: apertar_botao('('))
    abre_parenteses.place(relx= 0.1, rely=0.59, relwidth= 0.15, relheight= 0.15)
    
    fecha_parenteses = Button(frame_2, text=')', command=lambda: apertar_botao(')'))
    fecha_parenteses.place(relx= 0.26, rely=0.59, relwidth= 0.15, relheight= 0.15)
    
    exponenciacao = Button(frame_2, text= '^', command=lambda: apertar_botao('^'))
    exponenciacao.place(relx= 0.42, rely=0.59, relwidth= 0.15, relheight= 0.15)

    backsplace= Button(frame_2, text= 'Back', command= lambda: backspace())
    backsplace.place(relx= 0.58, rely=0.59, relwidth= 0.15, relheight= 0.15)

    clear = Button(frame_2, text= 'C', command= lambda: clear_all(), background='#e83000', activebackground='#393d66')
    clear.place(relx= 0.74, rely=0.59, relwidth= 0.15, relheight= 0.15)

    raiz.mainloop()

if __name__ == '__main__':
    
    aplication()