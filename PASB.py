#INTERFAZ DE USUARIO
from tkinter import *
from tkinter import ttk,messagebox
from tkinter import font


class Usuario:
	def _init_(self,nombre,edad,altura,peso,sexo):
		self.nombre=nombre
		self.edad=int(edad)
		self.peso=float(peso)
		self.sexo=sexo
		self.altura=float(altura)

interfaz=Tk()
interfaz.geometry("1080x720")
interfaz.title("DIETA SALUDABLE")
interfaz.config(bg="green")
interfaz.resizable(width=0,height=0)

def validar():
	global name,high,age,weight,sex
	name=nombres.get()
	high=altura.get()
	age=edad.get()
	weight=peso.get()
	sex=sexo.get()
	def validarsexo(sex):
		if sex=="masculino" or sex=="femenino":
			return True
		else:
			return False

	if (age.isdigit() and high.isdigit() and validarsexo(sex)):
		return True
	else:
		messagebox.showinfo(message="ERROR DE DATOS",title="AVISO")
		return False

def ingreso():
	if (validar()):
		def regreso():
			ingresar.withdraw()
			interfaz.deiconify()		
		usuario=Usuario(name,age,high,weight,sex)
		interfaz.withdraw()
		ingresar=Toplevel()
		ingresar.geometry("1080x720")
		ingresar.title("BIENVENIDOS")
		ingresar.config(bg="purple")
		def imc():
			value=(usuario.peso/pow(usuario.altura,2))
			texto5.delete(0,END)
			texto5.insert(0,str(value))
		def mostrar():
			value="guillermo"
			texto5.delete(0,END)
			texto5.insert(0,str(value))

		texto5=Entry(ingresar,font="Arial 20",bg="yellow",justify="center")
		texto5.pack(pady=10,ipadx=150,ipady=70)
		
		boton2=Button(ingresar,text="INDICE DE MASA CORPORAL",font="Arial 35",command=imc,relief="raised",bd=5)
		boton2.pack(pady=10,ipadx=138,before=texto5)
		
		boton3=Button(ingresar,text="CANTIDAD DE AGUA INGERIBLE POR C/D",font="Arial 35",command=mostrar,relief="raised",bd=5)
		boton3.pack(pady=10,after=boton2)

		boton4=Button(ingresar,text="TABLA NUTRICIONAL DE ALIMENTOS",font="Arial 35",relief="raised",bd=5)
		boton4.pack(pady=10,ipadx=46,after=boton3)

		boton5=Button(ingresar,text="GASTO CALORICO",font="Arial 35",relief="raised",bd=5)
		boton5.pack(pady=10,ipadx=46,after=boton4)

		boton6=Button(ingresar,text="RETROCEDER",font="Arial 35",command=regreso,relief="raised",bd=5)
		boton6.pack(pady=10,ipadx=302,after=boton5)

		frase=Label(ingresar,text=f"BIENVENIDO {usuario.nombre.upper()}",font="Arial 35",bg="purple")
		frase.pack(before=boton2,pady=10)

		ingresar.mainloop()




frame=Frame(interfaz,bg="purple",width=1080,height=60)
frame1=Frame(interfaz,bg="purple",width=540,height=720)
frame2=Frame(interfaz,bg="purple",width=540,height=720)
frame.place(x=0,y=0)
frame1.place(x=0,y=60)
frame2.place(x=540,y=60)



titulo=Label(frame,text="DIETA SALUDABLE",font="Arial 40",justify="center",bg="purple")
titulo.place(x=300,y=0)

ingreset=Label(frame1,text="INGRESE SUS DATOS:",justify="left",fg="red",font="Arial 20",bg="purple")
ingreset.place(x=20,y=150)

nombrest=Label(frame1,text="NOMBRES: ",justify="left",fg="red",font="Arial 20",bg="purple")
nombrest.place(x=20,y=210)
nombres=Entry(frame1)
nombres.place(x=200,y=215 , height=25)

edadt=Label(frame1,text="EDAD :",justify="left",fg="red",font="Arial 20",bg="purple")
edadt.place(x=20,y=250)
edad=Entry(frame1)
edad.place(x=200,y=255 , height=25)

pesot=Label(frame1,text="PESO (kg):",justify="left",fg="red",font="Arial 20",bg="purple")
pesot.place(x=20,y=290)
peso=Entry(frame1)
peso.place(x=200,y=295 , height=25)

sexot=Label(frame1,text="SEXO :",justify="left",fg="red",font="Arial 20",bg="purple")
sexot.place(x=20,y=330)
sexo=ttk.Combobox(frame1, values=["masculino","femenino"], state="readonly")
sexo.place(x=200,y=335 , height=25,width=166)
sexo.current(0)

alturat=Label(frame1,text="ALTURA (cm): ",justify="left",fg="red",font="Arial 20",bg="purple")
alturat.place(x=20,y=370)
altura=Entry(frame1)
altura.place(x=200,y=375,height=25)

botonsito=Button(frame1,command=ingreso,text="VALIDAR DATOS",bd=5)
botonsito.place(x=200,y=415,width=166,height=50)

interfaz.mainloop()