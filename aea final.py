#INTERFAZ DE USUARIO
from io import BufferedRandom
from tkinter import *
from tkinter import ttk,messagebox
from tkinter import font
from PIL import ImageTk,Image
import matplotlib.pyplot as plt 
import copy



fichero=open("tablas.txt","r")
def procesar():
	fichero=open("tablas.txt","r")
	x=fichero.readlines()
	guardo=[]
	for j in x:
		reservar=[]
		letras=""
		numeros=[]
		j=j.replace("\t"," ")
		strralist=j.split(" ")
		for i in strralist:
			if i=="" or i==" ":
				pass
			else:
				if "\n" in i:
					i=i.replace("\n","")
				if "\t" in i:
					i=i.replace("\t","")
				i=i.strip()
				reservar.append(i)

		for i in reservar:
			try:
				if ("*" in i):
					numeros.append(i)
				float(i)
				numeros.append(i)
			except:
				if  not("*" in i):
					letras+=i
					letras+=" "
		numeros.insert(0,letras)
		guardo.append(numeros)
	fichero.close()
	return guardo

def archivo2():
	fichero2=open("actividad.txt","r")
	z=fichero2.readlines()
	guardo=[]
	for i in z:
		letras=""
		numeros=[]
		i=i.replace("\n","")
		strralist=i.split(" ")

		for i in strralist:
			try:
				float(i)
				numeros.append(i)
			except:
				letras+=i
				letras+=" "
		numeros.insert(0,letras)
		guardo.append(numeros)
	fichero.close()
	return guardo
tablasactivi=archivo2()
valor=procesar()
cereales=valor[2:20]
vegetales=valor[25:43]
frutas=valor[47:63]
carnes=valor[68:86]
pescados=valor[90:108]
lacteosyhuevo=valor[113:127]
bebidas=valor[134:143]
menestras=valor[149:156]
tuberculos=valor[160:174]
comidas=valor[178:219]
total=cereales+vegetales+frutas+carnes+pescados+lacteosyhuevo+bebidas+menestras+tuberculos+comidas
valorcitos=[]
valorcitos+=total
print(valorcitos)


class Usuario:
	def __init__(self,nombre,edad,altura,peso,sexo):
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
	if (age.isdigit() and high.isdigit() and weight.isdigit() and validarsexo(sex)):
		return True
	else:
		messagebox.showinfo(message="ERROR DE DATOS",title="AVISO")
		return False

def ingreso():
	if (validar()):
		usuario=Usuario(name,age,high,weight,sex)
		def regreso():
			ingresar.withdraw()
			interfaz.deiconify()				
		interfaz.withdraw()
		ingresar=Toplevel()
		ingresar.geometry("1080x720")
		ingresar.title("BIENVENIDOS")
		ingresar.config(bg="purple")
		valorcito=StringVar()

		def imc():
			value=(usuario.peso/pow(usuario.altura/100,2))
			valo2=""
			if (value<18.5):
				valo2="USTED SE ENCUENTRA EN UN ESTADO DE PESO DE DESNUTRICION"
			if (18.5<value<24.9):
				valo2="USTES SE ENCUENTRA EN UN ESTADO DE PESO NORMAL"
			if (24.9<value<29.9):
				valo2="USTED SE ENCUENTRA DENTRO DEL RANGO DE SOBREPESO"
			if (value>29.9):
				valo2="USTED SE ENCUENTRA DENTRO DEL RANGO DE OBESIDAD"
			valorcito.set("TU INDICE DE MASA CORPORTAL ES: "+str(value)+"\n"+valo2)

		def indiceagua():
			aguita=usuario.peso*0.035
			valorcito.set("USTED DEBE BEBER "+str(aguita)+" "+"LITROS DE AGUA CADA DIA")

		def tablas():
			ingresar.withdraw()
			ventana=Toplevel()
			ventana.title("TABLAS")
			ventana.geometry("1140x720")
			ventana.config(bg="#fb0")
			ventana.resizable(width=0,height=0)
			def regreso():
				ventana.withdraw()
				ingresar.deiconify()

			style=ttk.Style()
			style.configure("XD.Treeview",foreground="black",font="padmaa",background="yellow")
			tv=ttk.Treeview(ventana,columns=("c1","c2","c3","c4","c5","c6","c7","c8","c9","c10","c11"),style="XD.Treeview")
			tv.column("#0",width=200,anchor=CENTER)
			tv.column("c1",width=80,anchor=CENTER)
			tv.column("c2",width=80,anchor=CENTER)
			tv.column("c3",width=80,anchor=CENTER)
			tv.column("c4",width=80,anchor=CENTER)
			tv.column("c5",width=120,anchor=CENTER)
			tv.column("c6",width=80,anchor=CENTER)
			tv.column("c7",width=80,anchor=CENTER)
			tv.column("c8",width=80,anchor=CENTER)
			tv.column("c9",width=80,anchor=CENTER)
			tv.column("c10",width=80,anchor=CENTER)
			tv.column("c11",width=80,anchor=CENTER)
			tv.heading("#0", text="Alimento\n  (100g)", anchor=CENTER)
			tv.heading("c1",text="Energia\n  (cal)",anchor=CENTER)
			tv.heading("c2",text="Agua\n  (g)",anchor=CENTER)
			tv.heading("c3",text="Proteina\n     (g)",anchor=CENTER)
			tv.heading("c4",text="Grasa\n  (g)",anchor=CENTER)
			tv.heading("c5",text="Carbohidratos\n        (g)",anchor=CENTER)
			tv.heading("c6",text="Fibra\n  (g)",anchor=CENTER)
			tv.heading("c7",text="Calcio\n (mg)",anchor=CENTER)
			tv.heading("c8",text="Zinc\n (g)",anchor=CENTER)
			tv.heading("c9",text="Hierro\n   (g)",anchor=CENTER)
			tv.heading("c10",text="Sodio\n (mg)",anchor=CENTER)
			tv.heading("c11",text="Potasio\n   (mg)",anchor=CENTER)
			treeScroll = ttk.Scrollbar(ventana)
			treeScroll.configure(command=tv.yview)
			tv.configure(yscrollcommand=treeScroll.set)
			treeScroll.place(x=1120,y=0,height=720,width=20)		
						
			for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
					
			def vegetal():	
				global valorcitos
				valorcitos.clear()
				valorcitos+=vegetales
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
				print(id(valorcitos))
			def cereal():
				global valorcitos
				valorcitos=cereales
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
				print(id(valorcitos))
			def fruta():
				global valorcitos
				valorcitos=frutas
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
				print(id(valorcitos))
			def carne():
				global valorcitos
				valorcitos=carnes
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
			def pescado():
				global valorcitos
				valorcitos=pescados
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
			def lacteo():
				global valorcitos
				valorcitos=lacteosyhuevo
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
			def bebida():
				global valorcitos
				valorcitos=bebidas
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
			def menestra():
				global valorcitos
				valorcitos=menestras
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
			def tuberculo():
				global valorcitos
				valorcitos=tuberculos
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])
			def comida():
				global valorcitos
				valorcitos=comidas
				for i in tv.get_children():
						tv.delete(i)
				for i in valorcitos:
					tv.insert("",END,text=f"{i[0]}",values=i[1:])

			botoncito1=Button(ventana,text="CEREALES",command=vegetal,font="padmaa 13")
			botoncito1.place(x=0 , y=0,width=224,height=30)
			botoncito2=Button(ventana,text="VEGETALES",command=cereal,font="padmaa 13")
			botoncito1.place(x=0 , y=0,width=224,height=30)
			botoncito2.place(x=224 , y=0,width=224,height=30)
			botoncito3=Button(ventana,text="FRUTAS",command=fruta,font="padmaa 13")
			botoncito1.place(x=0 , y=0,width=224,height=30)
			botoncito3.place(x=448 , y=0,width=224,height=30)
			botoncito4=Button(ventana,text="CARNES",command=carne,font="padmaa 13")
			botoncito4.place(x=672 , y=0,width=224,height=30)
			botoncito5=Button(ventana,text="PESCADOS",command=pescado,font="padmaa 13")
			botoncito5.place(x=896 , y=0,width=224,height=30)
			botoncito6=Button(ventana,text="LACTEOS Y HUEVOS",command=lacteo,font="padmaa 12")
			botoncito6.place(x=0 , y=30,width=186,height=30)
			botoncito7=Button(ventana,text="BEBIDAS",command=bebida,font="padmaa 13")
			botoncito7.place(x=186 , y=30,width=186,height=30)
			botoncito8=Button(ventana,text="MENESTRAS",command=menestra,font="padmaa 13")
			botoncito8.place(x=372 , y=30,width=186,height=30)
			botoncito9=Button(ventana,text="TUBERCULOS",command=tuberculo,font="padmaa 13")
			botoncito9.place(x=558 , y=30,width=186,height=30)
			botoncito10=Button(ventana,text="COMIDAS",command=comida,font="padmaa 13")
			botoncito10.place(x=744, y=30,width=186,height=30)
			botoncito11=Button(ventana,text="REGRESAR",command=regreso,font="padmaa 13")
			botoncito11.place(x=930, y=30,width=190,height=30)
			tv.place(width=1120,height=600,y=60)
			def energy():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[1]=="*"):
						i[1]="0"
					guardo2.append(float(i[1]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("ENERGIA")
				fig.canvas.set_window_title("ENERGIA")
				plt.show()
			def water():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[2]=="*"):
						i[2]="0"
					guardo2.append(float(i[2]))
				fig, ax = plt.subplots()
				ax.set_title("AGUA")
				ax.barh(guardo, guardo2)
				fig.canvas.set_window_title("AGUA")
				plt.show()
			def protein():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[3]=="*"):
						i[3]="0"
					guardo2.append(float(i[3]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("PROTEINA")
				fig.canvas.set_window_title("PROTEINA")
				plt.show()
			def grease():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[4]=="*"):
						i[4]="0"
					guardo2.append(float(i[4]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("GRASA")
				fig.canvas.set_window_title("GRASA")
				plt.show()
			def carbohydrates():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[5]=="*"):
						i[5]="0"
					guardo2.append(float(i[5]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("CARBOHIDRATOS")
				fig.canvas.set_window_title("CARBOHIDRATOS")
				plt.show()
			def fiber():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[6]=="*"):
						i[6]="0"
					guardo2.append(float(i[6]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("FIBRA")
				fig.canvas.set_window_title("FIBRA")
				plt.show()
			def calcium():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[7]=="*"):
						i[7]="0"
					guardo2.append(float(i[7]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("CALCIO")
				fig.canvas.set_window_title("CALCIO")
				plt.show()
			def zincii():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[8]=="*"):
						i[8]="0"
					guardo2.append(float(i[8]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("ZINC")
				fig.canvas.set_window_title("ZINC")
				plt.show()
			def hierroo():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[9]=="*"):
						i[9]="0"
					guardo2.append(float(i[9]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("HIERRO")
				fig.canvas.set_window_title("HIERRO")
				plt.show()
			def sodic():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[10]=="*"):
						i[10]="0"
					guardo2.append(float(i[10]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("SODIO")
				fig.canvas.set_window_title("SODIO")
				plt.show()
			def potasic():			
				guardo=[]
				guardo2=[]
				for i in valorcitos:
					guardo.append(i[0])
					if (i[11]=="*"):
						i[11]="0"
					guardo2.append(float(i[11]))
				fig, ax = plt.subplots()
				ax.barh(guardo, guardo2)
				ax.set_title("POTASIO")
				fig.canvas.set_window_title("POTASIO")
				plt.show()
			def aaaa():
				print("alonso")


			botonc1=Button(ventana,text="ENERGIA",width=186,command=energy)
			botonc1.place(y=660,x=0,height=30,width=186.5)
			botonc2=Button(ventana,text="AGUA",command=water)
			botonc2.place(y=660,x=186,height=30,width=186)
			botonc3=Button(ventana,text="PROTEINA",command=protein)
			botonc3.place(y=660,x=372,height=30,width=186)
			botonc4=Button(ventana,text="GRASA",command=grease)
			botonc4.place(y=660,x=558,height=30,width=186)
			botonc5=Button(ventana,text="CARBOHIDRATOS",command=carbohydrates)
			botonc5.place(y=660,x=744,height=30,width=186)
			botonc6=Button(ventana,text="FIBRA",command=fiber)
			botonc6.place(y=660,x=930,height=30,width=190)
			botonc7=Button(ventana,text="CALCIO",command=calcium)
			botonc7.place(y=690,x=0,height=30,width=186)
			botonc8=Button(ventana,text="ZINC",command=zincii)
			botonc8.place(y=690,x=186,height=30,width=186)
			botonc9=Button(ventana,text="HIERRO",command=hierroo)
			botonc9.place(y=690,x=372,height=30,width=186)
			botonc10=Button(ventana,text="SODIO",command=sodic)
			botonc10.place(y=690,x=558,height=30,width=186)
			botonc11=Button(ventana,text="POTASIO",command=potasic)
			botonc11.place(y=690,x=744,height=30,width=186)
			botonc12=Button(ventana,text="",command=aaaa)
			botonc12.place(y=690,x=930,height=30,width=190)
			ventana.mainloop()


		def gastoporacti():
			ingresar.withdraw()
			ventana=Toplevel()
			diccionario=dict(tablasactivi)
			ventana.title("GASTO POR ACTIVIDAD")
			ventana.geometry("600x470")
			ventana.config(bg="purple")
			valuess=[]
			keys=[]
			for values in tablasactivi:
				valuess.append(values[1])
				keys.append(values[0])
			def regreso():
				ventana.withdraw()
				ingresar.deiconify()
			valorres=StringVar()
			valorres.set("COMPLETE LAS OPCIONES")
			def ratificar():
				try:
					float(entraditaa.get())
					value1=float(entraditaa.get())
					resultado=value1*float(diccionario[combo.get()])*usuario.peso
					valorres.set("LOS CALORIAS QUEMADAS SON:\n   "+str(resultado))
				except:
					messagebox.showinfo(message="ERROR INGRESE UN NUMERO",title="AVISO")
			etii=Label(ventana,text="SELECCIONE LA ACTIVIDAD FISICA:",bg="purple",font="padmaa 23")
			etii.pack(pady=10)
			combo=ttk.Combobox(ventana,values=keys,font="padmaa 19")
			combo.pack(pady=10)
			combo.current(0)
			etii2=Label(ventana,text="SELECCIONE LOS MINUTOS: ",bg="purple",font="padmaa 23")
			etii2.pack(pady=10)
			entraditaa=Entry(ventana,font="padmaa 21",bg="purple")
			entraditaa.pack(pady=10)
			ettitq=Label(ventana,bg="purple",font="padmaa 25",textvariable=valorres)
			ettitq.pack(pady=10)
			bton=Button(ventana,text="CALCULAR",command=ratificar,font="padmaa 20",relief="raised",bd=5)
			bton.place(y=400,x=20,width=270)
			vale=Button(ventana,text="RETROCEDER",command=regreso,font="padmaa 20",relief="raised",bd=5)
			vale.place(y=400,x=310,width=270)

		def factorm():
			ingresar.withdraw()
			ventana=Toplevel()
			ventana.title("FACTOR MEDIO")
			ventana.geometry("800x720")
			ventana.config(bg="purple")
			def regreso():
				ventana.withdraw()
				ingresar.deiconify()
			eti3=Label(ventana,text="¿CUANTAS HORAS REALIZA ACTIVIDADES LIGERAS?",font="padmaa 20",bg="purple")
			eti3.pack(pady=6)
			entrada3=Entry(ventana,bg="purple")
			entrada3.pack(pady=10,ipadx=200,ipady=6)
			eti4=Label(ventana,text="¿CUANTAS HORAS REALIZA ACTIVIDADES MODERADAS?",font="padmaa 20",bg="purple")
			eti4.pack(pady=10)
			entrada4=Entry(ventana,bg="purple")
			entrada4.pack(pady=10,ipadx=200,ipady=6)
			eti5=Label(ventana,text="¿CUANTAS HORAS REALIZA ACTIVIDADES INTENSAS?",font="padmaa 20",bg="purple")
			eti5.pack(pady=10)
			entrada5=Entry(ventana,bg="purple")
			entrada5.pack(pady=10,ipadx=200,ipady=6)
			eti1=Label(ventana,text="¿CUANTAS HORAS DUERME O DESCANSA?",font="padmaa 20",bg="purple")
			eti1.pack(pady=10)
			entrada1=Entry(ventana,bg="purple")
			entrada1.pack(pady=10,ipadx=200,ipady=6)
			eti2=Label(ventana,text="¿CUANTAS HORAS ESTA ACTIVO?",font="padmaa 20",bg="purple")
			eti2.pack(pady=10)
			entrada2=Entry(ventana,bg="purple")
			entrada2.pack(pady=10,ipadx=200,ipady=6)
			valorr=StringVar()

			def factormedi():
				global fma
				if (entrada1.get().isdigit() and entrada2.get().isdigit() and entrada3.get().isdigit() and entrada4.get().isdigit() and entrada5.get().isdigit()):
					if(float(entrada1.get())+float(entrada2.get())+float(entrada3.get())+float(entrada4.get())+float(entrada5.get())!=24):
						messagebox.showinfo(message="ERROR LAS HORAS DEBEN SER\n\t   24",title="AVISO")
					else:
						fma=float(entrada1.get())*1+float(entrada2.get())*1.5+float(entrada3.get())*2.5+float(entrada4.get())*5+float(entrada5.get())*7
						valorr.set(f"TU GASTO CALORICO POR DIA ES : {str(fma/24*tmr)}")
				else:
					messagebox.showinfo(message="ERROR DE TIPO DE DATOS",title="AVISO")
			botonn1=Button(ventana,text="CALCULAR ",command=factormedi,relief="raised",bd=5,font="padmaa 20")
			botonn1.place(x=50,y=650,width=325,height=43)
			botonn2=Button(ventana,text="RETROCEDER",command=regreso,relief="raised",bd=5,font="padmaa 20")
			botonn2.place(x=425,y=650,width=325,height=43)
			etiquetar=Label(ventana,textvariable=valorr,font="padmaa 20",bg="purple")
			etiquetar.pack(ipady=6)
			ventana.mainloop()
		if usuario.sexo=="masculino":
				tmr=66+13.7*usuario.peso+5*usuario.altura-6.8*usuario.edad
		elif usuario.sexo=="femenino":
				tmr=655+9.6*usuario.peso+1.8*usuario.altura-4.7*usuario.edad


		texto5=Label(ingresar,font="Suravaram 20",bg="green",justify="center",textvariable=valorcito,background="purple")
		texto5.pack(pady=8,ipadx=150,ipady=70)				
		boton2=Button(ingresar,text="INDICE DE MASA CORPORAL",font="padmaa 26",command=imc,relief="raised",bd=5)
		boton2.pack(pady=8,ipadx=138,before=texto5)	
		boton3=Button(ingresar,text="CANTIDAD DE AGUA INGERIBLE POR C/D",font="padmaa 26",command=indiceagua,relief="raised",bd=5)
		boton3.pack(pady=8,ipadx=35,after=boton2)
		boton4=Button(ingresar,text="TABLA NUTRICIONAL DE ALIMENTOS",font="padmaa 26",relief="raised",bd=5,command=tablas)
		boton4.pack(pady=8,ipadx=70,after=boton3)
		boton5=Button(ingresar,text="RETROCEDER",font="padmaa 26",command=regreso,relief="raised",bd=5)
		boton5.pack(pady=8,ipadx=260,after=boton4)
		frase=Label(ingresar,text=f"BIENVENIDO {usuario.nombre.upper()}",font="padmaa 26",bg="purple")
		frase.pack(before=boton2,pady=8)
		boton1=Button(ingresar,text="GASTO CALORICO POR DIA",font="padmaa 26",command=factorm,relief="raised",bd=5)
		boton1.pack(pady=8,ipadx=150,before=boton5)
		boton6=Button(ingresar,text="GASTO CALORICO POR ACTIVIDAD FISICA",font="padmaa 26",command=gastoporacti,relief="raised",bd=5)
		boton6.pack(before=boton5,pady=8,ipadx=25)
		ingresar.mainloop()

imagen=Image.open("aaa.png")
imagen=imagen.resize((540,640),Image.ANTIALIAS)
img=ImageTk.PhotoImage(imagen)

def redimensionar(direccion,tamaño):
	return ImageTk.PhotoImage(Image.open(direccion).resize(tamaño,Image.ANTIALIAS))

img2=redimensionar("aaa.png",(200,200)) #PARA AJUSTAR EL TAMAÑO DE LAS IMAGENES

frame=Frame(interfaz,bg="purple",width=1080,height=60)
frame1=Frame(interfaz,bg="purple",width=540,height=720)
frame2=Frame(interfaz,bg="purple",width=540,height=720)
frame.place(x=0,y=0)
frame1.place(x=0,y=60)
frame2.place(x=540,y=60)
fondo=Label(frame2,image=img,bg="purple")
fondo.place(x=0,y=0)
titulo=Label(frame,text="DIETA SALUDABLE",font=("Rachana",40),justify="center",bg="purple")
titulo.place(x=300,y=0)
ingreset=Label(frame1,text="INGRESE SUS DATOS:",justify="left",fg="black",font=('Suravaram',20),bg="purple")
ingreset.place(x=20,y=150)
nombrest=Label(frame1,text="NOMBRES: ",justify="left",fg="black",font="Suravaram 20",bg="purple")
nombrest.place(x=20,y=210)
nombres=Entry(frame1,bg="purple",font="padmaa 17")
nombres.place(x=200,y=222 ,width=300 , height=30)
edadt=Label(frame1,text="EDAD :",justify="left",fg="black",font="Suravaram 20",bg="purple")
edadt.place(x=20,y=250)
edad=Entry(frame1,bg="purple",font="padmaa 17")
edad.place(x=200,y=262 , height=30,width=300)
pesot=Label(frame1,text="PESO (kg):",justify="left",fg="black",font="Suravaram 20",bg="purple")
pesot.place(x=20,y=290)
peso=Entry(frame1,bg="purple",font="padmaa 17")
peso.place(x=200,y=302 , height=30,width=300)
sexot=Label(frame1,text="SEXO :",justify="left",fg="black",font="Suravaram 20",bg="purple")
sexot.place(x=20,y=330)
sexo=ttk.Combobox(frame1, values=["masculino","femenino","si","no"],state="readonly",font="Suravaram 20",background="purple")
sexo.place(x=200,y=342 , height=30,width=300)
sexo.configure(background="purple")
sexo.current(0)
alturat=Label(frame1,text="ALTURA (cm): ",justify="left",fg="black",font="Suravaram 20",bg="purple")
alturat.place(x=20,y=370)
altura=Entry(frame1,bg="purple",font="padmaa 17")
altura.place(x=200,y=382,height=30,width=300)
botonsito=Button(frame1,command=ingreso,text="VALIDAR DATOS",font="Suravaram 20",bd=5)
botonsito.place(x=200,y=425,width=300,height=50)
interfaz.mainloop()
