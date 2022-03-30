
# --------------- ÁLVARO JAVIER PEDROZO PEÑA --------------
# ---------------- CODIG: 2018114053 --------


from cProfile import label
from operator import concat
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from typing import List
from pip import main;
from collections import OrderedDict;
import random;


#------------------- CREANDO LA VENTANA --------------------
ventana = Tk();
ventana.geometry("750x550");
ventana.title("LENGUAJE");
ventana.resizable(False, False);
ventana.config(background="#213141");
main_title = Label(text="TEORIA DE LENGUAJES", font=("Cambria", 13), bg="#56CD63", fg="white", width="550", height="2");
main_title.pack();


#------- PANTALLA 1 (PARA ALFABETOS) ---------
Pantalla_Label_1 = Label(ventana, text="ALFABETOS: ", font=("Cambria", 11), bg="#213141", fg="white" ,width=15, height=2);
Pantalla_Label_1.place(x=0, y=46);
Pantalla = Text(ventana, width=75, height=5);
Pantalla.place(x=2, y=80);

#AGREGANDO EL SCROLL PARA PANTALLA 1
scrollvertical_1 = Scrollbar(ventana, command=Pantalla.yview);
scrollvertical_1.place(x=610, y=80);


# ------ PANTALLA 2 (PARA LOS LENGUAJES) --------
Pantalla_Label_2 = Label(ventana, text="LENGUAJES: ", font=("Cambria", 11), bg="#213141", fg="white" ,width=15, height=3);
Pantalla_Label_2.place(x=0, y=270);
Pantalla_2 = Text(ventana, width=75, height=5);
Pantalla_2.place(x=2, y=310);

#AGREGANDO EL SCROLL PARA PANTALLA 2
scrollvertical_2 = Scrollbar(ventana, command=Pantalla_2.yview);
scrollvertical_2.place(x=610, y=310);


#---- LABEL DE ALFABETO ------
union_alfabet = Text(ventana, width=20, height=1);
union_alfabet.place(x=85, y=185);

Dif_alfabet = Text(ventana, width=20, height=1);
Dif_alfabet.place(x=350, y=185);

Int_alfabet = Text(ventana, width=20, height=1);
Int_alfabet.place(x=85, y=220);

Estrella_alfabet = Text(ventana, width=25, height=1);
Estrella_alfabet.place(x=385, y=220);


#---- LABEL DE LENGUAJE ------
union_Lenguaje = Text(ventana, width=30, height=1);
union_Lenguaje.place(x=85, y=410);

Dif_Lenguaje = Text(ventana, width=30, height=1);
Dif_Lenguaje.place(x=425, y=410);

Inter_Lenguaje = Text(ventana, width=30, height=1);
Inter_Lenguaje.place(x=85, y=445);

Potencia_Lenguaje = Text(ventana, width=38, height=1);
Potencia_Lenguaje.place(x=425, y=445);

Inversa_Lenguaje = Text(ventana, width=30, height=1);
Inversa_Lenguaje.place(x=92, y=480);

Cardinalidad_Lenguaje = Text(ventana, width=32, height=1);
Cardinalidad_Lenguaje.place(x=470, y=480);

Concat_Lenguaje = Text(ventana, width=79, height=1);
Concat_Lenguaje.place(x=93, y=515);

#---------- GUARDANDO LOS DATOS INTRODUCIDOS ------------
cantidad_1 = int();
cantidad_2 = int();
list_1 = [];
list_2 = [];



#----------------------- CREANDO LA CLASE ALFABETO --------------------------
class Alfabeto():
	list_Alfabeto_1 = [];
	list_Alfabeto_2 = [];

	#INSTANCIANDO LA CLASE
	def iniciar(self, arg1, arg2):
		self.list_Alfabeto_1 = arg1;
		self.list_Alfabeto_2 = arg2;


	#CREANDO EL METODO UNION DEL ALFABETO
	def Union(self):
		union = [];
		union = list(OrderedDict.fromkeys(self.list_Alfabeto_1+self.list_Alfabeto_2));
		return union;

		
	#CREANDO EL METODO INTERSECCION
	def Intercepcion(self):
		return (set(self.list_Alfabeto_1[:]).intersection(set(self.list_Alfabeto_2[:])));


	#CREANDO EL METODO DIFERENCIA
	def Diferencia(self, tipo):
		#COMPROBANDO SI EL ELEMENTO QUE ESTA EN LA LISTA 1 ES DIFERENTE O NO ESTA EN LA LISTA 2
		if(tipo == "a" or tipo == "A" or tipo == "1"):
			dif = [elem for elem in self.list_Alfabeto_1 if elem not in self.list_Alfabeto_2];
			return dif;
			
		
		elif(tipo == "b" or tipo == "B" or tipo == "2"):
			dif = [elem for elem in self.list_Alfabeto_2 if elem not in self.list_Alfabeto_1];
			return dif;
			

	#CREANDO EL METODO IMPRIMIR
	def imprimir(self):
		print("\n",self.list_Alfabeto_1,"\n",self.list_Alfabeto_2);


	def getList_1(self):
		aux1 = self.list_Alfabeto_1[:];
		return aux1;

	def getList_2(self):
		aux2 = self.list_Alfabeto_2[:];
		return aux2;
        
        

class Lenguaje(Alfabeto):
	List_Lenguaje_1 = [];
	List_Lenguaje_2 = [];

	def iniciar(self, arg1, arg2):
		super().iniciar(arg1, arg2);

		seleccion = simpledialog.askstring("Tipo Alfabeto", "SELECCIONE ENTRE A Y B PARA CREAR EL LENGUAJE");

		if(seleccion=='a' or seleccion=="1" or seleccion=="A"):
			cant = simpledialog.askinteger("cantidad", "INGRESE LA CANTIDAD DE PALABRAS PARA EL LENGUAJE:");

			for i in range(cant):
				self.List_Lenguaje_1.append(str(super().getList_1()[random.randint(0, (len(super().getList_1())-1))]     +    super().getList_1()[random.randint(0, (len(super().getList_1())-1))] ));
				self.List_Lenguaje_2.append(str(super().getList_1()[random.randint(0, (len(super().getList_1())-1))]     +    super().getList_1()[random.randint(0, (len(super().getList_1())-1))] ));


		elif(seleccion=='b' or seleccion=="2" or seleccion=="B"):
			cant = simpledialog.askinteger("cantidad", "INGRESE LA CANTIDAD DE PALABRAS PARA EL LENGUAJE:");

			for i in range(cant):
				self.List_Lenguaje_1.append(str(super().getList_2()[random.randint(0, (len(super().getList_2())-1))]     +    super().getList_2()[random.randint(0, (len(super().getList_2())-1))] ));
				self.List_Lenguaje_2.append(str(super().getList_2()[random.randint(0, (len(super().getList_2())-1))]     +    super().getList_2()[random.randint(0, (len(super().getList_2())-1))] ));

		return seleccion;

	def Union(self):
		aux_list = [];
		aux_list = list(OrderedDict.fromkeys(self.List_Lenguaje_1 + self.List_Lenguaje_2));
		return aux_list;


	def Intercepcion(self):
		return list(set(self.GetList_Lenguaje_1()) & set(self.GetList_Lenguaje_2()));

	def Diferencia(self, tipo):
		if(tipo == "a" or tipo == "A" or tipo == "1"):
			dif = [elem for elem in self.List_Lenguaje_1 if elem not in self.List_Lenguaje_2];
			return dif;
		
		elif(tipo == "b" or tipo == "B" or tipo == "2"):
			dif = [elem for elem in self.List_Lenguaje_2 if elem not in self.List_Lenguaje_1];
			return dif;

	def Concatenacion(self):
		aux1 = self.GetList_Lenguaje_1();
		aux2 = self.GetList_Lenguaje_2();

		concatenacion_lenguaje = [];

		for i in aux1:
			for j in aux2:
				aux3 = i + j;
				concatenacion_lenguaje.append(aux3);

		return concatenacion_lenguaje;


	def Inversa(self):
		selec = simpledialog.askstring("Inversa", "INDIQUE QUE LENGUAJE HALLARA SU INVERSA: ");

		if(selec == "a" or selec == "A" or selec == "1"):
			Lista_Inversa = [elem for elem in reversed(self.GetList_Lenguaje_1())];

		elif(selec == "b" or selec == "B" or selec == "2"):
			Lista_Inversa = [elem for elem in reversed(self.GetList_Lenguaje_2())];
			
		return Lista_Inversa;

	def Potencia(self, lista):
		if(len(lista) == 0):
			return [[]];
		
		
		#cont = cont + 1;
		r = self.Potencia(lista[:-1]);
		return r + [elem + [lista[-1]] for elem in r];
			

	def Cardinalidad(self):
		select = simpledialog.askstring("Cardinal", "INDIQUE EL LENGUAJE A CALCULAR EL CARDINAL: ");

		if(select == "a" or select == "A" or select == "1"):
			return len(self.List_Lenguaje_1);

		elif(select == "b" or select == "B" or select == "2"):
			return len(self.List_Lenguaje_2);


	def GetList_Lenguaje_1(self):
		return self.List_Lenguaje_1;
	
	def GetList_Lenguaje_2(self):
		return self.List_Lenguaje_2;




#-------------------CREANDO FUNCIONES PARA LAS OPCIONES DE MENU ----------------

#     FUNCION PARA SALIR DE LA VENTANA
def Salir_Aplicacion():
    valor = messagebox.askquestion("Salir" ,"¿Desea salir de la aplicacion?");
    if(valor == "yes"):
        ventana.destroy();


#     FUNCION PARA CREAR UN ALFABETO
def Crear_Alfabeto():
    cantidad_1 = simpledialog.askinteger("CANTIDAD A","INGRESE LA CANTIDAD DEL ALFABETO A: ");
    cantidad_2 = simpledialog.askinteger("CANTIDAD B","INGRESE LA CANTIDAD DEL ALFABETO B: ");
    
    for i in range(cantidad_1):
        list_1.append(str(simpledialog.askstring("SÍMBOLOS DE A","INGRESE LOS SÍMBOLOS DEL ALFABETO A: ")));
    
    for i in range(cantidad_2):
        list_2.append(simpledialog.askstring("SÍMBOLOS DE B","INGRESE LOS SÍMBOLOS DEL ALFABETO B: "));
    

    alfabeto.iniciar(list_1, list_2);
    Pantalla.insert(INSERT, "Alfabeto A:  ");
    Pantalla.insert(INSERT, list_1);
    Pantalla.insert(INSERT, "\nAlfabeto B:  ");
    Pantalla.insert(INSERT, list_2);
    

#-------------- FUNCION PARA CREAR EL LENGUAJE -------------
def Crear_Lenguaje():
	Pantalla_2.delete("1.0", "end");
	opcion = lenguaje.iniciar(alfabeto.getList_1(), alfabeto.getList_2());

	if(opcion == "a" or opcion == "1" or opcion == "A"):
		Pantalla_2.insert(INSERT, "CREADO DE A: ");
		Pantalla_2.insert(INSERT, str(alfabeto.getList_1()));
		Pantalla_2.insert(INSERT, "\nLENGUAJE A1: ");
		Pantalla_2.insert(INSERT, str(lenguaje.GetList_Lenguaje_1()));
		Pantalla_2.insert(INSERT, "\n");
		Pantalla_2.insert(INSERT, "LENGUAJE B1");
		Pantalla_2.insert(INSERT, str(lenguaje.GetList_Lenguaje_2()));

	elif(opcion == "b" or opcion == "2" or opcion == "B"):
		Pantalla_2.insert(INSERT, "CREADO DE B: ");
		Pantalla_2.insert(INSERT, str(alfabeto.getList_2()));
		Pantalla_2.insert(INSERT, "\nLENGUAJE A2: ");
		Pantalla_2.insert(INSERT, str(lenguaje.GetList_Lenguaje_1()));
		Pantalla_2.insert(INSERT, "\n");
		Pantalla_2.insert(INSERT, "LENGUAJE B1");
		Pantalla_2.insert(INSERT, str(lenguaje.GetList_Lenguaje_2()));


#----------- OPERACION DE FUNCIONES DE CONJUNTO PARA ALFABETO ----------------
def Funcion_Union_Alfabeto():
	union_alfabet.delete("1.0", "end");
	union_alfabet.insert(INSERT, alfabeto.Union());
	

def Funcion_Dif_Alfabeto():
	Dif_alfabet.delete("1.0", "end");
	tipo = simpledialog.askstring("Diferencia", "INGRESE EL FALBETO INICIAL: ");
	Dif_alfabet.insert(INSERT, alfabeto.Diferencia(tipo));

def Funcion_Inter_Alfabeto():
	Int_alfabet.delete("1.0", "end");
	Int_alfabet.insert(INSERT, str(alfabeto.Intercepcion()));

def Funcion_Estrella_Alfabeto():
    Estrella_alfabet.delete("1.0", "end");
    cant = simpledialog.askinteger("Cantidad", "INGRESE LA CANTIDAD FINITA DE PALABRAS:");
    lista = [];
    for i in range(cant):
        lista.append(str(list_1[random.randint(0, (len(list_1)-1))]     +    list_2[random.randint(0, (len(list_2)-1))] ));
    Estrella_alfabet.insert(INSERT, lista);
	


#----------- OPERACION DE FUNCIONES DE CONJUNTO PARA LENGUAJE ----------------
def Funcion_Union_Lenguaje():
	union_Lenguaje.delete("1.0", "end");
	union_Lenguaje.insert(INSERT, lenguaje.Union());

def Funcion_Dif_Lenguaje():
	Dif_Lenguaje.delete("1.0", "end");
	tipo = simpledialog.askstring("Diferencia", "INGRESE EL FALBETO INICIAL: ");
	Dif_Lenguaje.insert(INSERT, lenguaje.Diferencia(tipo));

def Funcion_Inter_Lenguaje():
	Inter_Lenguaje.delete("1.0", "end");
	Inter_Lenguaje.insert(INSERT, str(lenguaje.Intercepcion()));

def Funcion_Concat_Lenguaje():
	Concat_Lenguaje.delete("1.0", "end");
	Concat_Lenguaje.insert(INSERT, lenguaje.Concatenacion());

def Funcion_Potencia_Lenguaje():
	Potencia_Lenguaje.delete("1.0", "end");
	leng = simpledialog.askstring("Potencia", "ELIGA EL LENGUAJE: ");


	if(leng == "a" or leng == "A" or leng == "1"):
		pot = simpledialog.askinteger("Potencia", "INGRESE LA POTENCIA: ");
		
		lista_Potencia = lenguaje.Potencia( lenguaje.GetList_Lenguaje_1());
		
		if(pot == 0):
			
			Potencia_Lenguaje.insert(INSERT, str(lista_Potencia[0]));

		else:
			Potencia_Lenguaje.insert(INSERT, str(lista_Potencia[0:(pot+1)]));

	elif(leng == "b" or leng == "B" or leng == "2"):
		pot = simpledialog.askinteger("Potencia", "INGRESE LA POTENCIA: ");
		
		lista_Potencia = lenguaje.Potencia( lenguaje.GetList_Lenguaje_2());
		
		if(pot == 0):
			
			Potencia_Lenguaje.insert(INSERT, str(lista_Potencia[0]));

		else:
			Potencia_Lenguaje.insert(INSERT, str(lista_Potencia[:(pot+1)]));
						

def Funcion_Inversa_Lenguaje():
	Inversa_Lenguaje.delete("1.0", "end");
	Inversa_Lenguaje.insert(INSERT, str(lenguaje.Inversa()));

def Funcion_Cardinalidad_Lenguaje():
	Cardinalidad_Lenguaje.delete("1.0", "end");
	Cardinalidad_Lenguaje.insert(INSERT, str(lenguaje.Cardinalidad()));


#CREANDO BARRA DE MENU
barraMenu = Menu(ventana);
ventana.config(menu=barraMenu);

#ELEMENTOS DE LA BARRA DE MENU
archivo_Menu = Menu(barraMenu, tearoff=0);

#MOSTRANDO ELEMENTOS DE LA BARRA DE MENU
barraMenu.add_cascade(label="Archivo", menu=archivo_Menu);

#AGREGANDO LAS OPCIONES DEL MENU
archivo_Menu.add_command(label="Crear Alfabeto", command=Crear_Alfabeto);
archivo_Menu.add_command(label="Abrir Alfabeto");
archivo_Menu.add_separator();
archivo_Menu.add_command(label="Crear Lenguaje", command=Crear_Lenguaje);
archivo_Menu.add_command(label="Abrir Lenguaje");
archivo_Menu.add_separator();
archivo_Menu.add_command(label="Cerrar todo");
archivo_Menu.add_separator();
archivo_Menu.add_command(label="Salir", command=Salir_Aplicacion);


alfabeto = Alfabeto();
lenguaje = Lenguaje();


#-------------- CREANDO LOS BOTONES Y SUS ACCIONES -------------

#BOTONES PARA ALFABETO
Boton_Union_Alfabeto = Button(ventana, text="AUB (Union)", command=Funcion_Union_Alfabeto, width=10, height=1, bg="#006fff", fg="white");
Boton_Union_Alfabeto.place(x=2, y=185);

Boton_Dif_Alfabeto = Button(ventana, text="A-B (Dif)", command=Funcion_Dif_Alfabeto, width=10, height=1, bg="#006fff", fg="white");
Boton_Dif_Alfabeto.place(x=265, y=185);

Boton_Interc_Alfabeto = Button(ventana, text="A∩B (Inter)", command=Funcion_Inter_Alfabeto, width=10, height=1, bg="#006fff", fg="white");
Boton_Interc_Alfabeto.place(x=2, y=220);

Boton_Estrella_Alfabeto = Button(ventana, text="A∑*B (CER_ESTR)", command=Funcion_Estrella_Alfabeto, width=15, height=1, bg="#006fff", fg="white");
Boton_Estrella_Alfabeto.place(x=265, y=220);


#BOTONES PARA LENGUAJE
Boton_Union_Lenguaje = Button(ventana, text="AUB (Union)", command=Funcion_Union_Lenguaje, width=10, height=1, bg="#006fff", fg="white");
Boton_Union_Lenguaje.place(x=2, y=410);

Boton_Dif_Lenguaje = Button(ventana, text="A-B (Dif)", command=Funcion_Dif_Lenguaje, width=10, height=1, bg="#006fff", fg="white");
Boton_Dif_Lenguaje.place(x=340, y=410);

Boton_Interc_Lenguaje = Button(ventana, text="A∩B (Inter)", command=Funcion_Inter_Lenguaje, width=10, height=1, bg="#006fff", fg="white");
Boton_Interc_Lenguaje.place(x=2, y=445);

Boton_Potencia_Lenguaje = Button(ventana, text="A^n (Potencia)", command=Funcion_Potencia_Lenguaje, width=11, height=1, bg="#006fff", fg="white");
Boton_Potencia_Lenguaje.place(x=340, y=445);

Boton_Inversa_Lenguaje = Button(ventana, text=" A^-1 (Inversa)", command=Funcion_Inversa_Lenguaje, width=11, height=1, bg="#006fff", fg="white");
Boton_Inversa_Lenguaje.place(x=2, y=480);

Boton_Cardinalidad_Lenguaje = Button(ventana, text=" |A| (Cardinalidad)", command=Funcion_Cardinalidad_Lenguaje, width=15, height=1, bg="#006fff", fg="white");
Boton_Cardinalidad_Lenguaje.place(x=350, y=480);

Boton_Concat_Lenguaje = Button(ventana, text="A||B (Concat)", command=Funcion_Concat_Lenguaje, width=11, height=1, bg="#006fff", fg="white");
Boton_Concat_Lenguaje.place(x=2, y=515);


ventana.mainloop();