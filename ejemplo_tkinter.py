from tkinter import *
'''
=====================
   PARTE FUNCIONAL
=====================
'''
'''
=====================
   INTERFAZ GRÁFICA
=====================
'''
# ---Espaciados ---
esp_x = 10
esp_y = 10
# ---Colores para el framecampos---
framecampos_color_fondo = 'pink'
frame_campos_color_letra = 'black'
#---Colores para framebotones---
framebotones_color_fondo = 'plum'
framebotones_color_boton = 'black'
framebotones_color_texto_boton = 'SeaGreen2'




# RAÍZ 
raiz = Tk()
raiz.title('Python CRUD - Comision 22607')

#BARRA DE MENU
barramenu = Menu(raiz)
raiz.config(menu=barramenu)

bbddmenu= Menu(barramenu, tearoff=0)
bbddmenu.add_command(label = ' Conectar con BBDD')
bbddmenu.add_command(label = ' Salir del programa')

borramenu = Menu(barramenu, tearoff=0)
borramenu.add_command(label = ' Limpiar formulario')
barramenu.add_cascade(label = 'Limpiar', menu=borramenu)

ayudamenu = Menu(barramenu, tearoff=0)
ayudamenu.add_command(label = 'Licencia')
ayudamenu.add_command(label = 'Acerca de ....' )

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Limpiar', menu=borramenu)
barramenu.add_cascade(label='Acerca de ...', menu=ayudamenu)

#----FRAME PARA CAMPOS----
framecampos = Frame(raiz)
framecampos.config(bg=framecampos_color_fondo)
framecampos.pack(fil='both')

# Labels (se lo llama asi al texto)
'''
"STICKY"
     n
  nw   ne
w         e
  sw   se
     s
'''
#Apunte: posicionamiento de elemento en tkinter:https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/
def configurar_label(mi_label, fila):
   espaciado_labels = {'column':0, 'sticky': 'e', 'padx':esp_x, 'pady':esp_y}
   colores_label = {'bg':framecampos_color_fondo, 'fg':
   frame_campos_color_letra} #bg:backgroudn, fg:foregrond
   mi_label.grid(row=fila, **espaciado_labels)
   mi_label.config(**colores_label)


legajolabel= Label(framecampos, text='Legajo:')
#legajolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)
configurar_label(legajolabel,0 )


calificacionlabel= Label(framecampos, text='Calificacion:')
#legajolabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)
configurar_label(calificacionlabel,1 )

escuelalabel= Label(framecampos, text='Escuela:')
#escuelalabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)
configurar_label(escuelalabel,2 )

localidadlabel= Label(framecampos, text='Localidad:')
#legajolabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)
configurar_label(localidadlabel,3 )

provincialabel= Label(framecampos, text='Provincia:')
#Provincialabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)
configurar_label(provincialabel, 4)


#---CAMPOS DE ENTRADA ---
'''
entero = IntVar()  # Declara variable de tipo entera
flotante = DoubleVar()  # Declara variable de tipo flotante
cadena = StringVar()  # Declara variable de tipo cadena
booleano = BooleanVar()  # Declara variable de tipo booleana
'''
legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx = 10, pady=10)

alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=0, column=1, padx = 10, pady=10)

escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=0, column=1, padx = 10, pady=10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=0, column=1, padx = 10, pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=0, column=1, padx = 10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=0, column=1, padx = 10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=0, column=1, padx = 10, pady=10)

#---FRAME PARA LA BOTONERA CRUD---- ->Create, read, update, delete
framebotones = Frame(raiz)
framebotones.pack()

boton_crear= Button(framebotones, text='Crear')
boton_crear.grid(row = 0, column=0, padx=10, pady=10)

boton_leer= Button(framebotones, text='Leer')
boton_leer.grid(row = 0, column=0, padx=10, pady=10)

boton_actualizar= Button(framebotones, text='Actualizar')
boton_actualizar.grid(row = 0, column=0, padx=10, pady=10)

boton_borrar= Button(framebotones, text='Borrar')
boton_borrar.grid(row = 0, column=0, padx=10, pady=10)

#---FRAME DEL PIE
framecopy = Frame(raiz)
framecopy.pack()

copylabel= Label(framecopy, text='(2022) por Carla Allende')
copylabel.grid(column=0, padx=10, pady=10)

#Debe ser la ultima linea
raiz.mainloop()