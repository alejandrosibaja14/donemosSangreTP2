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

def buscarDonadorPorCedula(matrizBaseDatos, cedulaBuscar):
    indice = 0
    donadorEncontrado = [] 
    while indice < len(matrizBaseDatos):
        filaActual = matrizBaseDatos[indice]
        if filaActual[1] == cedulaBuscar:
            donadorEncontrado = filaActual
            indice = len(matrizBaseDatos)
        else:
            indice = indice + 1
            
    return donadorEncontrado

def actualizarDatos(
    matrizBase, 
    cedula, 
    columna, 
    nuevoDato
):
    indice= 0
    largo= len(matrizBase)
    exito= False
    mensaje= "Error: Cedula no existe"
    while indice< largo:
        fila= matrizBase[indice]
        if fila[1]== cedula:
            fila[columna]= nuevoDato
            matrizBase[indice]= fila
            exito= True
            mensaje= "Dato actualizado"
            indice= largo
        else:
            indice= indice + 1
    return [
        matrizBase, 
        mensaje, 
        exito
    ]

import datetime

def generarReporteProvincia(
    matrizBase,
    nombreProvincia,
    lugaresProvincia
):
    donadoresFiltrados = []
    indice = 0
    total = len(matrizBase)
    
    while indice < total:
        fila = matrizBase[indice]
        esActivo = fila[8]
        
        lugarDonacion = fila[9]
        
        if esActivo == True:
            indLugar = 0
            totLugares = len(
                lugaresProvincia
            )
            encontrado = False
            
            while indLugar < totLugares:
                lugarActual = (
                    lugaresProvincia[
                        indLugar
                    ]
                )
                if lugarActual == lugarDonacion:
                    encontrado = True
                    indLugar = totLugares
                else:
                    indLugar = indLugar + 1
                    
            if encontrado == True:
                donadoresFiltrados = (
                    donadoresFiltrados +
                    [fila]
                )
        indice = indice + 1
        
    totalFiltro = len(donadoresFiltrados)
    indI = 0
    
    while indI < (totalFiltro - 1):
        indJ = 0
        limite = totalFiltro - indI - 1
        
        while indJ < limite:
            donador1 = (
                donadoresFiltrados[indJ]
            )
            donador2 = (
                donadoresFiltrados[
                    indJ + 1
                ]
            )
            
            nom1 = donador1[0]
            texto1 = (
                nom1[1] + nom1[2] + nom1[0]
            )
            
            nom2 = donador2[0]
            texto2 = (
                nom2[1] + nom2[2] + nom2[0]
            )
            if texto1 > texto2:
                temp = donadoresFiltrados[
                    indJ
                ]
                donadoresFiltrados[
                    indJ
                ] = donadoresFiltrados[
                    indJ + 1
                ]
                donadoresFiltrados[
                    indJ + 1
                ] = temp
                
            indJ = indJ + 1
        indI = indI + 1
    try:
        fechaHora = str(
            datetime.datetime.now()
        )
        
        html = "<!DOCTYPE html>\n"
        html = html + "<html>\n<head>\n"
        html = html + "<title>"
        html = html + "Reporte "
        html = html + nombreProvincia
        html = html + "</title>\n"
        html = html + "</head>\n<body>\n"
        html = html + "<h2>"
        html = html + "Reporte Donantes: "
        html = html + nombreProvincia
        html = html + "</h2>\n"
        html = html + "<p>Fecha: "
        html = html + fechaHora
        html = html + "</p>\n"
        html = html + "<table border='1'>\n"
        html = html + "<tr>"
        html = html + "<th>Cedula</th>"
        html = html + "<th>Nombre</th>"
        html = html + "<th>Nacimiento</th>"
        html = html + "<th>Telefono</th>"
        html = html + "<th>Correo</th>"
        html = html + "</tr>\n"
        indHtml = 0
        while indHtml < totalFiltro:
            filaH = donadoresFiltrados[
                indHtml
            ]
            ced = str(filaH[1])
            nomCom = (
                filaH[0][0] + " " +
                filaH[0][1] + " " +
                filaH[0][2]
            )
            nac = str(filaH[4])
            tel = str(filaH[7])
            cor = str(filaH[6])
            html = html + "<tr>"
            html = html + "<td>" + ced + "</td>"
            html = html + "<td>" + nomCom + "</td>"
            html = html + "<td>" + nac + "</td>"
            html = html + "<td>" + tel + "</td>"
            html = html + "<td>" + cor + "</td>"
            html = html + "</tr>\n"
            indHtml = indHtml + 1
        html = html + "</table>\n"
        html = html + "</body>\n</html>"
        nombreArch = (
            "Reporte_" + 
            nombreProvincia + 
            ".html"
        )
        archivo = open(
            nombreArch, 
            "w", 
            encoding="utf-8"
        )
        archivo.write(html)
        archivo.close()
        
        return "Reporte creado satisfactoriamente"
        
    except:
        return "Reporte no creado."

def reporteSangreProvincia(
    matrizBase,
    tipoSangreStr,
    nombreProv,
    lugaresProv,
    tuplaSangre
):
    indSangre = 0
    totSangre = len(tuplaSangre)
    sangreBuscada = -1
    while indSangre < totSangre:
        if tuplaSangre[indSangre] == tipoSangreStr:
            sangreBuscada = indSangre
        indSangre = indSangre + 1
    filtrados = []
    ind = 0
    totBase = len(matrizBase)
    while ind < totBase:
        fila = matrizBase[ind]
        activo = fila[8]
        sangreAct = fila[2]
        lugar = fila[9] 
        if activo == True:
            if sangreAct == sangreBuscada:
                indLugar = 0
                totLug = len(lugaresProv)
                esDeProv = False
                while indLugar < totLug:
                    lugarRev = lugaresProv[indLugar]
                    if lugarRev == lugar:
                        esDeProv = True
                        indLugar = totLug
                    else:
                        indLugar = indLugar + 1
                        
                if esDeProv == True:
                    filtrados = filtrados + [fila]    
        ind = ind + 1
    try:
        fechaActual = str(datetime.datetime.now())
        html = "<!DOCTYPE html>\n"
        html = html + "<html>\n<head>\n"
        html = html + "<title>Emergencia " + tipoSangreStr + "</title>\n"
        html = html + "</head>\n<body>\n"
        html = html + "<h2>Reporte " + tipoSangreStr + " en " + nombreProv + "</h2>\n"
        html = html + "<p>Fecha: " + fechaActual + "</p>\n"
        html = html + "<table border='1'>\n"
        html = html + "<tr>"
        html = html + "<th>Cedula</th>"
        html = html + "<th>Nombre</th>"
        html = html + "<th>Nac.</th>"
        html = html + "<th>Tel</th>"
        html = html + "<th>Correo</th>"
        html = html + "</tr>\n"
        indH = 0
        totFiltrados = len(filtrados)
        while indH < totFiltrados:
            f = filtrados[indH]
            ced = str(f[1])
            nom = f[0][0] + " " + f[0][1] + " " + f[0][2]
            nac = str(f[4])
            tel = str(f[7])
            cor = str(f[6])
            html = html + "<tr>"
            html = html + "<td>" + ced + "</td>"
            html = html + "<td>" + nom + "</td>"
            html = html + "<td>" + nac + "</td>"
            html = html + "<td>" + tel + "</td>"
            html = html + "<td>" + cor + "</td>"
            html = html + "</tr>\n"
            indH = indH + 1
        html = html + "</table>\n"
        html = html + "</body>\n</html>"
        nomArch = "Emergencia_" + nombreProv + ".html"     
        archivo = open(nomArch, "w", encoding="utf-8")
        archivo.write(html)
        archivo.close()
        return "Reporte creado satisfactoriamente"
               
    except:
        return "Reporte no creado."

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

def insertarLugarDonacion(plugaresDonacion,pdonadores,pcedula,pprovincia):
    donadorEncontrado=False
    for donador in pdonadores:
        if donador[0]==pcedula:
            donadorEncontrado=True
            if donador[6]==False:
                return plugaresDonacion,"El donador está inactivo."
            if pprovincia not in plugaresDonacion:
                return plugaresDonacion,"La provincia ingresada no existe."
            if pcedula in plugaresDonacion[pprovincia]:
                return plugaresDonacion,"El donador ya fue agregado en esta provincia."
            plugaresDonacion[pprovincia].append(pcedula)
            return plugaresDonacion,"Lugar de donación agregado correctamente."
    if not donadorEncontrado:
        return plugaresDonacion,"El donador no existe."
    
def obtenerReporteGeneral(pdonadores):
    activos=0
    inactivos=0
    for donador in pdonadores:
        if donador[6]:
            activos+=1
        else:
            inactivos+=1
    return activos,inactivos

def contarDatos(pdonadores,pindice,pcategorias):
    conteo={}
    for categoria in pcategorias:
        conteo[categoria]=0
    for donador in pdonadores:
        dato=donador[pindice]
        if dato in conteo:
            conteo[dato]+=1
    return conteo

def modificarLugarDonacion(plugaresDonacion,pcedula,pnuevaProvincia):
    if pnuevaProvincia not in plugaresDonacion:
        return plugaresDonacion,"La provincia ingresada no existe."
    for provincia in plugaresDonacion:
        if pcedula in plugaresDonacion[provincia]:
            plugaresDonacion[provincia].remove(pcedula)
            plugaresDonacion[pnuevaProvincia].append(pcedula)
            return plugaresDonacion,"Lugar de donación modificado correctamente."
    return plugaresDonacion,"El donador no tiene lugar de donación registrado."

def eliminarLugarDonacion(plugaresDonacion,pcedula):
    for provincia in plugaresDonacion:
        if pcedula in plugaresDonacion[provincia]:
            plugaresDonacion[provincia].remove(pcedula)
            return plugaresDonacion,"Lugar de donación eliminado correctamente."
    return plugaresDonacion,"El donador no tiene lugar de donación registrado."

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
            print("\n===== INSERTAR LUGAR DE DONACIÓN =====\n")
            cedula=input("Ingrese la cédula del donador: ")
            provincia=input("Ingrese la provincia: ").title()
            lugaresDeDonacion,mensaje=insertarLugarDonacion(lugaresDeDonacion, donadores, cedula, provincia)
            print(mensaje)
        elif opcion=="6":
            print("\n===== MODIFICAR LUGAR DE DONACIÓN =====\n")
            cedula=input("Ingrese la cédula del donador: ")
            nuevaProvincia=input("Ingrese la nueva provincia: ").title()
            lugaresDeDonacion,mensaje=modificarLugarDonacion(lugaresDeDonacion,cedula,nuevaProvincia)
            print(mensaje)
        elif opcion=="7":
            print("\n===== ELIMINAR LUGAR DE DONACIÓN =====\n")
            cedula=input("Ingrese la cédula del donador: ")
            lugaresDeDonacion,mensaje=eliminarLugarDonacion(lugaresDeDonacion,cedula)
            print(mensaje)
        elif opcion=="8":
            print("\n===== REPORTES =====\n")
            print("1. Cantidad de donadores por tipo de sangre")
            print("2. Cantidad de donadores por provincia")
            print("3. Donadores activos e inactivos")
            opcionReporte=input("Seleccione el reporte que desea visualizar: ")
            if opcionReporte=="1":
                resultado=contarDatos(donadores,4,tiposDeSangre)
                for tipo in resultado:
                    print(tipo+":",resultado[tipo])
            elif opcionReporte=="2":
                provincias=("San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón")
                resultado=contarDatos(donadores,5,provincias)
                for provincia in resultado:
                    print(provincia+":",resultado[provincia])
            elif opcionReporte=="3":
                activos, inactivos=obtenerReporteGeneral(donadores)
                print("Donadores activos:",activos)
                print("Donadores inactivos:",inactivos)
        elif opcion=="9":
            print("Donar sangre, es donar vida")
            break
        else:
            print("Opción inválida.")

#Inicio del programa principal
main()
