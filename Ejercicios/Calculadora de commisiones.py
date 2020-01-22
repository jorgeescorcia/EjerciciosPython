#Calculadora De Comisiones

vendedor = input("Nombre del Vendendor: ")
mes1 = int(input("Ventas del mes 1: "))
mes2 = int(input("Ventas de mes 2: "))
mes3 = int(input("Ventas del mes 3: "))

suma_de_ventas =(mes1 + mes2 + mes3)

comision =(suma_de_ventas * 12.5) / 100

 #Impresion de reporte


print("\nINFORME DE COMISIONES\n\nVendedor\t\tVentas\t\tComision")
print("-----------\t\t-------------\t--------------")
print(vendedor+"\t\t"+"$"+str(suma_de_ventas)+"\t\t"+"$"+str(comision))
 
"""print("----------------------")
print("Vendedor: " , vendedor)
print("Ventas Totales:", suma_de_ventas)
print("La comision es: ", comision)
"""
print ()


input("")
