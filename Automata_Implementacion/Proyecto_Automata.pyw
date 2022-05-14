
from cProfile import label
from tkinter import *
from tkinter import simpledialog
from pip import main;
from visual_automata.fa.dfa import VisualDFA
import pyttsx3;


#CREANDO EL MOTOR DE AUDIO
engine = pyttsx3.init(); 
engine.setProperty('volume',1.0)
engine.setProperty('rate', 125)

class App():

    #INICIALIZACION
    def __init__(self):
        self.idioma = True;
        self.raiz = Tk();
        self.raiz.geometry("750x550");
        self.raiz.title("AUTOMATA");
        self.raiz.resizable(False, False);
        self.raiz.config(background="#213141");
        self.main_title = Label(text="AUTOMATA FINITO DETERMINISTA (DFA)", font=("Cambria", 13), bg="#56CD63", fg="white", width="550", height="2");
        self.main_title.pack();

        #-------------------- CREANDO AUTOMATA -----------------------
        self.dfa = VisualDFA(
                        states= {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'},
                        input_symbols= {'a', 'b'},
                        transitions= {
                            'q0': {'a':'q1', 'b':'q2'},
                            'q1': {'a':'q4', 'b':'q5'},
                            'q2': {'a':'q3', 'b':'q7'},
                            'q3': {'a':'q3', 'b':'q7'},
                            'q4': {'a':'q7', 'b':'q6'},
                            'q5': {'a':'q7', 'b':'q7'},
                            'q6': {'a':'q4', 'b':'q5'},
                            'q7': {'a':'q7', 'b':'q7'}
                        },

                        initial_state= 'q0',
                        final_states={'q2', 'q3', 'q5'}
        )

        self.miFrame = Frame(self.raiz);
        self.Pantalla =Text(self.miFrame);
        
        self.Boton_Comprobar = Button(self.raiz, text="Introducir cadena", command=self.Funcion_Comprobar, width=20, height=1, bg="#006fff", fg="white");
        self.Boton_Comprobar.place(x=150, y=460);

        self.Boton_Limpiar = Button(self.raiz, text="Limpiar pantalla", command=self.Funcion_Clear_Pantalla, width=20, height=1, bg="#006fff", fg="white");
        self.Boton_Limpiar.place(x=400, y=460);

        self.Boton_Idioma = Button(self.raiz, text="Change language", command=self.Funcion_Idioma, width=20, height=1, bg="#006fff", fg="white");
        self.Boton_Idioma.place(x=275, y=500);


#----------------------------- FUNCION COMPROBAR ----------------------------------
    def Funcion_Comprobar(self):
        aux = str();
        if(self.idioma == True):
            engine.say("INGRESE LA CADENA A COMPROBAR");
            engine.runAndWait();
            engine.stop()

            try:
                cadena = simpledialog.askstring("Comprobar", "INGRESE LA CADENA: ");
                comprobar = str(self.dfa.input_check(cadena.lower()));

                comprobar = comprobar.replace("Accepted", "Aceptado");
                comprobar = comprobar.replace("Rejected", "Rechazado");
                comprobar = comprobar.replace("Step", "Pasos")
                comprobar = comprobar.replace("Current state", "Estado Actual")
                comprobar = comprobar.replace("Input symbol", "Símbolo de entrada")
                comprobar = comprobar.replace("New state", "Nuevo Estado")
                aux = comprobar.find("Aceptado");


                if( aux !=-1):
                    engine.say("CADENA INTRODUCIDA FUE ACEPTADA");
                
                else:
                    engine.say("CADENA INTRODUCIDA NO HA SIDO ACEPTADA");

                engine.runAndWait();
                engine.stop()

                self.Pantalla.insert(INSERT, comprobar+"\n\nCADENA INTRODUCIDA: "+cadena+"\n\n-------------------------------------------------------------------------");
                self.dfa.show_diagram(cadena).render('test-output/round-table.gv', view=True)
            
            except:
                self.Pantalla.insert(INSERT, "\nCADENA INCORRECTA, NO HA CUMPLE CON EL AUTOMATA\n\n-------------------------------------------------------------------------");
                engine.say("CADENA INTRODUCIDA NO CUMPLE CON EL AUTOMATA");
                engine.runAndWait();
                engine.stop()
        
        else:
            engine.say("ENTER STRING");
            engine.runAndWait();

            try:
                cadena = simpledialog.askstring("Check", "ENTER STRING: ");
                comprobar = str(self.dfa.input_check(cadena.lower()));

                self.Pantalla.insert(INSERT, comprobar+"\n\nINTRODUCED CHAIN: "+cadena+"\n\n-------------------------------------------------------------------------");

                aux = comprobar.find("Accepted");

                if( aux !=-1):
                    engine.say("ENTERED STRING WAS ACCEPTED");
                
                else:
                    engine.say("ENTERED STRING HAS NOT BEEN ACCEPTED");

                engine.runAndWait();
                engine.stop()
                self.dfa.show_diagram(cadena).render('test-output/round-table.gv', view=True)
            
            except:
                self.Pantalla.insert(INSERT, "\nINCORRECT CHAIN, DOES NOT COMPLY WITH THE AUTOMAT\n\n-------------------------------------------------------------------------");
                engine.say("INTRODUCED CHAIN DOES NOT COMPLY WITH THE AUTOMATION");
                engine.runAndWait();
                engine.stop()


#----------------------------- FUNCION LIMPIAR PANTALLA ----------------------------------

    def Funcion_Idioma(self):
        
        if(self.idioma == True):
            engine.say("DETERMINISTIC FINITE AUTOMATION");
            engine.runAndWait();
            self.idioma = False;
            self.main_title.config(text="DETERMINISTIC FINITE AUTOMATION (DFA)");
            self.raiz.title("AUTOMATON");
            self.Boton_Comprobar.config(text="enter string");
            self.Boton_Limpiar.config(text="Clean screen");
            self.Boton_Idioma.config(text="Cambiar idioma");
        else:
            engine.say("AUTOMATA FINITO DETERMINISTA");
            engine.runAndWait();
            self.idioma = True;
            self.raiz.title("AUTOMATA");
            self.main_title.config(text="AUTOMATA FINITO DETERMINISTA (DFA)");
            self.Boton_Comprobar.config(text="Introducir cadena");
            self.Boton_Limpiar.config(text="Limpiar pantalla");
            self.Boton_Idioma.config(text="Change language");

    def Funcion_Clear_Pantalla(self):
        self.Pantalla.delete("1.0", "end");
        if(self.idioma==True):
            engine.say("LIMPIANDO PANTALLA");
        else:
            engine.say("CLEANING SCREEN");
        engine.runAndWait();
        engine.stop()


    def ventana(self):
        self.miFrame.config(width=600, height=500);
        self.miFrame.pack();
        self.miFrame.propagate(0);

        
        #========================= PANTALLA =========================
        self.Pantalla.grid(row=3, column=0, padx=3, pady=3, stick="e");
        #self.Pantalla.insert(INSERT, "\t\t\tTODOS LOS ATRIBUTOS DE LOS ITEMS\n\n");
        
        

        #-------------- CREANDO EL SCROLL (Barra lateral) ----------------------
        self.scrollVert = Scrollbar(self.miFrame, command=self.Pantalla.yview); 
        self.scrollVert.grid(row=3, column=1, stick="nsew");
        self.Pantalla.config(yscrollcommand=self.scrollVert.set);

        #self.Pantalla.config(state='disabled');

        

        engine.say("AUTOMATA FINITO DETERMINISTA");
        engine.runAndWait();
        engine.stop()
        self.raiz.mainloop();

app = App();
app.ventana();

