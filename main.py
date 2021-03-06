
from tkinter import *
import re
from xml.sax.handler import all_properties



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
    label = Label(raiz, textvariable=contas, highlightthickness=3, highlightbackground='black', highlightcolor='black') 
    
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
                contas.set('Erro Aritm??tico')
            
            except ZeroDivisionError:
                text = ''
                contas.set('Erro: divis??o por 0')
            
    
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
        variaveis = []
     
        global text
        
        equation = re.findall(r'(?:\d*\.?\d*y?(?=[^y\d])[\^\+\-/x]?)+(?<![=])=(?![=])(?:\d*\.?\d*y?[\^\+\-/x]?)+', text)
        

        
        if equation:
            lado_esquerdo = str(''.join(re.findall(r'(.+)=', text)))
            lado_direito = str(''.join(re.findall(r'=(.+)', text)))
            
            
            lado_esquerdo_valores = [x for x in  re.findall(r'[x/]?[+\-]*\d*\.?\d*y?(?:\^?\d+)?', lado_esquerdo) if x] #guarda numa lista todos os valores do lado esquerdo da equa????o
            
            lado_direito_valores = [x for x in re.findall(r'[x/]?[+\-]*\d*\.?\d*y?(?:\^?\d+)?', lado_direito) if x] #guarda numa lista todos os valores do lado direito da equa????o
            
            print(lado_direito_valores)
            print(lado_esquerdo_valores)
            for i, value in enumerate(lado_esquerdo_valores):
                if re.match(r'^[+\-x\/]?y', value):
                    value = list(value)
                    value.insert(value.index('y'), '1')
                    lado_esquerdo_valores[i] = ''.join(value)
            #ISOLANDO AS VARI??VEIS NO LADO ESQUERDO
            for value in lado_direito_valores: #Para cada valor no lado direito, se tiver y, vamos guard??-lo e tir??-lo do lado direito
                if 'y' in value:
            
                    variaveis.append(value)
                    lado_direito_valores.remove(value)
                

                
           
            for value in variaveis: #para cada valor separado, separar o coeficiente e parte literal para tratar o coeficiente ao pass??-lo para o outro lado (inverter a opera????o). Depois concatenar novamente os dois no lado esquerdo
                if not re.match(r'\d', str(value)):
                    value = list(value)
                    value.insert(value.index('y'), '1')
                    
                variavel = re.findall(r'y(?:^\d.?\d*)?', value)
               
                value = re.sub(r'y(?:^\d.?\d*)?', '', value)
                  
                if 'x' in value or '/' in value:
                        coeficiente = re.sub(r'[x/]', 'x' if '/' in value else '/', value)
                else: 
                    coeficiente = float(value) * -1

                    
                    lado_esquerdo_valores.append(str(coeficiente) + str(''.join(variavel)))
            
            
            
            
            #Resolvendo opera????ese Colocando os n??meros para o lado_direito.
            termo_independente = []
            for value in lado_esquerdo_valores:
                if not 'y' in value:
                    lado_esquerdo_valores.remove(value)
                    if 'x' in value:
                       
                        value = re.sub(r'x', '*', value)
                        
                    termo_independente.append(value)
                    print(termo_independente)
                    

            termo_independente = str(eval(''.join(termo_independente)))
            lado_esquerdo_valores.append(termo_independente)
            print(termo_independente)
                    #lado_esquerdo_valores.remove(value)
                    #if 'x' in value or '/' in value:
                      #  value = re.sub(r'[/x]', '/' if 'x' in value else 'x', value)
                    
            
                       # lado_direito_valores.append(value)
                    #else: 
                     #   value = float(value)
                      #  value = str(value * -1)
                       # if not '-' in value:
                        #    value = '+' + value
                       # lado_direito_valores.append(str(value))
                       
                   
                    
            print(lado_direito_valores)
            if lado_direito_valores: #Se n??o houver nada sobrando no lado direito, ele ?? 0, se tiver, ser?? um valor num??rico. Para calcular o valor num??rico do lado_direito ?? preciso substituir os s??mbolos colocados para facilitar o entendimento do usu??rio por operadores.
                lado_direito = re.sub(r'x', '*', ''.join(lado_direito_valores))
                
                lado_direito = eval(lado_direito)
            else:
                lado_direito = 0
            print(lado_direito)
            lado_esquerdo_valores.append(str(lado_direito * -1))
            
          
            print(lado_esquerdo_valores)
            
            numeros_com_y = []
            numeros = []
            for value in lado_esquerdo_valores: #para cada valor no lado esquerdo, separar aqueles sem vari??vel, com vari??vel e com vari??vel elevada a algum n??mero
                
                if not '^' in value:
                   
                    if 'y' in value:
                        numeros_com_y.append(re.sub(r'y', '', value)) #queremos os coeficientes para simplificar a equa????o
                        
                    else:
                        numeros.append(value)
            

            
                else:
                    pass
                
            print(numeros_com_y)
            print(numeros)
          
                
            numeros = eval(''.join(numeros)) 
            lado_direito = numeros * -1
            lado_esquerdo = eval(''.join(numeros_com_y)) 
            print(lado_esquerdo)
            print(lado_direito)
            y = lado_direito / lado_esquerdo
            contas.set(y)
        else:
            text = ''
            contas.set('Equa????o inv??lida')

    def botoes_numeros():
        numero = 1
        for linha in range(3):
            for coluna in range(3):
                botao = Button(frame_2, text=numero, command= lambda numero=numero: apertar_botao(numero), background='#a2b9bc')
                botao.place(relx=0.26 + 0.16 * coluna, rely= 0.1+ 0.16 * linha, relwidth=0.15, relheight=0.15)
                numero += 1
    
    botoes_numeros() 

    divisao = Button(frame_2, text= '/', command=lambda: apertar_botao('/'), background='#82b74b')
    divisao.place(relx=0.1, rely=0.1, relwidth=0.15,relheight=0.15)

    

    mais = Button(frame_2, text='+', command=lambda: apertar_botao('+'), background='#82b74b')
    mais.place(relx=0.74, rely=0.1, relwidth=0.15, relheight=0.15)


    botao_vezes = Button(frame_2, text='x', command=lambda: apertar_botao('x'), background='#82b74b')
    botao_vezes.place(relx=0.1, rely=0.27, relwidth=0.15, relheight=0.15)

    

    menos = Button(frame_2, text='-', command=lambda: apertar_botao('-'), background='#82b74b')
    menos.place(relx=0.74, rely=0.27, relwidth=0.15, relheight=0.15)

    exponenciacao = Button(frame_2, text='^', command= lambda: apertar_botao('^'), background='#82b74b')
    exponenciacao.place(relx=0.1, rely=0.43, relwidth=0.15, relheight=0.15)

   

    igual = Button(frame_2, text='=', command=lambda: igual_a(), background='#82b74b')
    igual.place(relx=0.74, rely=0.43, relwidth=0.15, relheight=0.15)
    
    abre_parenteses = Button(frame_2, text='(', command=lambda: apertar_botao('('), background='#82b74b')
    abre_parenteses.place(relx= 0.1, rely=0.59, relwidth= 0.15, relheight= 0.15)
    
    fecha_parenteses = Button(frame_2, text=')', command=lambda: apertar_botao(')'), background='#82b74b')
    fecha_parenteses.place(relx= 0.26, rely=0.59, relwidth= 0.15, relheight= 0.15)
    
    botao_0 = Button(frame_2, text= '0', command=lambda: apertar_botao('0'), background='#a2b9bc')
    botao_0.place(relx= 0.42, rely=0.59, relwidth= 0.15, relheight= 0.15)

    back_space= Button(frame_2, text= 'Back', command= lambda: backspace(), background='#82b74b')
    back_space.place(relx= 0.58, rely=0.59, relwidth= 0.15, relheight= 0.15)

    clear = Button(frame_2, text= 'C', command= lambda: clear_all(), background='#e83000', activebackground='#393d66')
    clear.place(relx= 0.1, rely=0.75, relwidth= 0.15, relheight= 0.15) 

    variavel = Button(frame_2, text= 'y', command= lambda: colocar_variavel())
    variavel.place(relx= 0.42, rely=0.75, relwidth=0.15, relheight=0.15)
    variavel.config(state=DISABLED)
    
    equacao = Button(frame_2, text= 'Equa????o', command= lambda: set_to_equation(equacao, exp, [solve, variavel]), background='#cccc99')
    equacao.place(relx=0.26, rely=0.75, relwidth=0.15, relheight=0.15)
    
    exp = Button(frame_2, text= 'Express??o', command= lambda: set_to_expression(exp, equacao, [solve, variavel]), background='#cccc99')
    exp.place(relx=0.58, rely=0.75, relwidth=0.15, relheight=0.15)
    exp.config(relief=SUNKEN)
    
    solve = Button(frame_2, text= 'Solve', command= lambda: solve_equation())
    solve.place(relx = 0.74, rely= 0.75, relheight= 0.15, relwidth= 0.15)
    solve.config(state=DISABLED)
    
    dot = Button(frame_2, text=',', command= lambda: apertar_botao(','), background='#82b74b')
    dot.place(relx= 0.74, rely= 0.59, relheight=0.15, relwidth=0.15)
    
    
    
    raiz.mainloop()

if __name__ == '__main__':
    
    aplication()