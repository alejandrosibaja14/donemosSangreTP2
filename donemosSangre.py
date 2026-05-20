#Creado por: Alejandro Sibaja Badilla y Marco Herrera Gómez
#Fecha de creación: 16/05/2026
#Ultima actualización: xx/05/2026
#Versión de python: 3.14
#Definición de funciones
def cargarBaseDatos(rutaArchivo):
    matrizBaseDatos= []
    archivo= open(rutaArchivo, "r")
    lineas= archivo.readlines()
    archivo.close()
    indiceLinea= 0
    while indiceLinea< len(lineas):
        lineaActual= lineas[indiceLinea].strip() 
        if lineaActual!= "":
            datosSeparados= lineaActual.split(",")
            nombreCompleto= [datosSeparados[0], datosSeparados[1], datosSeparados[2]]
            cedula= int(datosSeparados[3])
            tipoSangreStr= datosSeparados[4]
            tipoSangreInt= 0
            indiceTupla= 0
            while indiceTupla< len(tiposDeSangre):
                if tiposDeSangre[indiceTupla]== tipoSangreStr:
                    tipoSangreInt= indiceTupla
                indiceTupla= indiceTupla + 1
            sexo= False
            if datosSeparados[5]== "Masculino":
                sexo= True
            fechaNacimiento= datosSeparados[6]
            peso= float(datosSeparados[7])
            correo= datosSeparados[8]
            telefono= int(datosSeparados[9])
            estado= False
            if datosSeparados[10]== "Activo":
                estado= True
            justificacion= datosSeparados[11]
            registroDonador= [
                nombreCompleto,   
                cedula,           
                tipoSangreInt,    
                sexo,             
                fechaNacimiento,  
                peso,             
                correo,           
                telefono,         
                estado,           
                justificacion     
            ]
            matrizBaseDatos= matrizBaseDatos+ [registroDonador]
        indiceLinea= indiceLinea + 1
    return matrizBaseDatos
    
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