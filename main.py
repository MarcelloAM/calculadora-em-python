from tkinter import *
from tkinter import ttk

# Cores
cor1 = '#3b3b3b' # Cor Preta
cor2 = '#feffff' # Cor Branca
cor3 = '#38576b' # Azul
cor4 = '#ECEFF1' # Cor Cinzenta
cor5 = '#FFAB40' # Cor Laranja

# Criando Janela
janela = Tk()

# Definindo nome da Janela
janela.title('Calculadora')

# Definindo largura e comprimento da janela
janela.geometry('235x310')
janela.config(bg=cor1)

# Dividindo a tela da calculadora, sendo um para o display e outro para os botões (Frames)
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


dados = ''
valor_texto = StringVar()


def entrada_de_dados(numero):
    # Função para ler dados

    global dados

    dados = dados + str(numero)

    # Passando valor para a tela
    valor_texto.set(dados)


def calcular():
    # Função para calcular

    global dados
    resultado = eval(dados)
    valor_texto.set(str(resultado))


def limpar_tela():
    # Função para limpar a tela de dados

    global dados
    dados = ''
    valor_texto.set('')


# Criando Label

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Criando Botões
b_1 = Button(frame_corpo, command= lambda: limpar_tela(), text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrada_de_dados('%'), text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0) 
b_3 = Button(frame_corpo, command= lambda: entrada_de_dados('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command= lambda: entrada_de_dados('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)  
b_5 = Button(frame_corpo, command= lambda: entrada_de_dados('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)  
b_6 = Button(frame_corpo, command= lambda: entrada_de_dados('9'), text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)  
b_7 = Button(frame_corpo, command= lambda: entrada_de_dados('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command= lambda: entrada_de_dados('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)  
b_9 = Button(frame_corpo, command= lambda: entrada_de_dados('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)  
b_10 = Button(frame_corpo, command= lambda: entrada_de_dados('6'), text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)  
b_11 = Button(frame_corpo, command= lambda: entrada_de_dados('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command= lambda: entrada_de_dados('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)  
b_13 = Button(frame_corpo, command= lambda: entrada_de_dados('2'), text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)  
b_14 = Button(frame_corpo, command= lambda: entrada_de_dados('3'), text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)  
b_15 = Button(frame_corpo, command= lambda: entrada_de_dados('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156) 

b_16 = Button(frame_corpo, command= lambda: entrada_de_dados('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command= lambda: entrada_de_dados('.'), text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208) 
b_18 = Button(frame_corpo, command= lambda: calcular(),  text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()   

