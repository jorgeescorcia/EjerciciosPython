#Realizar un programa en python que pida 2 numero por teclado y diga,
#si es mayor o menor o igual.


print ("---------------------------------------")
print ("|Calcular Mayor, Menor , igual|")
print ("---------------------------------------")


print     ("1. Mayor")
print     ("2. Menor")
print     ("3. Igual")
print     ("        ")


opcion = input("Ingrese una opcion: ")#Ingresamos por teclado la opcion

print     ("        ")

n1 = int(input ("Ingrese el primer numero: "))#Ingresamos por teclado los numeros a calcular
n2 = int(input ("Ingrese el segundo numero: "))
print     ("        ")



if opcion == "1":
     mayor = max(n1,n2)#Utilizamos "max" Para saber el mayor de 2 numeros
     print("--------------------------------------")
     print("El numero mayor es: ", mayor)
     print("--------------------------------------")
     
     
if opcion == "2":
     menor = min(n1,n2)#Utilizamos "min" Para saber el menor de 2 numeros
     print("--------------------------------------")
     print ("El numero menor es: ", menor)
     print("--------------------------------------")
     
if opcion == "3":
     if n1 == n2:
         print("--------------------------------------")
         print ("Los numero son iguales")
         print("--------------------------------------")
     else:
          print("--------------------------------------")
          print ("Los numero no son iguales")
          print("--------------------------------------")


input()


  


