
from tkinter import *
import re



text = ''
equ = False

def aplication():
    
    raiz = Tk()
    raiz.title('Calculadora')
    raiz.configure(background='#4040a1') 
    raiz.geometry('700x600')
    raiz.resizable(True, True)
    raiz.maxsize(width=900, height=700)
    raiz.minsize(width=500, height=300)
    
    contas = StringVar()
    label = Label(raiz, textvariable=contas, highlightthickness=3, highlightbackground='black', highlightcolor='black') # bd = borda, 
    
    label.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.20) 
    
    
    frame_2 = Frame(raiz, highlightthickness=3, highlightbackground='black', highlightcolor='black')
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
        global equ
        if equ:
            text = text + str('=')
            contas.set(text)
        
        else:
            try:
                text= text.replace(',', '.')
                text = text.replace('x', '*')
                text = text.replace('^', '**')
                parenteses()

            
                total = eval(text)
                text = str(total)
                text = text.replace('.', ',')
                contas.set(text)
            except SyntaxError:
                text = ''
                contas.set('Erro Aritmético')
            
            except ZeroDivisionError:
                text = ''
                contas.set('Erro: divisão por 0')
            
    
    def clear_all():
        global text
        text = ''
        contas.set(text) 
        
    
    def set_to_equation(pressed_button, raised_button=None, disabled_buttons=None):
        global equ
        equ = True
        
        pressed_button.config(relief=SUNKEN)
        
        raised_button.config(relief=RAISED)
        if disabled_buttons is not None:
            for button in disabled_buttons:
                button.config(state=ACTIVE)
            
           
    def set_to_expression(pressed_button, raised_button=None, disabled_buttons=None):
        global equ
        equ= False
       
        pressed_button.config(relief=SUNKEN)
        
        raised_button.config(relief=RAISED)
        if disabled_buttons is not None:
            for button in disabled_buttons: 
                button.config(state=DISABLED)
        
        
        
    def colocar_variavel():
        global equ
        global text
        if equ:
            text = text + 'y'
            contas.set(text)
        else:
            pass
        
    
    def solve_equation():
        global text
        equation = re.findall(r'(?:\d*\.?\d*y?(?=[^y\d])[\^\+\-/x]?)*=(?:\d*\.?\d*y?[\^\+\-/x]?)+', text)
        
        print(equation)
    
        

    divisao = Button(frame_2, text= '/', command=lambda: apertar_botao('/'), background='#82b74b')
    divisao.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.15)

    botao_1 = Button(frame_2, text='1', command=lambda: apertar_botao(1), background='#a2b9bc')
    botao_1.place(relx=0.26, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_2 = Button(frame_2, text='2',  command=lambda: apertar_botao(2), background='#a2b9bc')
    botao_2.place(relx=0.42, rely=0.1, relwidth=0.15, relheight=0.15)

    botao_3 = Button(frame_2, text='3',  command=lambda: apertar_botao(3), background='#a2b9bc')
    botao_3.place(relx=0.58, rely=0.1, relwidth=0.15, relheight=0.15)

    mais = Button(frame_2, text='+', command=lambda: apertar_botao('+'), background='#82b74b')
    mais.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.15)


    botao_vezes = Button(frame_2, text='x', command=lambda: apertar_botao('x'), background='#82b74b')
    botao_vezes.place(relx=0.1, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_4 = Button(frame_2, text='4',  command=lambda: apertar_botao(4), background='#a2b9bc')
    botao_4.place(relx=0.26, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_5 = Button(frame_2, text='5', command=lambda: apertar_botao(5), background='#a2b9bc')
    botao_5.place(relx=0.42, rely=0.27, relwidth=0.15, relheight=0.15)

    botao_6 = Button(frame_2, text='6',  command=lambda: apertar_botao(6), background='#a2b9bc')
    botao_6.place(relx=0.58, rely=0.27, relwidth=0.15, relheight=0.15)

    menos = Button(frame_2, text='-', command=lambda: apertar_botao('-'), background='#82b74b')
    menos.place(relx=0.74, rely=0.27, relwidth=0.15, relheight=0.15)

    exponenciacao = Button(frame_2, text='^', command= lambda: apertar_botao('^'), background='#82b74b')
    exponenciacao.place(relx=0.1, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_7 = Button(frame_2, text='7',  command=lambda: apertar_botao(7), background='#a2b9bc')
    botao_7.place(relx=0.26, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_8 = Button(frame_2, text='8',  command=lambda: apertar_botao(8), background='#a2b9bc')
    botao_8.place(relx=0.42, rely=0.43, relwidth=0.15, relheight=0.15)

    botao_9 = Button(frame_2, text='9',  command=lambda: apertar_botao(9), background='#a2b9bc')
    botao_9.place(relx=0.58, rely=0.43, relwidth=0.15, relheight=0.15)

    igual = Button(frame_2, text='=', command=lambda: igual_a(), background='#82b74b')
    igual.place(relx=0.74, rely=0.43, relwidth=0.15, relheight=0.15)
    
    abre_parenteses = Button(frame_2, text='(', command=lambda: apertar_botao('('), background='#82b74b')
    abre_parenteses.place(relx= 0.1, rely=0.59, relwidth= 0.15, relheight= 0.15)
    
    fecha_parenteses = Button(frame_2, text=')', command=lambda: apertar_botao(')'), background='#82b74b')
    fecha_parenteses.place(relx= 0.26, rely=0.59, relwidth= 0.15, relheight= 0.15)
    
    botao_0 = Button(frame_2, text= '0', command=lambda: apertar_botao('0'), background='#a2b9bc')
    botao_0.place(relx= 0.42, rely=0.59, relwidth= 0.15, relheight= 0.15)

    backsplace= Button(frame_2, text= 'Back', command= lambda: backspace(), background='#82b74b')
    backsplace.place(relx= 0.58, rely=0.59, relwidth= 0.15, relheight= 0.15)

    clear = Button(frame_2, text= 'C', command= lambda: clear_all(), background='#e83000', activebackground='#393d66')
    clear.place(relx= 0.74, rely=0.59, relwidth= 0.15, relheight= 0.15)

    variavel = Button(frame_2, text= 'y', command= lambda: colocar_variavel())
    variavel.place(relx= 0.42, rely=0.75, relwidth=0.15, relheight=0.15)
    
    equacao = Button(frame_2, text= 'Equação', command= lambda: set_to_equation(equacao, exp, [solve, variavel]))
    equacao.place(relx=0.26, rely=0.75, relwidth=0.15, relheight=0.15)
    
    exp = Button(frame_2, text= 'Expressão', command= lambda: set_to_expression(exp, equacao, [solve, variavel]))
    exp.place(relx=0.58, rely=0.75, relwidth=0.15, relheight=0.15)
    
    solve = Button(frame_2, text= 'Solve', command= lambda: solve_equation())
    solve.place(relx = 0.74, rely= 0.75, relheight= 0.15, relwidth= 0.15)
    
    dot = Button(frame_2, text=',', command= lambda: apertar_botao(','))
    dot.place(relx= 0.1, rely= 0.75, relheight=0.15, relwidth=0.15)
    
    
    
    raiz.mainloop()

if __name__ == '__main__':
    
    aplication()