# importa la libreria
import os #se indica el sistema operativo a utilizar que es windows
from ClaseProfesor import Profesor
from ClaseEstudiante import Estudiante
from tkinter import StringVar

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
app.title("Sistema de Matrícula ")  # Titulo ventana
app.configure(background="light blue")
##############Clase sigleton#######
# clase singleton para el nombre del negocio se usa una unica vez
class NombreCentroEducativo(object):
    class __NombreCentroEducativo:
        def __init__(self):
            self.nombre = None

        def __str__(self):
            return self.nombre
    __instance = None
    def __new__(cls): # La función comprueba si ya existe una instancia de la clase interna
        if not cls.__instance:
            cls.__instance = cls.__NombreCentroEducativo()
        return cls.__instance
    def __getattr__(self, nombre):#se ejecuta cuando se accede a un atributo que no existe en una instancia de la clase
        return getattr(self.__instance, nombre) #retorna
    def __setattr__(self, nombre, valor): #se ejecuta cuando se establece un valor para un atributo en una instancia de la clase
        return setattr(self.__instance, nombre, valor)
 # función limpia consola
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # indica que se limpia pantalla en windows o en ubunto
    #############instancia sigleton para el nombre del colegio###
centro_educativo_singleton = NombreCentroEducativo()  # instancia del singleton
centro_educativo = NombreCentroEducativo()  # instancia del centro educativo
centro_educativo.nombre = "School Las Brisas de la Gloria."  # nombre del centro
Clear() #limpia consola
###########Funciones independientes################
def CargaDatosProfesores():
    # Uso de diccionario y tuplas para cargar datos de los profesores desde archivo txt
    auxProfes = dict() #almacena datos de p
    tupla = tuple() # se crea tupla vacia para que vaya almacenando temporalmente cada linea de archivo
    # se intenta abrir el archivo profesores
    try:
        f = open("profesores.txt", "r", encoding="utf-8")  # busca o abre fichero
    except FileNotFoundError:  # ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada
        print("¡El fichero no existe!")  # muestra mensaje
    else: #si el archivo existe se sigue ejecundo lo que este dentro del else
        contfilas = 0 # esta variable se usa para contar las filas usado
        for linea in f: #recorre la linea y se va a almacenar en la linea actual
            contfilas = contfilas + 1 # recorre  la fila y cuenta del número de filas que se han procesado.
            cont = 1 # llevar la cuenta del número de elementos en cada tupla
            tupla = linea.split() # el metodo split divide la linea en cada espacio en blanco y se almacena en tupla
            for tu in tupla:  #Se recorre cada elemento en la tupla utilizando otro bucle
                if cont == 1: # se usa if para comprobar el valor de la variable que incrementa en 1
                    auxProfes["Cedula" + str(contfilas)] = tu # se almacena lo guardado
                if cont == 2: #en este caso vuelve a comprobar el valor e incrementa
                    auxProfes["Nombre" + str(contfilas)] = tu # se almacena lo guardado
                if cont == 3: #en este caso vuelve a comprobar el valor e incrementa
                    auxProfes["FechaN" + str(contfilas)] = tu# se almacena lo guardado
                if cont == 4: #en este caso vuelve a comprobar el valor e incrementa
                    auxProfes["Celular" + str(contfilas)] = tu# se almacena lo guardado
                cont = cont + 1 # incrementa el valor de la variable
        # Cierra el fichero
        f.close()
        return auxProfes #retorna lo guardado en auxProfes
def CargaDatosEstudiantes():
    # Uso de diccionario y tuplas para cargar datos de los estudiantes desde archivo txt
    auxEstu = dict()
    tupla = tuple()
    # Lo asigna para mostrarlo en tkinter
    try: #excepcion, abre el fichero estudiantes
        f = open("estudiantes.txt", "r", encoding="utf-8")  # busca o abre fichero
    except FileNotFoundError:  # ocurre cuando se intenta acceder  aun fichero que no existe en la ruta indicada
        print("¡El fichero no existe!")  # muestra mensaje
    else:
        contfilas = 0
        for linea in f:#recorre la linea y se va a almacenar en la linea actual
            contfilas = contfilas + 1 # recorre  la fila y cuenta del número de filas que se han procesado.
            cont = 1  # llevar la cuenta del número de elementos
            tupla = linea.split() # separa espacios en blanco
            for tu in tupla: #Se recorre cada elemento en la tupla utilizando otro bucle
                if cont == 1:  #en este caso vuelve a comprobar el valor e incrementa
                    auxEstu["Cedula" + str(contfilas)] = tu # se almacena lo guardado
                if cont == 2:  #en este caso vuelve a comprobar el valor e incrementa
                    auxEstu["Nombre" + str(contfilas)] = tu# se almacena lo guardado
                if cont == 3: #en este caso vuelve a comprobar el valor e incrementa
                    auxEstu["FechaN" + str(contfilas)] = tu# se almacena lo guardado
                if cont == 4: #en este caso vuelve a comprobar el valor e incrementa
                    auxEstu["Celular" + str(contfilas)] = tu# se almacena lo guardado
                cont = cont + 1  #incrementa el valor de la variable
        # Cierra el fichero
        f.close()
        return auxEstu #retorna lo guardado en auxEstu
# Captura la opción seleccionada en el menú principal para la ventana
# mostrar el siguiente menú
def OptionMenu_Select(event):
    if obMenu.get() == "Mantenimientos": #Cuenta con opcion mantenimientos
        MostrarMenuMantenimientos() #llama lo que se guarda en
    elif obMenu.get() == "Matrícula de estudiantes": #Cuenta con opcion matricula estudiante
        MostrarMenuMatricula() #llama lo que se guarada en
    elif obMenu.get() == "Salir": #Cuenta con  opcion salir
        app.destroy()
# Función para limpiar las variables con datos del profesor y estudiante
def LimpiarCampos():
    Cedula.set("")
    CedulaProf.set("")
    CedulaEst.set("")
    CedulaMatri.set("")
    Nombre.set("")
    FechaN.set("")
    Celular.set("")
#  Pantalla para incluir, modificar o eliminar profesores
def MantenimientoProfesores():
    #  Función para salir de la ventana de mantenimiento de profesores
    def SalirVentanaProfesores():
        newWindowM.destroy()

    #  Función para crear y guardar el archivo txt
    def GuardarArchivoTxt():
        from tkinter import messagebox ## Importa la función "messagebox" del módulo "tkinter"
        with open("profesores.txt", "w") as file:# Abre el archivo "profesores.txt" en modo escritura ("w") y lo asigna a la variable "file"
            for profe in profes.items():   # Recorre cada elemento (tupla) en el diccionario "profes"
                if profe[0][0:6] == "Cedula":# Verifica si la clave comienza con "Cedula"
                    subcadena = profe[0][6:7] # Obtiene el número de la subcadena
                    file.write(profes["Cedula" + subcadena] + " " + profes["Nombre" + subcadena] + " " + ## Escribe los valores correspondientes a la tupla en el archivo, separados por espacios y seguidos de un salto de línea
                               profes["FechaN" + subcadena] + " " + profes["Celular" + subcadena] + "\n")
            #  SE OBTIENE LA RUTA DEL PATH DONDE SE GUARDAN LOS ARCHIVOS
            ruta = os.getcwd()
            messagebox.showinfo(parent=newWindowM,       # Muestra una ventana emergente ("messagebox") con un mensaje
                                message="Archivo estudiantes.txt actualizado con éxito en la ruta " + ruta,
                                title="Información")

    #  Cargar cajas de texto
    def LlenarCajasTexto(e):
        booEncontro = False # Crea una variable booEncontro y la inicializa como false
        for profe in profes.items():# Recorre cada elemento (tupla) en el diccionario "profes"
            if profe[1] == CedulaProf.get():# Verifica si el valor de la clave "Cedula" es igual al valor del cuadro de texto "CedulaProf"
                subcadena = profe[0][6:7] # Obtiene el número de la subcadena
                Nombre.set(profes["Nombre" + subcadena])# Asigna los valores correspondientes a los cuadros de texto nombre, FechaN y Celular
                FechaN.set(profes["FechaN" + subcadena])
                Celular.set(profes["Celular" + subcadena])
                booEncontro = True            # Cambia el valor de booEncontro a True

                break # Sale del bucle "for"
        # Verifica si no se encontró el profesor y establece los valores de los cuadros de texto en blanco
        if booEncontro == False:
            Nombre.set("")
            FechaN.set("")
            Celular.set("")

    #  Función para guardar datos del profesor
    def GuardarDatosProfesor():
        from tkinter import messagebox ## Importa la función "messagebox" del módulo "tkinter"
        booEncontro = False# Crea una variable booEncontro y la inicializa como false
        resp = messagebox.askyesno(parent=newWindowM, message="¿Desea guardar el registro?", title="Guardar") #muestra un mensaje emergente que pregunta al usuario si desea guardar el registro y almacena su respuesta en la variable resp
        if resp:                #verifica si la variable "resp" es verdadera.
            if len(profes) > 0: #verifica si la longitud de la lista profes es mayor que cero
                for profe in profes.items(): #itera a través de los elementos de la lista profes y los almacena en la variable profe
                    if profe[1] == CedulaProf.get():   #verifica si el segundo elemento de la tupla profe es igual al valor obtenido de la función get del objeto CedulaProf
                        subcadena = profe[0][6:7] # almacena una subcadena de la primera cadena de la tupla profe que se encuentra entre los índices 6 y 7.
                        Nombre.set(profes["Nombre" + subcadena]) # Asigna los valores correspondientes a los cuadros de texto nombre, FechaN y Celular
                        FechaN.set(profes["FechaN" + subcadena])
                        Celular.set(profes["Celular" + subcadena])
                        booEncontro = True# Cambia el valor de booEncontro a True
                        break #cierra el bucle

                if booEncontro: #verifica la variable
                    messagebox.showwarning(parent=newWindowM, message="Profesor ya está registrado", title="Alerta") #Muestra un mensaje de advertencia al usuario indicando que el profesor ya está registrado
                else:
                    if CedulaProf.get() == "" or Nombre.get() == "" or FechaN.get() == "" or Celular.get() == "": #se verifica si todos los campos requeridos estan llenos
                        messagebox.showerror(parent=newWindowM, message="Faltan datos para el registro", title="Error")#Si falta alguno, se muestra un mensaje de error
                    else:
                        for profe1 in profes.items(): #Recorre la lista de profes y verifica el último número utilizado para el registro.
                            if profe1[0][0:6] == "Cedula": #Verifica si esta correcto que comienza con la cedula
                                subcadena1 = profe1[0][6:7]# Obtiene el último número utilizado para el registro.
                                longitud = int(subcadena1)

                        profes["Cedula" + str(longitud + 1)] = CedulaProf.get() #Agrega la nueva cédula a la lista
                        profes["Nombre" + str(longitud + 1)] = Nombre.get() #agrega nuevo nombre
                        profes["FechaN" + str(longitud + 1)] = FechaN.get()#agrega nueva fecha nacimiento
                        profes["Celular" + str(longitud + 1)] = Celular.get()# agrega nuevo celular
                        GuardarArchivoTxt()# guarda archivo
                        LimpiarCampos() # llama a la función que se encaraga de limpiar los campos cedula, nombre, fechanaci, y celular
                        messagebox.showinfo(parent=newWindowM, message="Registro guardado con éxito", #muestra mensaje  que el registro se guardo con exito
                                            title="Información")
            else:
                if CedulaProf.get() == "" or Nombre.get() == "" or FechaN.get() == "" or Celular.get() == "":#se verifican los datos
                    messagebox.showerror(parent=newWindowM, message="Faltan datos para el registro", title="Error")# si faltan datos, da un mensaje de error
                else: #si los datos estan completos se ejecuta lo seguinte
                    profes["Cedula1"] = CedulaProf.get() ##Agrega la nueva cédula a la lista
                    profes["Nombre1"] = Nombre.get()#Agrega el nombre nuevo a la lista
                    profes["FechaN1"] = FechaN.get()#Agrega la nueva fechanacimiento a la lista
                    profes["Celular1"] = Celular.get()#Agrega celular1 a la lista
                    GuardarArchivoTxt() #guarda los archivos
                    LimpiarCampos() #limpia los campos d etexto
                    messagebox.showinfo(parent=newWindowM, message="Registro guardado con éxito", title="Información")#muestra mensaje  que el registro se guardo con exito

    #  Función para eliminar datos del profesor
    def EliminarDatosProfesor():
        from tkinter import messagebox## Importa la función "messagebox" del módulo "tkinter"
        booEncontro = False  # Crea una variable booEncontro y la inicializa como false
        resp = messagebox.askyesno(parent=newWindowM, message="¿Desea eliminar el registro?", title="Eliminar") ##Muestra un mensaje al usuario si desea eliminar el registro
        if resp:#Se verifica si la respuesta del usuario
            if CedulaProf.get() == "":# verifica el numero de la cedula
                messagebox.showerror(parent=newWindowM, message="Faltan el número de cédula para eliminar el registro", #si no es correcta la cedula o no esta muestra mensaje error
                                     title="Error")
            else:
                for profe in profes.items():#Este es un bucle que recorre todos los elementos del diccionario
                    if profe[1] == CedulaProf.get():#Se verifica si el valor del campo Cedula es igual al valor que se encuentra en el campo
                        subcadena = profe[0][6:7]#e extrae la subcadena que representa el número de registro del profesor a eliminar
                        profes.pop("Cedula" + subcadena)#Se eliminan los elementos del diccionario "profes" cedula, nombre, fecha, cular
                        profes.pop("Nombre" + subcadena)
                        profes.pop("FechaN" + subcadena)
                        profes.pop("Celular" + subcadena)
                        booEncontro = True #Se cambia el valor de la variable "booEncontro" a "True", indicando que se ha encontrado el profesor que se quiere eliminar
                        GuardarArchivoTxt()#guarda el archivo
                        LimpiarCampos()#limpia los campos del archivo
                        break #cierra el bucle

                if booEncontro: #Si se encontró el profesor a eliminar, se ejecuta lo siguiente
                    messagebox.showinfo(parent=newWindowM, message="Registro eliminado con éxito",#Muestra una ventana emergente con un mensaje de información indicando que se ha eliminado el registro exitosamente.
                                        title="Información")
                else:
                    messagebox.showwarning(parent=newWindowM, message="Profesor no está registrado", title="Alerta")#muestra mensaje que el profesor no esta registrado

    #  Función para actualizar datos del profesor
    def ActualizarDatosProfesor():
        from tkinter import messagebox # Importa la función "messagebox" del módulo "tkinter"
        booEncontro = False # Crea una variable booEncontro y la inicializa como false
        resp = messagebox.askyesno(parent=newWindowM, message="¿Desea actualizar el registro?", title="Actualizar")##Muestra un mensaje al usuario si desea actualizar los datos
        if resp:#Se verifica si la respuesta del usuario
            if CedulaProf.get() == "" or Nombre.get() == "" or FechaN.get() == "" or Celular.get() == "": #el código comprueba si los campos de la cédula, nombre, fecha de nacimiento y número de celular están vacíos. Si alguno de estos campos está vacío, muestra un mensaje de error
                messagebox.showerror(parent=newWindowM, message="Faltan datos para actualizar el registro",
                                     title="Error")
            else:
                for profe in profes.items():##Este es un bucle que recorre todos los elementos del diccionario
                    if profe[1] == CedulaProf.get():# y busca el registro que coincide con la cédula ingresada por el usuario
                        subcadena = profe[0][6:7]#se extrae la subcadena que representa el número de registro cedula, nombre, fechana, celular
                        profes.update({"Cedula" + subcadena: CedulaProf.get()})
                        profes.update({"Nombre" + subcadena: Nombre.get()})
                        profes.update({"FechaN" + subcadena: FechaN.get()})
                        profes.update({"Celular" + subcadena: Celular.get()})
                        GuardarArchivoTxt()#guarda archivo
                        LimpiarCampos()#limpia los campos de archivo
                        booEncontro = True
                        break #cierra bucle

                if booEncontro:
                    messagebox.showinfo(parent=newWindowM, message="Registro actualizado con éxito",# si encuantra registro, muestra mensaje que el registro se actualizo con exito
                                        title="Información")
                else:
                    messagebox.showwarning(parent=newWindowM, message="Profesor no está registrado", title="Alerta")# muestra mensaje alerta que el profezsor no esta registrado

    # Uso Toplevel para crear una nueva ventana
    newWindowM = tk.Toplevel()
    newWindowM.title("Catálogo de Profesores")# titulo de la ventana
    #  Obtenemos el largo y  ancho de la pantalla
    wtotalmant = newWindowM.winfo_screenwidth()
    htotalmant = newWindowM.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventanamant = 400
    hventanamant = 350
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidthmant = round(wtotalmant / 2 - wventanamant / 2)
    pheightmant = round(htotalmant / 2 - hventanamant / 2)
    newWindowM.geometry(str(wventanamant) + "x" + str(hventanamant) + "+" + str(pwidthmant) + "+" + str(
        pheightmant))  # dimensiones de la ventana
    newWindowM.transient(app)
    iconoM = tk.PhotoImage(file="tesis.png")
    newWindowM.iconphoto(True, iconoM)
#Creación de etiquetas y botones para ingreso datos profesor
    # para etiqueta cédula.
    tk.Label(
        newWindowM,
        text="Cédula",
        fg="white",   # se le asigna color texto
        bg="blue",   # se le asigna color fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    #  Comando para llamar a la función cuando se presiona la tecla Enter
    #  si el profesor existe se llenan los campos restantes
    vcmd = (newWindowM.bind('<Return>', LlenarCajasTexto))
    # Se digita el # de cédula
    tk.Entry(
        newWindowM,
        bg="yellow",  #  # se le asigna color fondo
        fg="blue",  #  # se le asigna color texto
        relief="sunken", validatecommand=vcmd,
        justify="center",
        textvariable=CedulaProf
    ).pack()
    # para etiqueta nombre del profesor en ventana.
    tk.Label(
        newWindowM,  #se asigna la ventana donde aparecerá
        text="Nombre", #el texto que lleva etiqueta
        fg="white",  #  # se le asigna color texto
        bg="blue",  #  # se le asigna color fondo
        font=("Verdana", 14),
        anchor="center", # el texto centrado
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se digita el nombre del profesor
    tk.Entry(
        newWindowM, # indica la ventana donde va adigitar
        bg="yellow",  # asigna color al fondo
        fg="blue",  #  # se le asigna color texto
        relief="sunken",
        justify="center",
        textvariable=Nombre
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,  # fill llena el both
        expand=False,
    )
    # para etiqueta fecha de nacimiento del profesor.
    tk.Label(
        newWindowM,
        text="Fecha de nacimiento", #la etiqueta va  a aprecer con fecha nacimiento
        fg="white",  # se le asigna color texto
        bg="blue",  # se le asigna color  al fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se digita la fecha de nacimiento del profesor
    tk.Entry(
        newWindowM,
        bg="yellow",   # se le asigna color fondo
        fg="blue",   # se le asigna color texto
        relief="sunken",
        justify="center",
        textvariable=FechaN
    ).pack()
    # para etiqueta número de celular del profesor.
    tk.Label(
        newWindowM,
        text="# Celular",
        fg="white",  # # se le asigna color texto
        bg="blue",  #  # se le asigna color fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se digita el número de celular del profesor
    tk.Entry(
        newWindowM,
        bg="yellow",  #  # se le asigna color fondo
        fg="blue",  #  # se le asigna color texto
        relief="sunken",
        justify="center",
        textvariable=Celular
    ).pack()
    # Llama a la función de guardado de datos del profesor.
    tk.Button(
        newWindowM,
        text="Guardar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  #  # se le asigna color fondo
        fg="white",  # color texto
        command=GuardarDatosProfesor,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    # Llama a la función de eliminar datos del profesor.
    tk.Button(
        newWindowM,
        text="Eliminar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  #  # se le asigna color fondo
        fg="white",  # color texto
        command=EliminarDatosProfesor,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    # Llama a la función de actualización de datos del profesor.
    tk.Button(
        newWindowM,
        text="Actualizar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  # cambia color al fondo
        fg="white",  # color texto
        command=ActualizarDatosProfesor,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    # Llama a la función para salir de la ventana de profesores.
    tk.Button(
        newWindowM,
        text="Salir",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  # cambia color de fondo
        fg="white",  # color texto
        command=SalirVentanaProfesores,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )

#  Pantalla para incluir, modificar,mostrar o eliminar estudiantes
def MantenimientoEstudiantes():
    #  Función para salir de la ventana de mantenimiento de estudiantes
    def SalirVentanaEstudiantes():
        newWindowE.destroy()

    #  Función para crear y guardar el archivo txt
    def GuardarArchivoTxt():
        from tkinter import messagebox
        with open("estudiantes.txt", "w") as file:
            for estu in estudiantes.items():
                if estu[0][0:6] == "Cedula":
                    subcadena = estu[0][6:7]
                    file.write(estudiantes["Cedula" + subcadena] + " " + estudiantes["Nombre" + subcadena] + " " +
                               estudiantes["FechaN" + subcadena] + " " + estudiantes["Celular" + subcadena] + "\n")
            #  SE OBTIENE LA RUTA DEL PATH DONDE SE GUARDAN LOS ARCHIVOS
            ruta = os.getcwd()
            messagebox.showinfo(parent=newWindowE,
                                message="Archivo estudiantes.txt actualizado con éxito en la ruta " + ruta,
                                title="Información")
    #  Cargar cajas de texto
    def LlenarCajasTexto(e):
        booEncontro = False
        for estu in estudiantes.items():
            if estu[1] == CedulaEst.get():
                subcadena = estu[0][6:7]
                Nombre.set(estudiantes["Nombre" + subcadena])
                FechaN.set(estudiantes["FechaN" + subcadena])
                Celular.set(estudiantes["Celular" + subcadena])
                booEncontro = True
                break

        if booEncontro == False:
            Nombre.set("")
            FechaN.set("")
            Celular.set("")

    #  Función para guardar datos del Estudiante
    def GuardarDatosEstudiante():
        from tkinter import messagebox
        booEncontro = False
        resp = messagebox.askyesno(parent=newWindowE, message="¿Desea guardar el registro?", title="Guardar")
        if resp:
            if len(estudiantes) > 0:
                for estu in estudiantes.items():
                    if estu[1] == CedulaEst.get():
                        subcadena = estu[0][6:7]
                        Nombre.set(estudiantes["Nombre" + subcadena])
                        FechaN.set(estudiantes["FechaN" + subcadena])
                        Celular.set(estudiantes["Celular" + subcadena])
                        booEncontro = True
                        break
                if booEncontro:
                    messagebox.showwarning(parent=newWindowE, message="Estudiante ya está registrado", title="Alerta")
                else:
                    if CedulaEst.get() == "" or Nombre.get() == "" or FechaN.get() == "" or Celular.get() == "":
                        messagebox.showerror(parent=newWindowE, message="Faltan datos para el registro", title="Error")
                    else:
                        for estu1 in estudiantes.items():
                            if estu1[0][0:6] == "Cedula":
                                subcadena1 = estu1[0][6:7]
                                longitud = int(subcadena1)

                        estudiantes["Cedula" + str(longitud + 1)] = CedulaEst.get()
                        estudiantes["Nombre" + str(longitud + 1)] = Nombre.get()
                        estudiantes["FechaN" + str(longitud + 1)] = FechaN.get()
                        estudiantes["Celular" + str(longitud + 1)] = Celular.get()
                        GuardarArchivoTxt()
                        LimpiarCampos()
                        messagebox.showinfo(parent=newWindowE, message="Registro guardado con éxito",
                                            title="Información")
            else:
                if CedulaEst.get() == "" or Nombre.get() == "" or FechaN.get() == "" or Celular.get() == "":
                    messagebox.showerror(parent=newWindowE, message="Faltan datos para el registro", title="Error")
                else:
                    estudiantes["Cedula1"] = CedulaEst.get()
                    estudiantes["Nombre1"] = Nombre.get()
                    estudiantes["FechaN1"] = FechaN.get()
                    estudiantes["Celular1"] = Celular.get()
                    GuardarArchivoTxt()
                    LimpiarCampos()
                    messagebox.showinfo(parent=newWindowE, message="Registro guardado con éxito", title="Información")

    #  Función para eliminar datos del estudiante
    def EliminarDatosEstudiante():
        from tkinter import messagebox
        booEncontro = False
        resp = messagebox.askyesno(parent=newWindowE, message="¿Desea eliminar el registro?", title="Eliminar")
        if resp:
            if CedulaEst.get() == "":
                messagebox.showerror(parent=newWindowE, message="Faltan el número de cédula para eliminar el registro",
                                     title="Error")
            else:
                for estu in estudiantes.items():
                    if estu[1] == CedulaEst.get():
                        subcadena = estu[0][6:7]
                        estudiantes.pop("Cedula" + subcadena)
                        estudiantes.pop("Nombre" + subcadena)
                        estudiantes.pop("FechaN" + subcadena)
                        estudiantes.pop("Celular" + subcadena)
                        booEncontro = True
                        GuardarArchivoTxt()
                        LimpiarCampos()
                        break

                if booEncontro:
                    messagebox.showinfo(parent=newWindowE, message="Registro eliminado con éxito",
                                        title="Información")
                else:
                    messagebox.showwarning(parent=newWindowE, message="Estudiante no está registrado", title="Alerta")

    #  Función para actualizar datos del estudiante
    def ActualizarDatosEstudiante():
        from tkinter import messagebox
        booEncontro = False
        resp = messagebox.askyesno(parent=newWindowE, message="¿Desea actualizar el registro?", title="Actualizar")
        if resp:
            if CedulaEst.get() == "" or Nombre.get() == "" or FechaN.get() == "" or Celular.get() == "":
                messagebox.showerror(parent=newWindowE, message="Faltan datos para actualizar el registro",
                                     title="Error")
            else:
                for estu in estudiantes.items():
                    if estu[1] == CedulaEst.get():
                        subcadena = estu[0][6:7]
                        estudiantes.update({"Cedula" + subcadena: CedulaEst.get()})
                        estudiantes.update({"Nombre" + subcadena: Nombre.get()})
                        estudiantes.update({"FechaN" + subcadena: FechaN.get()})
                        estudiantes.update({"Celular" + subcadena: Celular.get()})
                        GuardarArchivoTxt()
                        LimpiarCampos()
                        booEncontro = True
                        break

                if booEncontro:
                    messagebox.showinfo(parent=newWindowE, message="Registro actualizado con éxito",
                                        title="Información")
                else:
                    messagebox.showwarning(parent=newWindowE, message="Estudiante no está registrado", title="Alerta")

    #######
    # Función mostrar Datos del Estudiante
    def MostrarDatosEstudiante():
        from tkinter import messagebox, Text
        booEncontro = False
        resp = messagebox.askyesno(parent=newWindowE, message="Desea Mostrar el registro", title="Mostrar")
        if resp:
            newWindowD = tk.Toplevel()
            newWindowD.title("Lista de Estudiantes")
            #  Obtenemos el largo y  ancho de la pantalla
            wtotalmant = newWindowD.winfo_screenwidth()
            htotalmant = newWindowD.winfo_screenheight()
            #  Guardamos el largo y alto de la ventana
            wventanamant = 400
            hventanamant = 400
            #  Aplicamos la siguiente formula para calcular donde debería posicionarse
            pwidthmant = round(wtotalmant / 2 - wventanamant / 2)
            pheightmant = round(htotalmant / 2 - hventanamant / 2)
            newWindowD.geometry(str(wventanamant) + "x" + str(hventanamant) + "+" + str(pwidthmant) + "+" + str(
                pheightmant))
            # dimensiones de la ventana
            newWindowD.transient(app)
            iconoM = tk.PhotoImage(file="tesis.png")
            newWindowD.iconphoto(True, iconoM)
            # Create a Text widget to display the student records
            text_widget = Text(newWindowD)
            text_widget.pack(fill="both", expand=True)
            # Load the student data from a text file
            with open("estudiantes.txt", "r") as file:
                content = file.read()
            # Insert the file content into the Text widget
            text_widget.insert("end", content)
        # inicializa la ventana
            newWindowD.mainloop()
    #########
    # Uso Toplevel para crear una nueva ventana
    newWindowE = tk.Toplevel()
    newWindowE.title("Catálogo de Estudiantes")
    #  Obtenemos el largo y  ancho de la pantalla
    wtotalmant = newWindowE.winfo_screenwidth()
    htotalmant = newWindowE.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventanamant = 400
    hventanamant = 400
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidthmant = round(wtotalmant / 2 - wventanamant / 2)
    pheightmant = round(htotalmant / 2 - hventanamant / 2)
    newWindowE.geometry(str(wventanamant) + "x" + str(hventanamant) + "+" + str(pwidthmant) + "+" + str(
        pheightmant))  # dimensiones de la ventana
    newWindowE.transient(app)
    iconoM = tk.PhotoImage(file="tesis.png")
    newWindowE.iconphoto(True, iconoM)
    # para etiqueta cédula.
    tk.Label(
        newWindowE,
        text="Cédula",
        fg="white",  #  # se le asigna color texto
        bg="blue",  #  # se le asigna color fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    #  Comando para llamar a la función cuando se presiona la tecla Enter
    #  si el estudiante existe se llenan los campos restantes
    vcmd = (newWindowE.bind('<Return>', LlenarCajasTexto))
    # Se digita el # de cédula
    tk.Entry(
        newWindowE,
        bg="yellow",  # asigna color al fondo
        fg="blue",  #  # se le asigna color texto
        relief="sunken", validatecommand=vcmd,
        justify="center",
        textvariable=CedulaEst
    ).pack()
    # para etiqueta nombre del estudiante.
    tk.Label(
        newWindowE,
        text="Nombre",
        fg="white",  #  # se le asigna color texto
        bg="blue",  #  # se le asigna color fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se digita el nombre del estudiante
    tk.Entry(
        newWindowE,
        bg="yellow",  # asigna color al fondo
        fg="blue",  # # se le asigna color texto
        relief="sunken",
        justify="center",
        textvariable=Nombre
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,  # fill llena el both
        expand=False,
    )
    # para etiqueta fecha de nacimiento del estudiante.
    tk.Label(
        newWindowE,
        text="Fecha de nacimiento",
        fg="white",  #  # se le asigna color texto
        bg="blue",  # # se le asigna color fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se digita la fecha de nacimiento del estudiante
    tk.Entry(
        newWindowE,
        bg="yellow",  # asigna color al fondo
        fg="blue",  # asigna color al texto
        relief="sunken",
        justify="center",
        textvariable=FechaN
    ).pack()
    # para etiqueta número de celular del estudiante.
    tk.Label(
        newWindowE,
        text="# Celular",
        fg="white",  #  # se le asigna color texto
        bg="blue",  # color al fondo
        font=("Verdana", 14),
        anchor="center",
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se digita el número de celular del estudiante
    tk.Entry(
        newWindowE,
        bg="yellow",  # asigna color al fondo
        fg="blue",  # asigna color al texto
        relief="sunken",
        justify="center",
        textvariable=Celular
    ).pack()
    # Llama a la función de guardado de datos del estudiante.
    tk.Button(
        newWindowE,
        text="Guardar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  # cambia color del fondo
        fg="white",  # color texto
        command=GuardarDatosEstudiante,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    # Llama a la función de eliminar datos del estudiante.
    tk.Button(
        newWindowE,
        text="Eliminar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  # cambia color de fondo
        fg="white",  # color texto
        command=EliminarDatosEstudiante,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    # Llama a la función de actualización de datos del estudiante.
    tk.Button(
        newWindowE,
        text="Actualizar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  # cambia color de fondo
        fg="white",  # color texto
        command=ActualizarDatosEstudiante,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    # Llama a la función para salir de la ventana de estudiantes.
    tk.Button(
        newWindowE,
        text="Salir",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  # cambia color de fondo
        fg="white",  # color texto
        command=SalirVentanaEstudiantes,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    ################
    # Llama a la función de Mostrar de datos del estudiante.
    tk.Button(
        newWindowE,
        text="Mostrar",
        font=("Arial", 16),  # cambia la letra y el tamaño
        bg="lightblue",  #color de fondo
        fg="white",  # color texto
        command=MostrarDatosEstudiante,
        relief="flat",
        # el pack especifica las posiciones de los elementos
    ).pack(
        fill=tk.BOTH,
        expand=False,
    )
    ####################
#  Mostrar pantalla del menú de mantenimientos
def MostrarMenuMantenimientos():
    # Captura la opción seleccionada en el menú de mantenimientos
    def OptionMenuMant_Select(event):
        if obmenum.get() == "Profesores":
            MantenimientoProfesores()
        elif obmenum.get() == "Estudiantes":
            MantenimientoEstudiantes()
        else:
            newWindow.destroy()
    # Uso Toplevel para crear una nueva ventana
    newWindow = tk.Toplevel()
    newWindow.title("Mantenimiento de catálogos")
    #  Obtenemos el largo y  ancho de la pantalla
    wtotalmant = newWindow.winfo_screenwidth()
    htotalmant = newWindow.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventanamant = 600
    hventanamant = 400
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidthmant = round(wtotalmant / 2 - wventanamant / 2)
    pheightmant = round(htotalmant / 2 - hventanamant / 2)
    newWindow.geometry(str(wventanamant) + "x" + str(hventanamant) + "+" + str(pwidthmant) + "+" + str(
        pheightmant))  # dimensiones de la ventana
    newWindow.configure(background="light blue")
    newWindow.transient(app)
    iconoM = tk.PhotoImage(file="tesis.png")
    newWindow.iconphoto(True, iconoM)

    tk.Label(  # el label etiqueta dónde podemos mostrar algún texto estático.
        newWindow,
        text="Menú Mantenimientos",
        fg="white",  #  # se le asigna color texto
        bg="blue",  #  # color al fondo
        font=("Verdana", 14),
    ).pack(  # especifica las posiciones de los elementos
        fill=tk.BOTH,
        expand=False,
    )
    # Se crean las opciones para el menú mantenimientos
    MenuObMant = [
        "Profesores",  # se almacena como lista
        "Estudiantes", "Salir"
    ]
    obmenum = tk.StringVar(newWindow)  # variables para el menu
    obmenum.set(MenuObMant[0])  # obMenu devuelve lo que esta en MenuOb
    opcionM = tk.OptionMenu(newWindow, obmenum, *MenuObMant, command=OptionMenuMant_Select)
    opcionM.config(bg="blue", foreground="white",
                   font=('Arial', 12))  # configuración que se visualizara en la ventana, con color, letra
    opcionM.pack(pady=50)  # especifica las posiciones de los elementos

#  Mostrar pantalla del menú de matrícula de estudiantes
def MostrarMenuMatricula():
    Year = tk.IntVar(app)
    canMesesPagados = 0
    canMesesPorPagar = 0
    mesesPagar = []
    def CargaMesesPagados():
        # Uso de matriz para cargar meses pagados de un estudiante desde archivo txt, con excepciones
        tempMesesPagados = [[], [], []]
        # Lo asigna para mostrarlo en tkinter
        try:
            f = open("meses_pagados.txt", "r", encoding="utf-8")  # busca o abre fichero
        except FileNotFoundError:  # ocurre cuando se intenta acceder  aun fichero que no existe en la ruta indicada
            print("¡El fichero no existe!")  # muestra mensaje
        else:
            contfilas = 0
            for linea in f:
                contfilas = contfilas + 1
                cont = 0
                tupla = linea.split()
                if int(tupla[1]) == Year.get():
                    for tu in tupla:
                        tempMesesPagados[cont].append(tu)
                        cont = cont + 1# contador de los meses
            # Cierra el fichero
            f.close()
            return tempMesesPagados# retorna los meses pagados

    # se convierte número de mes a texto de la siguiente forma
    def ConvertirMes(mes):
        if mes == "1":
            return "Enero"
        elif mes == "2":
            return "Febrero"
        elif mes == "3":
            return "Marzo"
        elif mes == "4":
            return "Abril"
        elif mes == "5":
            return "Mayo"
        elif mes == "6":
            return "Junio"
        elif mes == "7":
            return "Julio"
        elif mes == "8":
            return "Agosto"
        elif mes == "9":
            return "Setiembre"
        elif mes == "10":
            return "Octubre"
        elif mes == "11":
            return "Noviembre"

    #  Cargar cajas de texto
    def BuscarEstudiante(e):
        from tkinter import messagebox
        mesesPagados = [[], [], []]
        booEncontro = False
        for estu in estudiantes.items():
            if estu[1] == CedulaMatri.get():
                subcadena = estu[0][6:7]
                Nombre.set(estudiantes["Nombre" + subcadena])
                mesesPagados = CargaMesesPagados()
                canMesesPagados = mesesPagados[0].__len__()
                canMesesPorPagar = 11 - int(canMesesPagados)
                canmxpagar.set(int(canMesesPorPagar))
                # para etiqueta meses pagados.
                tk.Label(
                    nuevaVentana,
                    text="Meses pagados",
                    fg="white",  # Foreground
                    bg="blue",  # Background
                    font=("Verdana", 12), width=15,
                    anchor="center",
                ).place(
                    x=5, y=290,
                )
                #  Lista de meses pagados
                listboxpagados = tk.Listbox(nuevaVentana, selectmode=tk.EXTENDED, width=25)
                cMeses = 0
                for k in range(1, canMesesPagados + 1):
                    listboxpagados.insert(cMeses, ConvertirMes(mesesPagados[2][cMeses]))
                    cMeses = cMeses + 1
                listboxpagados.place(
                    x=5, y=325,
                )

                # para etiqueta meses por pagar.
                tk.Label(
                    nuevaVentana,
                    text="Meses por pagar",
                    fg="white",  #  # se le asigna color texto
                    bg="blue",  # color de fondo
                    font=("Verdana", 12), width=15,
                    anchor="center",
                ).place(
                    x=340, y=290
                )
                #  Lista de meses sin pagar
                listboxporpagar = tk.Listbox(nuevaVentana, selectmode=tk.EXTENDED, width=25)
                cmesesxpagar = 0
                for k in range(canMesesPagados + 1, 12):
                    listboxporpagar.insert(cmesesxpagar, ConvertirMes(str(k)))
                    cmesesxpagar = cmesesxpagar + 1
                listboxporpagar.place(
                    x=340, y=325,
                )
                booEncontro = True
                break
        if booEncontro == False:
            Nombre.set("")
            messagebox.showwarning(parent=nuevaVentana,
                                   message="Estudiante debe ser registrado",
                                   title="Alerta")

    ################Función calcula matricula###################################################
    def ValorAPagar():  # Función que se activa al presionar el botón Calcular Valor Matricula

        global contadorEstudiantes # variable global
        from tkinter import messagebox #para mostrar mensaje
        if cuotasIngresadas.get() != "":
            if int(cuotasIngresadas.get()) <= canmxpagar.get():
                mesesPagados = int(cuotasIngresadas.get())  # Aqui se lee el número desde la entrada de texto
                cuotasIngresadas.delete(0, 2)  # Se borra la entrada de texto

                valorMensualidad = int(35000)  # Se define el valor de la mensualidad en 12

                msg = ""  # Variable str para guardar el mensaje para imprimir el valor a pagar

                """
                Se calcula el valor sin descuento, con descuento del 5% o del 10% según la cantidad de mesesPagados ingresadas
                """
                if mesesPagados >= 1 and mesesPagados <= 3: # calcula valor total de meses pagados si es mayor o igual a 1 o menor o igual a 3
                    valorTotal = valorMensualidad * mesesPagados #multiplica valor de mensualidad x meses pagados
                    msg = "Valor total a pagar: " + str(valorTotal)
                    montosdescuento.set(valorTotal)
                elif mesesPagados >= 4 and mesesPagados <= 8: #de igual forma  por si paga 4 meses o menos de 8 meses
                    valorSinDescuento = valorMensualidad * mesesPagados #se multiplica
                    valorDescuento = valorSinDescuento * (5 / 100) # se multiplica y divide 5 entre 100
                    valorTotal = valorSinDescuento - valorDescuento #se le resta a valor sin descuento a valor descuento
                    msg = "Valor total a pagar: " + str(valorTotal)
                    montosdescuento.set(valorSinDescuento)
                    descuento.set(valorDescuento)
                elif mesesPagados >= 9 and mesesPagados <= 12: #de igual forma si paga mayor de 9 meses y menos de 12
                    valorSinDescuento = valorMensualidad * mesesPagados #se multiplica
                    valorDescuento = valorSinDescuento * (10 / 100)# se multiplica y divide 10 entre 100

                    valorTotal = valorSinDescuento - valorDescuento #se realiza resta a valor sin descuento a valor descuento
                    msg = "Valor total a pagar: " + str(valorTotal) # muestra el valor totala  apagar

                    montosdescuento.set(valorSinDescuento)
                    descuento.set(valorDescuento)

                else: #sino da un error
                    messagebox.showerror(parent=nuevaVentana,
                                         message="Error de ingreso, solo se permiten valores de 1 a 12",
                                         title="Error de ingreso de datos")

                laValorPagar.config(text=msg)  # Se escribe el mensaje del valor a pagar en la etiqueta
                """
                En este bloque se controla algún error que resulte en el ingreso
                """
                try:
                    vectorEstudianteYCostoMatricula = [contadorEstudiantes, mesesPagados,
                                                       valorTotal]  # Se genera un vector con las caracteristicas de la matricula
                    matrizEstudiantes.append(vectorEstudianteYCostoMatricula)  # Se añade una nueva fila en la matriz

                    contadorEstudiantes = contadorEstudiantes + 1  # Se aumenta el contador de estudiantes para matricular otro
                    print(
                        matrizEstudiantes)  # Se imprime la matriz de estudiantes en la consola para verificar que los registros se han ingresado bien
                except Exception as error:
                    print(
                        'Error en la ejecucion por ingreso incorrecto')  # Se imprime un mensaje si ha ocurrido algún error
            else:
                messagebox.showerror(parent=nuevaVentana,
                                     message="La cantidad de cuotas a pagar no puede ser mayor a la cantidad de meses por pagar",
                                     title="Error de ingreso de datos")
        else:
            messagebox.showerror(parent=nuevaVentana, message="El campo cuotas ingresada no puede estar vacío",
                                 title="Error de ingreso de datos")

    nuevaVentana = tk.Toplevel(app, background="#223344")  # Se crea la ventana donde se realizará la matrícula
    nuevaVentana.withdraw()  # Se oculta la ventana para que no aparezca al tiempo con la ventana principal

    nuevaVentana.title("Matrícula estudiante")  # Titulo de la ventana de matricula

    #  Establecer las dimensiones de la ventana
    wtotalmatri = nuevaVentana.winfo_screenwidth()
    htotalmatri = nuevaVentana.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventanamatri = 500
    hventanamatri = 550
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidthmatri = round(wtotalmatri / 2 - wventanamatri / 2)
    pheightmatri = round(htotalmatri / 2 - hventanamatri / 2)
    nuevaVentana.geometry(str(wventanamatri) + "x" + str(hventanamatri) + "+" + str(pwidthmatri) + "+" + str(
        pheightmatri))  # dimensiones de la ventana
    nuevaVentana.configure(background="light blue")
    nuevaVentana.transient(app)
    iconoM = tk.PhotoImage(file="tesis.png")
    nuevaVentana.iconphoto(True, iconoM)

    descuento.set(0)
    montosdescuento.set(0)

    #  Creación de mensaje y se añade a la ventana de matricula

    l1 = tk.Label(nuevaVentana, text="Ingrese la cantidad de mensualidades que desea cancelar", fg="white",
                  # Foreground
                  bg="blue",  # color de fondo
                  font=("Verdana", 7),
                  anchor="center", )
    l1.place(
        x=50, y=150,
    )
    # Creación de mensaje y se añade a la ventana de matricula
    l2 = tk.Label(nuevaVentana,
                  text="Recuerde que la mensualidad es de 11 meses y hay descuentos si paga por adelantado", fg="white",
                  # Foreground
                  bg="blue",  # color de fondo
                  font=("Verdana", 7),
                  anchor="center", )
    l2.place(
        x=25, y=175,
    )
    #  Este elemento permite ingresar la cantidad de mensualidades a pagar en la ventana de matricula
    cuotasIngresadas = tk.Entry(nuevaVentana, bg="yellow",  # asigna color ade fondo
                                fg="blue",  # asigna color a texto
                                relief="sunken", width=10,
                                justify="center", )
    cuotasIngresadas.place(
        x=350, y=150,
    )
    #  Este elemento permite calcular el valor a pagar en la ventana de matricula
    tk.Button(nuevaVentana, text="Calcular Valor Mensualidad", font=("Arial", 16),  # cambia la letra y el tamaño
              bg="lightblue",  # cambia color fondo
              fg="white",  # color texto,
              command=ValorAPagar,
              relief="flat", ).place(
        x=120, y=195
    )
    #  Este elemento permite mostrar el valor total a pagar en la matricula
    laValorPagar = tk.Label(nuevaVentana, text="Valor total a pagar: 0", fg="white",  # color texto
                            bg="blue",  #color fondo
                            font=("Verdana", 12),
                            anchor="center", )
    laValorPagar.place(
        x=130, y=250
    )
    #  Este botón permite salir de la ventana de matricula y volver a la ventana principal
    tk.Button(nuevaVentana, text="Salir", font=("Arial", 16),  # cambia la letra y el tamaño
              bg="lightblue",  # cambia color de fondo
              fg="white",  # color texto,
              command=nuevaVentana.withdraw,
              relief="flat").place(
        x=230, y=500
    )
    #  Este elemento permite mostrar todos los registros de estudiantes matriculados
    laTotalMatriculas = tk.Label(nuevaVentana, text="Registro Matriculas", fg="white",  # color texto
                                 bg="blue",  # color fondo
                                 font=("Verdana", 12),
                                 anchor="center", )
    laTotalMatriculas.place(
        x=175, y=25
    )
    tk.Button(nuevaVentana, text="Procesar", font=("Arial", 16),  #se crea bóton procesar cambia la letra y el tamaño
              bg="lightblue",  # cambia color fondo
              fg="white",  # color texto,
              command=nuevaVentana.withdraw,
              relief="flat").place(
        x=230, y=400

    )

    #laValorPagar=tk.Button

    ########################################
    """
    Se inicia el programa en la ventana principal
    """
    laValorPagar.config(text="Valor total a pagar: 0")  # Se restaura el mensaje de la etiqueta del valor a pagar
    nuevaVentana.deiconify()  # Se muestra la ventana donde se realizará la matricula
    # valores sin descuento
    tk.Label(
        nuevaVentana,
        text="Total sin descuento",
        fg="white",  # color texto
        bg="blue",  # color fondo
        font=("Verdana", 12),
        anchor="center",
    ).place(
        x=165, y=280,
    )
    tk.Entry(
        nuevaVentana,
        bg="yellow",  # asigna color al fondo
        fg="blue",  # asigna color texto
        relief="sunken", width=10,
        justify="center", state="readonly",
        textvariable=montosdescuento
    ).place(
        x=225, y=310,
    )
    # valores con descuento
    tk.Label(
        nuevaVentana,
        text="Descuento",
        fg="white",  # color texto
        bg="blue",  # color fondo
        font=("Verdana", 12),
        anchor="center",
    ).place(
        x=210, y=335,
    )
    tk.Entry(
        nuevaVentana,
        bg="yellow",  # asigna color de fondo
        fg="blue",  # asigna color a texto
        relief="sunken", width=10,
        justify="center", state="readonly",
        textvariable=descuento
    ).place(
        x=225, y=365,
    )
    # para etiqueta año actual.
    tk.Label(
        nuevaVentana, #se llama a la ventana donde esta
        text="Año Actual", #texto que lleva
        fg="white",  # se le asigna color texto
        bg="blue",  # se le asigna color al fondo
        font=("Verdana", 12), #tamaño y estilo de letra
        anchor="center", # donde ira la posicion de la letra
    ).place(
        x=175, y=60,
    )
    # para mostrar el dato del año actual
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    Year.set(date.strftime("%Y"))
    tk.Entry(
        nuevaVentana,
        bg="yellow",  # asigna color a fondo
        fg="blue",  # asigna color a texto
        relief="sunken", width=10,
        justify="center", state="readonly",
        textvariable=Year
    ).place(
        x=275, y=60,
    )
    # para etiqueta número de cedula del estudiante.
    tk.Label(
        nuevaVentana,
        text="Cedula",
        fg="white",  # color texto
        bg="blue",  # color fondo
        font=("Verdana", 12),
        anchor="center",
    ).place(
        x=10, y=100,
    )
    #  Comando para llamar a la función cuando se presiona la tecla Enter
    #  si el profesor existe se llenan los campos restantes
    vcmd = (nuevaVentana.bind('<Return>', BuscarEstudiante))
    # Espacio para digitar el número de cédula del estudiante
    tk.Entry(
        nuevaVentana,
        bg="yellow",  # asigna color al fondo
        fg="blue",  # asigna color al  texto
        relief="sunken", width=20, validatecommand=vcmd,
        justify="center",
        textvariable=CedulaMatri
    ).place(
        x=80, y=100,
    )
    # Espacio para presentar el nombre del estudiante
    tk.Entry(
        nuevaVentana,
        bg="yellow",  # asigna color al fondo
        fg="blue",  # asigna color al fondo
        relief="sunken", width=50,
        justify="center", state="readonly",
        textvariable=Nombre

    ).place(
        x=190, y=100,
    )

tk.Label(  # el label etiqueta dónde podemos mostrar algún texto estático, ene ste caso se llama la instancia del sigleton del nombre.
    app,
    text="Bienvenidos estimados usuarios al Sistema de Matrícula del " + centro_educativo.nombre,
    fg="white",  ## se le asigna color al texto
    bg="blue",  # # se le asigna color al fondo
    font=("Verdana", 14),
).pack(  # especifica las posiciones de los elementos
    fill=tk.BOTH,
    expand=False,
)
#  Carga el diccionario global de profesores con los datos desde el archivo txt
profes = CargaDatosProfesores()
estudiantes = CargaDatosEstudiantes()
# ###Creación de los Botones
# Mensaje de Bienvenida
# se creo el menu para que el cliente presione la opción que desee
MenuOb = [
    "Menú Principal", "Mantenimientos",  # se almacena como lista contiene menu principal, mantenimientos, matricula y salir
    "Matrícula de estudiantes", "Salir"
]
obMenu = tk.StringVar(app)  # variables para el menu
obMenu.set(MenuOb[0])  # obMenu devuelve lo que esta en MenuOb
opcion = tk.OptionMenu(app, obMenu, *MenuOb, command=OptionMenu_Select)
opcion.config(bg="blue", foreground="white",
              font=('Arial', 12))  # configuración que se visualizara en la ventana, con color, letra
opcion.pack(pady=50)  # especifica las posiciones de los elementos
app.mainloop() #Se inicia el programa en la ventana principal
