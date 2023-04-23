# importa la libreria
import os #se indica el sistema operativo a utilizar que es windows
from tkinter import StringVar
from ClaseProfesor import Profesor
from ClaseEstudiante import Estudiante
# ########Tkinter debemos primero importar la librería#############
# Se importa tkinter y se renombra a tk para que sea más fácil###########
import tkinter as tk
import tkinter.ttk as ttk
import datetime
app = tk.Tk() #ventana principal
# Variables globales de diversos tipos, que utiliza tkinter
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)
Monto = tk.StringVar(app)
Nombre = tk.StringVar(app)
Cedula = tk.StringVar(app)
CedulaEst = tk.StringVar(app)
CedulaProf = tk.StringVar(app)
CedulaMatri = tk.StringVar(app)
FechaN = tk.StringVar(app)
Celular = tk.StringVar(app)
descuento = tk.IntVar(app)
montosdescuento = tk.IntVar(app)
canmxpagar = tk.IntVar(app)
matrizEstudiantes = []  # Matriz que permite almacenar cada estudiante matriculado por filas en donde cada fila indica el número de estudiante, meses pagados y valor a pagar con descuentos
contadorEstudiantes = 1  # Variable entera que permite contar la cantidad de estudiantes matriculados
global profes
# variables del archivo txt para mostrar en ventana
PrimeraLinea = tk.StringVar(app)
EscribirTexto = tk.StringVar(app)
#  Obtenemos el largo y  ancho de la pantalla
wtotal = app.winfo_screenwidth()
htotal = app.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 1200
hventana = 600
#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal / 2 - wventana / 2)
pheight = round(htotal / 2 - hventana / 2)
app.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))  # dimensiones de la ventana
app.title("Sistema de Matrícula School Las Brisas de la Gloria.")  # Titulo ventana
app.configure(background="light blue")
##############Clase sigleton#######
# clase singleton para el nombre del negocio se usa una unica vez
class NombreCentroEducativo(object):
    class __NombreCentroEducativo:  # se crea la clase nombre negocio y solo va a tener una unica instancia en el programa
        # constructor de la clase
        def __init__(self):
            self.nombre = None  # variable nombre vacia

        def __str__(self):  # el str para que está siempre en la misma posición de memoria
            return self.nombre  # regresa lo almacenado en nombre
    instance = None  # no tiene valor
    def __new__(cls):  # se crea la instancia
        if not NombreCentroEducativo.instance:  # sino recibe parametro
            NombreCentroEducativo.instance = NombreCentroEducativo.__NombreCentroEducativo()  # la variable NombreCentroEducativo. instancia va aser igual al NombreCentroEducativo
        return NombreCentroEducativo.instance  # retorna el nombre con la instancia

    def __getattr__(self, nombre):  # los getters  que llaman a la instancia.
        return getattr(self.instance, nombre)  # devuelve lo almacenado en la instancia

    def __setattr__(self, nombre, valor):  # los __setattr__ que llaman a la instancia.
        return setattr(self.instance, nombre, valor)  ##devuelve lo almacenado en la instancia
 # función limpia consola
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # indica que se limpia pantalla en windows



