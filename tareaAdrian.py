#Subir a GitHub un programa hecho en C# o Java o Python que tenga dos arreglos de tamaño 3.
#El programa debe solicitar ingresar los datos en cada uno de los arreglos
#con números desordenados.
#Como resultado los numeros deben salir ordenados
lista1=[]
print("Cuantos numeros desea ingresar para la lista 1?")
cantidad=int(input())
i=0
while i < cantidad:
    print("ingrese el numero: ", i+1)
    numero=input()
    lista1.append(numero)
    i+=1

lista2=[]
print("Cuantos numeros desea ingresar para la lista 2?")
cantidad=int(input())
i=0
while i < cantidad:
    print("ingrese el numero: ", i+1)
    numero=input()
    lista2.append(numero)
    i+=1
print("Los numeros de la lista 1 son: ")
print(lista1)
print("Los numeros de la lista 2 son: ")
print(lista2)


lista1.extend(lista2)
lista1.sort(reverse=False)
print("El resultado de las listas en orden ascendente es :")
print(lista1)
