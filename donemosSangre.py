#Creado por: Alejandro Sibaja Badilla y Marco Herrera Gómez
#Fecha de creación: 16/05/2026
#Ultima actualización: xx/05/2026
#Versión de python: 3.14
#Definición de funciones
import re
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

def cargarLugaresDonacion():
    lugaresPorProvincia= {
        1: [
            "El Banco Nacional de sangre", 
            "Hospital México", 
            "Hospital San Juan de Dios"
        ],
        2: [
            "Hospital San Rafael de Alajuela", 
            "Hospital de San Ramón", 
            "Hospital del Cantón Norteño"
        ],
        3: [
            "Hospital Max Peralta"
        ],
        4: [
            "Hospital San Vicente de Paúl"
        ],
        5: [
            "Hospital La Anexión en Nicoya", 
            "Hospital Enrique Baltodano de Liberia"
        ],
        6: [
            "Hospital Monseñor Sanabria"
        ],
        7: [
            "Hospital Tony Facio", 
            "Hospital de Guápiles"
        ]
    }
    return lugaresPorProvincia
def mostrarMenu():
    print("\n===== DONEMOS SANGRE =====")
    print("1. Insertar donante")
    print("2. Eliminar donante")
    print("3. Insertar lugar de donación")
    print("4. Reportes")
    print("5. Salir")

def validarCedula(pcedula):
    """
    Funcionamiento: Valida que la cédula tenga el formato correcto.
    Entradas: pcedula: cédula a validar.
    Salidas: True si es válida, False si no lo es.
    """
    patron=r"^\d-\d{4}-\d{4}$"
    if re.match(patron,pcedula):
        return True
    else: return False

def validarEdad(pedad):
    """
    Funcionamiento: Verifica que la edad sea numérica y mayor o igual a 18.
    Entradas: pedad: edad ingresada.
    Salidas: True si es válida, False si no lo es.
    """
    if not pedad.isdigit():
        return False
    edad=int(pedad)
    if edad<18:
        return False
    else: return True

def validarTipoSangre(ptipoSangre,ptiposDeSangre):
    """
    Funcionamiento: Verifica que el tipo de sangre exista en la tupla .
    Entradas: ptipoSangre: tipo de sangre ingresado.
            ptiposDeSangre: tupla de tipos válidos.
    Salidas: True si es válido, False si no lo es.
    """
    if ptipoSangre in ptiposDeSangre:
        return True
    else: return False

def validarDonadorExistente(pcedula,pmatrizDonadores):
    """
    Funcionamiento: Verifica si una cédula ya se encuentra registrada.
    Entradas: pcedula: cédula a buscar.
            pmatrizDonadores: matriz de donadores.
    Salidas: True si ya existe, False si no existe.
    """
    for donador in pmatrizDonadores:
        if donador[0]==pcedula:
            return True
    else: return False

def insertarDonante(pdonadores, pcedula, pnombre, pedad, psexo, ptipoSangre, pprovincia, ptiposDeSangre, plugaresDeDonacion):
    """
    Funcionamiento: Valida y registra un nuevo donador en la matriz de donadores.
    Entradas: pdonadores: matriz de donadores.
            pcedula: cédula del donador.
            pnombre: nombre completo del donador.
            pedad: edad del donador.
            psexo: sexo del donador.
            ptipoSangre: tipo de sangre del donador.
            pprovincia: provincia del donador.
            ptiposDeSangre: tupla con tipos de sangre válidos.
    Salidas: Matriz actualizada y mensaje de retroalimentación.
    """
    if not validarCedula(pcedula):
        return pdonadores, "Cédula inválida. Vuelva a intentarlo con un número de cédula válido."
    if validarDonadorExistente(pcedula, pdonadores):
        return pdonadores, "El donador ingresado ya existe."
    if not validarEdad(pedad):
        return pdonadores, "La edad ingresada no es válida. Debe ingresar una edad mayor o igual a 18 años."
    if psexo!="M" and psexo!="F":
        return pdonadores, "Sexo inválido. Debe ingresar M en caso de masculino y F si es femenino."
    if not validarTipoSangre(ptipoSangre, ptiposDeSangre):
        return pdonadores, "Tipo de sangre inválido. Vuelva a intentarlo."
    if not validarProvincia(pprovincia, plugaresDeDonacion):
        return pdonadores, "Provincia inválida. Debe ingresar una provincia de Costa Rica."
    donador=[
        pcedula,
        " ".join(pnombre.split()).title(),
        int(pedad),
        psexo,
        ptipoSangre,
        pprovincia.title(),
        True
    ]
    pdonadores.append(donador)
    return pdonadores, "El donador fue registrado correctamente."

def validarProvincia(pprovincia, plugaresDeDonacion):
    """
    Funcionamiento: Verifica que la provincia ingresada exista dentro del diccionario de lugares de donación.
    Entradas: pprovincia: provincia ingresada.
            plugaresDeDonacion: diccionario con provincias válidas.
    Salidas: True si la provincia existe, False si no existe.
    """
    if pprovincia.title() in plugaresDeDonacion:
        return True
    else: return False

def eliminarDonante(pcedula, pdonadores):
    if not validarCedula(pcedula):
        return pdonadores, "Cédula inválida. Vuelva a intentarlo."
    for donador in pdonadores:
        if donador[0]==pcedula:
            if donador[6]==False:
                return pdonadores,"El donador ya fue eliminado anteriormente."
            donador[6]=False
            return pdonadores,"Donador eliminado correctamente."
    return pdonadores,"El donador solicitado no existe."

def main():
    tiposDeSangre=("A+","A-","B+","B-","AB+","AB-","O+","O-")
    lugaresDeDonacion={"San José":[], "Alajuela":[], "Cartago":[], "Heredia":[], "Guanacaste":[],
    "Puntarenas":[], "Limón":[]}
    donadores=[]
    while True:
        mostrarMenu()
        opcion=input("Seleccione la opción que desee ejecutar: ")
        if opcion=="1":
            print("\n===== INSERTAR DONANTE =====\n")
            cedula=input("Ingrese la cédula del donador: ")
            nombre=input("Ingrese el nombre completo del donador: ")
            edad=input("Ingrese la edad del donador: ")
            sexo=input("Ingrese el sexo del donador (M/F): ").upper()
            tipoSangre=input("Ingrese el tipo de sangre del donador: ").upper()
            provincia=input("Ingrese la provincia del donador: ")
            donadores, mensaje=insertarDonante(donadores, cedula, nombre, edad, sexo, tipoSangre, provincia, tiposDeSangre)
            print(mensaje)
        elif opcion=="2":
            print("Modificar donante pendiente.")
        elif opcion=="3":
            print("\n===== ELIMINAR DONANTE =====\n")
            cedula=input("Ingrese la cédula del donador a eliminar: ")
            donadores,mensaje=eliminarDonante(cedula,donadores)
            print(mensaje)
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
