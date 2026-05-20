#Creado por: Alejandro Sibaja Badilla y Marco Herrera Gómez
#Fecha de creación: 16/05/2026
#Ultima actualización: xx/05/2026
#Versión de python: 3.14
#Definición de funciones
def mostrarMenu():
    print("\n===== DONEMOS SANGRE =====")
    print("1. Insertar donante")
    print("2. Eliminar donante")
    print("3. Insertar lugar de donación")
    print("4. Reportes")
    print("5. Salir")

def main():
    tiposDeSangre=("A+","A-","B+","B-","AB+","AB-","O+","O-")
    lugaresDeDonacion={"San José":[], "Alajuela":[], "Cartago":[], "Heredia":[], "Guanacaste":[],
    "Puntarenas":[], "Limón":[]}
    donadores=[]
    while True:
        mostrarMenu()
        opcion=input("Seleccione la opción que desee ejecutar: ")
        if opcion=="1":
            print("Insertar donante pendiente.")
        elif opcion=="2":
            print("Modificar donante pendiente.")
        elif opcion=="3":
            print("Eliminar donante pendiente.")
        elif opcion=="4":
            print("Consultar donante pendiente.")
        elif opcion=="5":
            print("Insertar lugar de donación pendiente.")
        elif opcion=="6":
            print("Modificar lugar de donación pendiente.")
        elif opcion=="7":
            print("Eliminar lugar de donación pendiente.")
        elif opcion=="8":
            print("Reportes pendientes.")
        elif opcion=="9":
            print("Donar sangre, es donar vida")
            break
        else:
            print("Opción inválida.")

#Inicio del programa principal
main()