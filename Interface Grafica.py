from tkinter import *
import controle_CSV as cc
import classe_matriz as cm

# Configurações da janela de interação com o usuario
app=Tk()
app.title("calculadora")  
app.geometry("500x300")
app.configure(background="#124")
     
# Caminho para o arquivo CSV que será usado para salvar a lista de matrizes
txt=Label(app,text="Origem do arquivo com as matrizes",background="#dde",foreground="#009")
txt.place(x=10,y=10,width=200,height=30)   
vorigem=Entry(app)
vorigem.place(x=10,y=30,width=200,height=20)

# Primeira matriz
txt=Label(app,text="Primeira matriz",background="#dde",foreground="#009")
txt.place(x=10,y=50,width=200,height=30)  
vprimeira=Entry(app) 
vprimeira.place(x=10,y=70,width=200,height=20)

# Tipo da primeira matriz
txt = Label(app, text = "Tipo 1", background = "#dde", foreground = "#009")
txt.place(x=210,y=50,width=200,height=30)  
tipo1 = Entry(app)
tipo1.place(x=210,y=70,width=200,height=20)

#Segunda matriz
txt=Label(app,text="Segunda matriz",background="#dde",foreground="#009")
txt.place(x=10,y=90,width=200,height=30)
vsegunda=Entry(app) 
vsegunda.place(x=10,y=110,width=200,height=20)

# Tipo da segunda matriz
txt = Label(app, text = "Tipo 2", background = "#dde", foreground = "#009")
txt.place(x=210,y=90,width=200,height=30)  
tipo2 = Entry(app)
tipo2.place(x=210,y=110,width=200,height=20)

# Escalar
txt=Label(app,text="Escalar",background="#dde",foreground="#009")
txt.place(x=10,y=130,width=200,height=30)  
vescalar=Entry(app) 
vescalar.place(x=10,y=150,width=200,height=20)

# Índice da matriz desejada na lista
txt=Label(app,text="Índice",background="#dde",foreground="#009")
txt.place(x=210,y=130,width=200,height=30)  
ind_m=Entry(app) 
ind_m.place(x=210,y=150,width=200,height=20)




# Lista das matrizes gravadas no arquivo CSV
matrix_l = []




## Printa a lista atual de matrizes
def show_list():
    print('\n')
    for i in range(len(matrix_l)):
        print(str(i) + ':\n')
        print('Tipo: ' + matrix_l[i].tag)
        print('Linhas: ' + str(matrix_l[i].n))
        print('Colunas: ' + str(matrix_l[i].m))
        print()
        print(matrix_l[i])
        if i != len(matrix_l) - 1:
            print('-----------------------------')
    print('\n')
    print('///////////////////')
    return




#Botão com cada um dos possiveis calculo de matrizes diponivel para o usuario

## Soma matricial
def funcaoadd():
    
    # Primeiro checamos se o usuário forneceu uma lista de índices de matrizes
    # da lista
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        # Caso tenha, buscamos as matrizes refentes aos índices na lista do
        # arquivo CSV
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        m2 = cc.getMatrix(vorigem.get(), int(ind_l[1]))
        
        # Soma as matrizes
        m = m1 + m2
        
        # Adiciona apenas o o resultado da soma na lista de matrizes, pois já
        # estamos usando matrizes que estão na lista para fazer o cálculo
        matrix_l.append(m)
        
    else:    
        # Converte o texto inserido pelo usuário em uma matriz
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        m2 = cc.str2matrix(vsegunda.get(), tipo2.get())
        
        # Soma as matrizes
        m = m1 + m2
        
        # Adiciona as matrizes usadas para o calculo e o resultado no final da
        # lista de matrizes
        matrix_l.extend((m1, m2, m))
    
    # Grava a lista atualizada no arquivo CSV
    cc.list2csv(vorigem.get(), matrix_l)
    show_list()
    
btn = Button(app, text="Adição", command = funcaoadd)
btn.place(x=0, y=200, width=100, height=20)




## Inversa
def funcaoinv():
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
    else:
        # Converte o texto da primeira matriz em uma matriz de fato
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
    
    # Computa a inversa da matriz e converte o resultado para a classe de
    # matrizes adequada
    m = m1.inv()
    m = cm.array_to_matriz(m)
    
    # Grava a lista atualizada no arquivo CSV
    matrix_l.extend((m1, m))
    cc.list2csv(vorigem.get(), matrix_l)
    
    show_list()
    
btn=Button(app,text="Inversa",command=funcaoinv)
btn.place(x=100,y=200,width=100,height=20)




## Multiplicação Matricial
def funcaomu():
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        m2 = cc.getMatrix(vorigem.get(), int(ind_l[1]))
        
        m = m1 * m2
        matrix_l.append(m)
    else:
        # Converte o texto inserido pelo usuário em uma matriz
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        m2 = cc.str2matrix(vsegunda.get(), tipo2.get())
    
        m = m1 * m2
        matrix_l.extend((m1, m2, m))
        
    cc.list2csv(vorigem.get(), matrix_l)
    show_list()

btn=Button(app,text="Multiplicação",command=funcaomu)
btn.place(x=200,y=200,width=100,height=20)




## Multiplicação por escalar
def funcaomu1():
    # Escalar passado pelo usuário
    s = float(vescalar.get())
    
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        m = m1 * s
        matrix_l.append(m)
    else:
        # Converte o texto inserido pelo usuário em uma matriz
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        m = m1 * s
        matrix_l.extend((m1, m))
        
    cc.list2csv(vorigem.get(), matrix_l)
    show_list()
    
btn=Button(app,text="Multiplicação por escalar",command=funcaomu1)
btn.place(x=300,y=200,width=150,height=20)




## Calcula a combinação linear de matrizes da lista a partir dos índices e dos 
 # escalares passados pelo úsuário
def funcaocl():
    
    # Transformando as strings passadas pelo usuario em listas de escalares e
    # índices de matrizes
    s_l = vescalar.get().split(',') # Lista de escalares
    ind_l = ind_m.get().split(',') # Lista de índices
    matrices = [] # Lista que irá conter a multiplicação dos escalares com as
                  # respectivas matrizes
    
    for i in range(len(s_l)):
        
        # Caso não seja passada uma lista de índices, usamos então as len(s_l)
        # primeiras matrizes da lista do arquivo CSV
        if ind_l == ['']:
            m = cc.getMatrix(vorigem.get(), i) * float(s_l[i])
        else:
            ind_l[i] = int(ind_l[i])
            m = cc.getMatrix(vorigem.get(), ind_l[i]) * float(s_l[i])
            
        matrices.append(m)
        
    # Por fim, calculamos a combinação linear somando todas as matrizes já 
    # computadas
    cl = matrices[0]
    for i in range(1, len(s_l)):
        cl += matrices[i]
        
    matrix_l.append(cl)
    show_list()
    
btn=Button(app,text="Combinação linear",command=funcaocl)
btn.place(x=0,y=230,width=120,height=20)




## Transposta
def funcaot():
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        m = m1.t()
        matrix_l.append(m)
    else:
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        m = m1.t()
        matrix_l.extend((m1, m))
        
    cc.list2csv(vorigem.get(), matrix_l)
    show_list()
    
btn=Button(app,text="Transposta",command=funcaot)
btn.place(x=120,y=230,width=100,height=20)




## Traço
def funcaof():
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        trace = m1.trace()
        print('Traço da matriz ' + ind_l[0] + ': ' + str(trace))
    else:
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        trace = m1.trace()
        print('Traço da primeira matriz: ' + str(trace))
    
btn=Button(app,text="Traço",command=funcaof)
btn.place(x=200,y=230,width=100,height=20)




## Determinante
def funcaodet():
    ind_l = ind_m.get().split(',')
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        det = m1.det()
        print('Determinante da matriz ' + ind_l[0] + ': ' + str(det))
    else:
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        det = m1.det()
        print('Determinante da primeira matriz: ' + str(det))
    
btn=Button(app,text="Determinante",command=funcaodet)
btn.place(x=300,y=230,width=100,height=20)




## Diagonalização
def funcaodiag():
    ind_l = ind_m.get().split(',')
    # print(cc.getMatrix(vorigem.get(), int(ind_l[0])))
    if ind_l != ['']:
        m1 = cc.getMatrix(vorigem.get(), int(ind_l[0]))
        m = m1.diag()
        matrix_l.extend((m[0], m[1]))
    else:
        m1 = cc.str2matrix(vprimeira.get(), tipo1.get())
        m = m1.diag()
        matrix_l.extend((m1, m[0], m[1]))
        
    cc.list2csv(vorigem.get(), matrix_l)
    show_list()
    
btn=Button(app,text="Diagonalização",command=funcaodiag)
btn.place(x=0,y=260,width=100,height=20)




## Adiciona a matriz escrita na primeira entrada na lista de matrizes do
 # arquivo CSV
def add_mat():
    m = cc.str2matrix(vprimeira.get(), tipo1.get())
    cc.add_matrix(vorigem.get(), m, matrix_l)
    show_list()

btn=Button(app,text="Adicionar na lista",command=add_mat)
btn.place(x=100,y=260,width=100,height=20)




## Zera a lista de matrizes do arquivo CSV
def del_list():
    global matrix_l
    matrix_l = []
    cc.list2csv(vorigem.get(), matrix_l)
    show_list()
    
btn=Button(app,text="Zerar lista",command=del_list)
btn.place(x=200,y=260,width=100,height=20)



    
btn=Button(app,text="Mostrar lista",command=show_list)
btn.place(x=300,y=260,width=100,height=20)




## Resgata a lista de matrizes do arquivo CSV passado pelo usuário
def getlist():
    global matrix_l
    matrix_l = cc.get_list(vorigem.get())
    show_list()
    
btn=Button(app,text="Resgatar lista",command=getlist)
btn.place(x=400,y=260,width=100,height=20)

app.mainloop()



