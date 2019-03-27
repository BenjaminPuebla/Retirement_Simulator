
from tkinter import *


ven = Tk()

ven.title("Casi simulador")

ven.resizable(False, False)
#ven.config(width=400, height=650)

ven.config(width="400", height="650")

Label(ven, text="Simular una pension", font=(2)).place(x=120, y=12)


sueldo = DoubleVar()
Label(ven, text="Sueldo").place(x=86, y=190)
Entry(ven, textvariable=sueldo).place(x=210, y=190)

apv = DoubleVar()
Label(ven, text="Porcentaje APV").place(x=64, y=50)
Entry(ven, textvariable=apv).place(x=210, y=50)
Label(ven, text="%").place(x=194, y=50)

fondoActual = DoubleVar()
Label(ven, text="Fondo actual").place(x=68, y=85)
Entry(ven, textvariable=fondoActual).place(x=210, y=85)

edad = DoubleVar()
Label(ven, text="Edad").place(x=89, y=120)
Entry(ven, textvariable=edad).place(x=210, y=120)

comision = DoubleVar()
Label(ven, text="Comisión").place(x=78, y=155)
com = Entry(ven, textvariable=comision)
com.pack()
com.place(x=210, y=155)


Label(ven, text="%").place(x=194, y=155)

Label(ven, text="Sexo").place(x=89, y=225)

def sexo():
	if op.get() == 1:
		edadmuerte.set(85)
		edadJubilacion.set(60)
	else:
		edadmuerte.set(80)
		edadJubilacion.set(65)


op = IntVar()
s = Radiobutton(ven, text="Masculino", variable=op, value=2, command=sexo)
s.pack()
s.place(x=270, y=225)

s2 = Radiobutton(ven, text="Femenino", variable=op, value=1, command=sexo)
s2.pack()
s2.place(x=190, y=225)


Label(ven, text="¿Estimar edades?").place(x=54, y=260)

def desactivar():
	if respuesta.get() == 2:
		edadm.config(state="normal")
		edadj.config(state="normal")
		s.config(state="disable")
		s2.config(state="disable")
	else:
		edadm.config(state="disable")
		edadj.config(state="disable")
		s.config(state="normal")
		s2.config(state="normal")

respuesta = IntVar()
si = Radiobutton(ven, text="no", variable=respuesta, value=1, command=desactivar)
si.pack()
si.place(x=280, y=260)

no = Radiobutton(ven, text="si", variable=respuesta, value=2, command=desactivar)
no.pack()
no.place(x=230, y=260)

edadmuerte = DoubleVar()
Label(ven, text="Edad estimada de muerte").place(x=35, y=330)
edadm = Entry(ven, textvariable=edadmuerte, state="disable")
edadm.pack()
edadm.place(x=210, y=330)


edadJubilacion = DoubleVar()
Label(ven, text="Edad estimada de jubilación").place(x=30, y=295)
edadj = Entry(ven, textvariable=edadJubilacion, state="disable")
edadj.pack()
edadj.place(x=210, y=295)


def calcular():
	try:
		trabajando = edadJubilacion.get() - edad.get()
		jubilado = edadmuerte.get() - edadJubilacion.get()
		jubilacion.set(int( ( ( ( ( (sueldo.get() * 12 * trabajando * 1.2) * (0.1 + apv.get()/100 ) ) + fondoActual.get()) / 12) / jubilado)*(100 - comision.get())/100 ) )
	except:
		x = Tk()

		x.title("Casi simulador")

		x.resizable(False, False)
		#ven.config(width=400, height=650)

		x.config(width="250", height="200")

		Label(x, text="Porfavor ingrese datos veridicos", font=(2)).place(x=10, y =100)

jubilacion = DoubleVar()
pension = Entry(ven, textvariable=jubilacion)
pension.config(background="green", justify="center")
pension.place(x=210, y=375)
Label(ven, text="Pensión:").place(x=171, y=373)

botonCalcular = Button(ven, text="Calcular", command=calcular)
botonCalcular.pack()
botonCalcular.place(x=80, y=373)

Label(ven, text="_____________________________________________________________________").place(x=25, y=410)
Label(ven, text="Jubilacion deseada", font=(2)).place(x=120, y=440)

jubilacionEsperada = DoubleVar()
Label(ven, text="Jubilación esperada").place(x=52, y=480)
Entry(ven, textvariable=jubilacionEsperada).place(x=210, y=480)

def calcular2():
	try:	
		trabajando = edadJubilacion.get() - edad.get()
		jubilado = edadmuerte.get() - edadJubilacion.get()
		x = (((jubilacionEsperada.get()*12*jubilado)-fondoActual.get())/((sueldo.get()*12*trabajando*1.2))-(0.1))*100
		x = x - apv.get()
		y = ( (12*jubilacionEsperada.get() * edadmuerte.get()) - fondoActual.get() + (14.4*sueldo.get()*edad.get()*(0.1+apv.get())))/(((0.1+apv.get())*14.4*sueldo.get())+ (12*jubilacionEsperada.get() ) )
		y = y - edadJubilacion.get()
		Label(ven, text="Para alcanzar la jubilación deseada estipulada debe ").place(x=60, y=560)
		Label(ven, text="Aumentar su APV en ").place(x=60, y=580)
		Label(ven, text = "{0:.4f}".format(x)).place(x=180, y=580)
		Label(ven, text = "%").place(x=220, y=580)
		Label(ven, text = "o jubilarse en ").place(x=235, y=580)
		Label(ven, text = "{0:.4f}".format(x)).place(x=310, y=580)
	except:
		x = Tk()

		x.title("Casi simulador")

		x.resizable(False, False)
		#ven.config(width=400, height=650)

		x.config(width="250", height="200")

		Label(x, text="Porfavor ingrese datos veridicos", font=(2)).place(x=10, y =100)


botonCalcular2 = Button(ven, text="Calcular", command=calcular2)
botonCalcular2.pack()
botonCalcular2.place(x=160, y=515)


ven.mainloop()
