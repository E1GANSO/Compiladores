from tkinter import *
import xml.etree.ElementTree as ET;
from tkinter import filedialog
from tkinter import messagebox


# AUTOR:     ÁLVARO JAVIER PEDROZO PEÑA          #CODIGO: 2018114053

#CLASE APP
class App():

	#VARIABLES INICIALIZACION
	def __init__(self):
		self.contenido = str();
		self.Leer_Archivo = str();
		self.raiz = Tk();
		self.miFrame = Frame(self.raiz);
		self.Pantalla =Text(self.miFrame);
		self.tree = ET.parse('ZOO.xml');
		self.root = self.tree.getroot();

	def Obtener_contenido(self):
		return self.contenido;
	
	def Obtener_Leer_Archivo(self):
		return self.Leer_Archivo.get();
	
	def Set_Leer_Archivo(self, arc):
		self.Leer_Archivo = arc;

	def Obtener_Pantalla(self):
		return self.Pantalla;
	
	def Set_Pantalla(self):
		self.Pantalla.replace(self.Pantalla,"");

	def Obtener_Root(self):
		return self.root;


	#LEER ARCHIVO
	def Open_File(self):
		self.Leer_Archivo = filedialog.askopenfile(title="Abrir", filetypes=(("Archivos de XML", "*.xml"),("Todos los archivos","*.*")));
		self.Set_Leer_Archivo(self.Leer_Archivo);

		print(self.Leer_Archivo);


	#SALIR DE LA APLICACION
	def Exit_App(self):
		valor = messagebox.askquestion("Salir","¿Desea salir de la aplicacion?");
		if(valor=="yes"):
			self.raiz.destroy();

	#VER LOS PADRES Y CANTIDAD DE PADRES
	def Ver_Padres(self):
		aux_Padre = str(); cont = 0;
		
		for elem in self.root:
			aux_Padre = aux_Padre + elem.tag + "\n";
			cont = cont+1;
		
		messagebox.showinfo("Padre(s)", aux_Padre+"\n\n Total Padre(s): "+str(cont));

	#VER LOS HIJOS Y CANTIDAD DE HIJOS
	def Ver_Hijos(self):
		aux_Hijos = str(); cont = 0;
		
		for elem in self.root:
			for subElem in elem :
				aux_Hijos = aux_Hijos + subElem.text + "\n";
				cont = cont+1;
			aux_Hijos = aux_Hijos +"\n";
		messagebox.showinfo("Hijos(s)", aux_Hijos+"\n\n Total Hijo(s): "+str(cont));
	
	def Ver_Atributos(self):
		cont = 0;
		for elem in self.root:
			for subElem in elem :
				messagebox.showinfo(elem.tag, subElem.text+"\n"+str(subElem.attrib));
				cont = cont+1;
			

	#CREANDO LA INTERFACE DE USUARIO
	def ventana(self):
		self.raiz.iconbitmap('zoo.ico');
		self.raiz.geometry("700x500");
		self.raiz.title("Lector XML");
		self.raiz.config(bg="#0059b3");	

		self.miFrame.config(width=600, height=450);
		self.miFrame.pack();
		self.miFrame.propagate(0);


		#INICIO DE LECTURA DE ARBOL
		tree = ET.parse('ZOO.xml');
		root = tree.getroot();

		#CUADROS DE TEXTO
		self.Pantalla.grid(row=0, column=0, padx=3, pady=3, stick="e");
		self.Pantalla.insert(INSERT, "\t\t\tTODOS LOS ATRIBUTOS DE LOS ITEMS\n\n");
		self.Pantalla.insert(INSERT, (self.root.tag+"\n"));
		

		#MOSTRAR INFORMACION EN PANTALLA
		contenido = "\t";

		for elem in self.root:
			contenido = contenido + elem.tag+"\n\t\t";
			for subElemen in elem:
				contenido = contenido + subElemen.text;
			contenido = contenido+"\n\t";
		self.Pantalla.insert(INSERT, contenido);


		#CREANDO BARRA DE MENU
		barraMenu = Menu(self.raiz);
		self.raiz.config(menu=barraMenu);
		archivoMenu = Menu(barraMenu, tearoff=0);

		archivoMenu.add_command(label="Abrir archivo", command=self.Open_File);
		archivoMenu.add_command(label="Ver Padre(s)", command=self.Ver_Padres);
		archivoMenu.add_command(label="ver Hijo(s)", command=self.Ver_Hijos);
		archivoMenu.add_command(label="ver Atributo(s)", command=self.Ver_Atributos);
		archivoMenu.add_command(label="Cerrar archivo");
		archivoMenu.add_command(label="Salir", command=self.Exit_App);
		barraMenu.add_cascade(label="Archivo", menu=archivoMenu);


		#CREANDO EL SCROLL (Barra lateral)
		scrollVert = Scrollbar(self.miFrame, command=self.Pantalla.yview); 
		scrollVert.grid(row=0, column=1, stick="nsew"); 
		self.Pantalla.config(yscrollcommand=scrollVert.set);

		self.Pantalla.config(state='disabled');
		self.raiz.mainloop();

#INICIANDO APP
app = App();
app.ventana();

