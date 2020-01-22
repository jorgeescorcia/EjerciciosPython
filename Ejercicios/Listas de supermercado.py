# Ejercicio
"""
Lista de Supermercados 
En este proyecto estarán creando un programa que se encargará de administrar una lista de supermercados. 

Para lograrlo, seguirán las siguientes instrucciones: 
• Crearán una variable que almacene nuestra lista de supermercados: supermercado.
• Crearán un menú que contendrá las siguientes opciones: 

MENU PRINCIPAL 
1 | Imprimir lista
2 | Agregar articulo a la lista
3 | Eliminar articulo especifico
4 | Imprimir una parte de lista
5 | Salir 

• Crearán una variable que almacenará la opción a elegir del menú: opción.
• El flujo de ejecución de la aplicación debe estar en un ciclo while.
• Para controlar la condición del ciclo, utilizarán una variable bandera: menu.
• En la opción 1, deberán imprimir los artículos de la lista junto a su respectivo índice.
• En la opción 2, se solicitará el nombre del artículo a ingresar y se incluirá en la lista.
• En la opción 3, se especificará el índice del artículo a borrar y se eliminará el mismo de la lista.
• En la opción 4, se especificará el índice del último artículo a imprimir y se mostrarán en pantalla.
• En la opción 5, se mostrará un mensaje de despedida y se terminará la aplicación.
• En caso tal no se cumpla ninguna de las opciones anteriores, debe mostrar un mensaje de error. 
 
Tendrán que utilizar la mayor parte de los conceptos aprendidos a lo largo de este capítulo: ciclos y decisiones. Además, aplicar los
conceptos aprendidos en capítulos anteriores.
"""

menu = True #Variable que controla el Ciclo de menu
supermercados = [] #Variable que representa la lista de Supermercados (Vacia en este caso)

while menu==True:  # Evalua si mantendremos la ejecucion del programa o no.

#Imprimimos el menu de la Aplicacion
     print("                                                 ")
     print("Menu    Principal")
     print("                                                 ")
     print(" 1 | Imprimir Lista")
     print(" 2 | Agregar Articulo A La lista")
     print(" 3 | Eliminar Articulo Especifico")
     print(" 4 | Imprimir Una Parte De La Lista")
     print(" 5 | Salir")
     print("                                                 ")
     
#Finaliza la impresion del menu
     
     opcion = int(input("Elegir una opcion deseada: ")) # Variable que almacena la opcion elegida en el menu

     if opcion == 1:   #Evaluamos la opcion elegida
          print("Tu lista de supermercados contiene: ")
          i =0
          for articulo in supermercados:
               print(str(i) + "\t" + articulo) #Asignamos un indice a cada articulo ingresado.
               i = i + 1
               
          
     elif opcion==2:
      nuevoarticulo =input("Nombre del articulo a ingresar: ") #Mediante una variable le pedimos al usuario que digite el nuevo articulo a agregar
      supermercados.append(nuevoarticulo) #Le pasamos ese articulo agregado por el usuario a la varibale supermercados creada a inicio de la App
      
   
      
     elif opcion==3:
          borrararticulo= int(input(" Articulo A Eliminar (Ingrese numero): "))# Mediante una variable le decimos al usuario que digite el indice del articulo que quiere elminar de la lista
          supermercados.pop(borrararticulo) # Le pasamos en indice ingresado por el usuario a la variable supermercados para que elimine el elemento
          print(supermercados)# Imprimimos por pantalla la nueva lista con el elemento eliminado

     elif opcion== 4:
          imprimirarticulo=int(input("Indice del ultimo articulo a imprimir(Ingrese numero): "))#variable para imprimir un articulo en particular de la lista(En este caso el ultimo de la lista)
          print(supermercados[imprimirarticulo])#Imprimimos el ultimo articulo
          
     elif opcion==5:
          print("¡Hasta Luego!")
          break #Aqui rompemos el Ciclo While para salir del programa

     else:
          print("Opcion no valida. ")


 


