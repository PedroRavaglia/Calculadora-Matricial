from tkinter import *

#Configurações da janela de interação com o usuario
app=Tk()
app.title("calculadora")  
app.geometry("500x300")
app.configure(background="#124")
     
              
txt=Label(app,text="Origem do arquivo com as matrizes",background="#dde",foreground="#009")
txt.place(x=10,y=10,width=200,height=30)   

vorigem=Entry(app)
vorigem.place(x=10,y=30,width=200,height=20)

txt=Label(app,text="primeira matriz",background="#dde",foreground="#009")
txt.place(x=10,y=50,width=200,height=30)  
 
vprimeira=Entry(app) 
vprimeira.place(x=10,y=70,width=200,height=20)
#
txt=Label(app,text="Segunda matriz",background="#dde",foreground="#009")
txt.place(x=10,y=90,width=200,height=30)
   
vsegunda=Entry(app) 
vsegunda.place(x=10,y=110,width=200,height=20)

txt=Label(app,text="Escalar",background="#dde",foreground="#009")
txt.place(x=10,y=130,width=200,height=30)  

vescalar=Entry(app) 
vescalar.place(x=10,y=150,width=200,height=20)

#Botão com cada um dos possiveis calculo de matrizes diponivel para o usuario

#cada funcao fazendo referencia aos calculos possiveis e salvando o resultado no final do arquivo
def funcaoadd(vorigem,vprimeira,vsegunda):
     a=index2matrix(vprimeira,vorigem)
     b=index2matrix(vsegunda,vorigem)
     c=__add__(l,c,a,b) #linha,coluna,matriz
     return add_row(c,vorigem)
btn=Button(app,text="adição",command=funcaoadd)
btn.place(x=0,y=200,width=100,height=20)

def funcaoinv(vorigem,vprimeira):
     a=index2matrix(vprimeira,vorigem)
     b=inv(l,c,a) #linha,coluna,matriz
     return add_row(b,vorigem)
btn=Button(app,text="Inversa",command=funcaoinv)
btn.place(x=100,y=200,width=100,height=20)

def funcaomu(vorigem,vprimeira,vsegunda):
     a=index2matrix(vprimeira,vorigem)
     b=index2matrix(vsegunda,vorigem)
     c=__mul__(l,c,a,b) #linha,coluna,matriz
     return add_row(c,vorigem)
btn=Button(app,text="multiplicacao",command=funcaomu)
btn.place(x=200,y=200,width=100,height=20)

def funcaomu1(vorigem,vprimeira,vescalar):
     a=index2matrix(vprimeira,vorigem)
     b=index2matrix(vescalar,vorigem)
     c=__mul__(l,c,a,b) #linha,coluna,matriz
     return add_row(c,vorigem)
btn=Button(app,text="multiplicacao por escalar",command=funcaomu1)
btn.place(x=300,y=200,width=150,height=20)

def funcaomu1(vorigem,vprimeira,vsegunda,vescalar):
     a=index2matrix(vprimeira,vorigem)
     b=index2matrix(vsegunda,vorigem)
     c=index2matrix(vescala,vorigem)
     d=__mul__(l,c,a,c[0])
     e=__mul__(l,c,b,c[1])
     f=__mul__(l,c,d,e) #linha coluna,matriz
     return add_row(f,vorigem)
btn=Button(app,text="Combinação linear",command=funcao1)
btn.place(x=0,y=230,width=120,height=20)

def funcaot(vorigem,vprimeira):
     a=index2matrix(vprimeira,vorigem)
     b=t(l,c,a) #linha,coluna,matriz
     return add_row(b,vorigem)
btn=Button(app,text="Transposta",command=funcaot)
btn.place(x=120,y=230,width=100,height=20)

def funcaof(vorigem,vprimeira):
     a=index2matrix(vprimeira,vorigem)
     b=trace(l,c,a) #linha,coluna,matriz
     return add_row(b,vorigem)
btn=Button(app,text="Traço",command=funcaof)
btn.place(x=200,y=230,width=100,height=20)

def funcaodet(vorigem,vprimeira):
     a=index2matrix(vprimeira,vorigem)
     b=det(l,c,a) #linha,coluna,matriz
     return add_row(b,vorigem)
btn=Button(app,text="Determinante",command=funcaodet)
btn.place(x=300,y=230,width=100,height=20)

def funcaodiag(vorigem,vprimeira):
     a=index2matrix(vprimeira,vorigem)
     b=diag(l,c,a) #linha,coluna,matriz
     return add_row(b,vorigem)
btn=Button(app,text="Diagonalização",command=funcaodiag)
btn.place(x=0,y=260,width=100,height=20)



app.mainloop()
