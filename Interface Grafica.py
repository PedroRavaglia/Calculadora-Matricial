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

#cada funcao1 trocar por uma fc da calculadora
btn=Button(app,text="adição",command=funcao1)
btn.place(x=0,y=200,width=100,height=20)

btn=Button(app,text="Inversa",command=funcao1)
btn.place(x=100,y=200,width=100,height=20)

btn=Button(app,text="multiplicacao",command=funcao1)
btn.place(x=200,y=200,width=100,height=20)

btn=Button(app,text="multiplicacao por escalar",command=funcao1)
btn.place(x=300,y=200,width=150,height=20)

btn=Button(app,text="Combinação linear",command=funcao1)
btn.place(x=0,y=230,width=120,height=20)

btn=Button(app,text="Transposta",command=funcao1)
btn.place(x=120,y=230,width=100,height=20)

btn=Button(app,text="Traço",command=funcao1)
btn.place(x=200,y=230,width=100,height=20)

btn=Button(app,text="Determinante",command=funcao1)
btn.place(x=300,y=230,width=100,height=20)

btn=Button(app,text="Diagonalização",command=funcao1)
btn.place(x=0,y=260,width=100,height=20)



app.mainloop()
