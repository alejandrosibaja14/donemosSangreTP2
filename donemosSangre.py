#Creado por: Alejandro Sibaja Badilla y Marco Herrera Gómez
#Fecha de creación: 16/05/2026
#Ultima actualización: xx/05/2026
#Versión de python: 3.14
#Definición de funciones
import re
import datetime
tiposDeSangre=(
    "O+",
    "O-",
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-"
)

justificaciones=(
    "No aplica",
    "Enfermedades infecciosas o crónicas",
    "Conductas de riesgo",
    "Factores de salud física",
    "Procedimientos médicos recientes",
    "Uso de medicamentos",
    "Estilo de vida o viajes recientes",
    "Situaciones específicas"
)

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

def reporteMujeresONegativo(matrizBase, tuplaSangre):
    indSangre = 0
    totSangre = len(tuplaSangre)
    sangreONeg = -1
    while indSangre < totSangre:
        if tuplaSangre[indSangre] == "O-":
            sangreONeg = indSangre
        indSangre = indSangre + 1
    fechaHoy = datetime.datetime.now()
    anioActual = fechaHoy.year
    filtradas = []
    ind = 0
    totBase = len(matrizBase)
    while ind < totBase:
        fila = matrizBase[ind]
        esActivo = fila[8]
        sexo = fila[3] 
        tipoSangre = fila[2]
        if esActivo == True:
            if sexo == False:
                if tipoSangre == sangreONeg:
                    fechaNac = str(fila[4])
                    partes = fechaNac.split("/")
                    if len(partes) != 3:
                        partes = fechaNac.split("-")
                    anioNacimiento = int(partes[2])
                    edad = anioActual - anioNacimiento
                    if edad < 45:
                        filtradas = filtradas + [fila]
        ind = ind + 1
    totFiltradas = len(filtradas)
    indI = 0
    while indI < (totFiltradas - 1):
        indJ = 0
        limite = totFiltradas - indI - 1
        while indJ < limite:
            donadora1 = filtradas[indJ]
            donadora2 = filtradas[indJ + 1]
            fNac1 = str(donadora1[4])
            p1 = fNac1.split("/")
            if len(p1) != 3:
                p1 = fNac1.split("-")
            edad1 = anioActual - int(p1[2])
            fNac2 = str(donadora2[4])
            p2 = fNac2.split("/")
            if len(p2) != 3:
                p2 = fNac2.split("-")
            edad2 = anioActual - int(p2[2])
            if edad1 > edad2:
                temp = filtradas[indJ]
                filtradas[indJ] = filtradas[indJ + 1]
                filtradas[indJ + 1] = temp
            indJ = indJ + 1
        indI = indI + 1
    try:
        fechaHoraStr = str(datetime.datetime.now())
        html = "<!DOCTYPE html>\n"
        html = html + "<html>\n<head>\n"
        html = html + "<title>Mujeres Donantes O-</title>\n"
        html = html + "</head>\n<body>\n"
        html = html + "<h2>Reporte: Mujeres Donantes O- (Menores a 45)</h2>\n"
        html = html + "<p>Fecha y hora del sistema: " + fechaHoraStr + "</p>\n"
        html = html + "<table border='1'>\n"
        html = html + "<tr>"
        html = html + "<th>Cedula</th>"
        html = html + "<th>Nombre Completo</th>"
        html = html + "<th>Fecha de nacimiento</th>"
        html = html + "<th>Telefono</th>"
        html = html + "<th>Correo</th>"
        html = html + "</tr>\n"
        indH = 0
        while indH < totFiltradas:
            f = filtradas[indH]
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
        archivo = open("Reporte_Mujeres_O_Negativo.html", "w", encoding="utf-8")
        archivo.write(html)
        archivo.close()
        return "Reporte creado satisfactoriamente"
    except:
        return "Reporte no creado."

def validarCedula(pcedula):
    """
    Funcionamiento: Valida la cédula con formato #-####-#### y primer dígito diferente de 0.
    Entradas: pcedula: cédula ingresada.
    Salidas: True si cumple, False si no cumple.
    """
    patron=r"^[1-9]-\d{4}-\d{4}$"
    if re.match(patron,pcedula):
        return True
    return False

def validarFechaNacimiento(pfecha):
    """
    Funcionamiento: Valida que la fecha tenga formato DD/MM/AAAA.
    Entradas: pfecha: fecha ingresada.
    Salidas: True si cumple el formato, False si no.
    """
    patron=r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"
    if re.match(patron,pfecha):
        return True
    return False

def validarCorreo(pcorreo):
    """
    Funcionamiento: Valida que el correo tenga uno de los dominios permitidos.
    Entradas: pcorreo: correo ingresado.
    Salidas: True si el correo es válido, False si no.
    """
    patron=r"^[a-zA-Z0-9]+@(costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr|gmail\.com)$"
    if re.match(patron,pcorreo):
        return True
    return False

def validarTelefono(ptelefono):
    """
    Funcionamiento: Valida teléfono con formato ####-#### y primer dígito diferente de 0, 1, 3 y 5.
    Entradas: ptelefono: teléfono ingresado.
    Salidas: True si cumple, False si no.
    """
    patron=r"^[246789]\d{3}-\d{4}$"
    if re.match(patron,ptelefono):
        return True
    return False

def validarPeso(ppeso):
    """
    Funcionamiento: Valida que el peso sea numérico, mayor a 50 y menor a 120.
    Entradas: ppeso: peso ingresado.
    Salidas: True si es válido, False si no.
    """
    try:
        peso=float(ppeso)
        if peso>50 and peso<120:
            return True
        return False
    except:
        return False

def validarTipoSangre(ptipoSangre,ptiposDeSangre):
    """
    Funcionamiento: Verifica que el tipo de sangre exista en la tupla global.
    Entradas: ptipoSangre: tipo de sangre ingresado.
            ptiposDeSangre: tupla de tipos de sangre.
    Salidas: True si existe, False si no existe.
    """
    if ptipoSangre in ptiposDeSangre:
        return True
    return False

def obtenerIndiceTipoSangre(ptipoSangre,ptiposDeSangre):
    """
    Funcionamiento: Obtiene la posición del tipo de sangre dentro de la tupla.
    Entradas: ptipoSangre: tipo de sangre.
            ptiposDeSangre: tupla de tipos de sangre.
    Salidas: Índice del tipo de sangre o -1 si no existe.
    """
    indice=0
    while indice<len(ptiposDeSangre):
        if ptiposDeSangre[indice]==ptipoSangre:
            return indice
        indice+=1
    return -1

def validarCamposRequeridos(plistaCampos):
    """
    Funcionamiento: Verifica que todos los campos obligatorios tengan información.
    Entradas: plistaCampos: lista con los valores ingresados.
    Salidas: True si todos tienen datos, False si alguno está vacío.
    """
    for campo in plistaCampos:
        if str(campo).strip()=="":
            return False
    return True

def eliminarDonante(pbaseDatos,pcedula,pjustificacion,pconfirmacion):
    """
    Funcionamiento: Cambia el estado de un donador a inactivo y guarda la justificación.
    Entradas: pbaseDatos: matriz de donadores.
            pcedula: cédula del donador.
            pjustificacion: número de justificación de eliminación.
            pconfirmacion: respuesta de confirmación del usuario.
    Salidas: Base de datos actualizada y mensaje de retroalimentación.
    """
    if not validarCedula(pcedula):
        return pbaseDatos,"Cédula inválida. Vuelva a intentarlo."
    if not str(pjustificacion).isdigit():
        return pbaseDatos,"La justificación debe ser un número entre 1 y 7."
    justificacion=int(pjustificacion)
    if justificacion<1 or justificacion>7:
        return pbaseDatos,"La justificación debe ser un número entre 1 y 7."
    cedulaEntera=int(pcedula.replace("-",""))
    for donador in pbaseDatos:
        if donador[1]==cedulaEntera:
            if donador[8]==0:
                return pbaseDatos,"El donador ya se encuentra inactivo."
            if pconfirmacion.upper()!="S":
                return pbaseDatos,"Donador NO eliminado."
            donador[8]=0
            donador[9]=justificacion
            return pbaseDatos,"Donador eliminado satisfactoriamente."
    return pbaseDatos,"La persona con el número de cédula: "+pcedula+" no está registrado en la base de datos del Banco de Sangre aún."

def insertarDonador(pbaseDatos,pnombre,papellido1,papellido2,pcedula,ptipoSangre,psexo,pfechaNacimiento,ppeso,pcorreo,ptelefono,ptiposDeSangre):
    """
    Funcionamiento: Valida y registra un nuevo donador con la estructura de matriz solicitada.
    Entradas: Datos del donador y base de datos.
    Salidas: Base de datos actualizada, mensaje y retroalimentación adicional.
    """
    retroalimentacion=[]
    campos=[pnombre,papellido1,papellido2,pcedula,ptipoSangre,psexo,pfechaNacimiento,ppeso,pcorreo,ptelefono]
    if not validarCamposRequeridos(campos):
        return pbaseDatos,"Todos los datos son requeridos.",retroalimentacion
    if not validarCedula(pcedula):
        return pbaseDatos,"Cédula inválida. Use el formato #-####-####.",retroalimentacion
    cedulaEntera=int(pcedula.replace("-",""))
    if buscarDonadorPorCedula(pbaseDatos,cedulaEntera)!=[]:
        return pbaseDatos,"La persona con esa cédula ya está registrada.",retroalimentacion
    if not validarFechaNacimiento(pfechaNacimiento):
        return pbaseDatos,"Fecha inválida. Use el formato DD/MM/AAAA.",retroalimentacion
    if not validarTipoSangre(ptipoSangre,ptiposDeSangre):
        return pbaseDatos,"Tipo de sangre inválido.",retroalimentacion
    if not validarPeso(ppeso):
        return pbaseDatos,"Peso inválido. Debe ser mayor a 50 y menor a 120.",retroalimentacion
    if not validarCorreo(pcorreo):
        return pbaseDatos,"Correo inválido. Use un dominio permitido.",retroalimentacion
    if not validarTelefono(ptelefono):
        return pbaseDatos,"Teléfono inválido. Use formato ####-####.",retroalimentacion
    tipoIndice=obtenerIndiceTipoSangre(ptipoSangre,ptiposDeSangre)
    if tipoIndice==-1:
        return pbaseDatos,"Tipo de sangre inválido.",retroalimentacion
    if psexo!="Masculino" and psexo!="Femenino":
        return pbaseDatos,"Sexo inválido.",retroalimentacion
    sexo=True
    if psexo=="Femenino":
        sexo=False
    fechaPartes=pfechaNacimiento.split("/")
    fechaTupla=(fechaPartes[0],fechaPartes[1],fechaPartes[2])
    telefonoLimpio=ptelefono
    donador=[
        [pnombre.strip().title(),papellido1.strip().title(),papellido2.strip().title()],
        cedulaEntera,
        tipoIndice,
        sexo,
        fechaTupla,
        float(ppeso),
        pcorreo,
        telefonoLimpio,
        1,
        0
    ]
    pbaseDatos.append(donador)
    edad=calcularEdad(fechaTupla)
    retroalimentacion.append("Donador registrado correctamente.")
    retroalimentacion.append("Edad calculada: "+str(edad)+" años.")
    if edad>=18:
        retroalimentacion.append("Dado su fecha de nacimiento usted ya puede ser donador.")
    else:
        retroalimentacion.append("Dado su fecha de nacimiento usted aún no puede ser donador.")
    retroalimentacion.append("Peso registrado: "+str(ppeso)+" kg.")
    if ptipoSangre=="A+":
        retroalimentacion.append("A los donadores A+ se les recomienda donar sangre entera y plaquetas.")
    elif ptipoSangre=="A-":
        retroalimentacion.append("A los donadores A- se les recomienda donar sangre entera y glóbulos rojos dobles.")
    return pbaseDatos,"Registro realizado correctamente.",retroalimentacion

def insertarLugarDonacion(plugaresDonacion,pnumeroProvincia,pnuevoLugar):
    """
    Funcionamiento: Inserta un nuevo lugar de donación en una provincia específica.
    Entradas: plugaresDonacion: diccionario de lugares de donación.
            pnumeroProvincia: número de provincia.
            pnuevoLugar: nombre del nuevo lugar de donación.
    Salidas: Diccionario actualizado y mensaje de retroalimentación.
    """
    if not str(pnumeroProvincia).isdigit():
        return plugaresDonacion,"La provincia debe ser un número válido."
    numeroProvincia=int(pnumeroProvincia)
    if numeroProvincia not in plugaresDonacion:
        return plugaresDonacion,"La provincia ingresada no existe."
    if pnuevoLugar.strip()=="":
        return plugaresDonacion,"Debe ingresar un lugar de donación."
    lugarNuevo=pnuevoLugar.strip()
    for lugar in plugaresDonacion[numeroProvincia]:
        if lugar.lower()==lugarNuevo.lower():
            return plugaresDonacion,"Ese lugar ya está registrado en esta provincia."
    plugaresDonacion[numeroProvincia].append(lugarNuevo)
    return plugaresDonacion,"Lugar de donación insertado correctamente."

def calcularEdad(pfechaNacimiento):
    """
    Funcionamiento: Calcula la edad de una persona según su fecha de nacimiento.
    Entradas: pfechaNacimiento: fecha en formato tupla o string.
    Salidas: Edad calculada.
    """
    fechaActual=datetime.datetime.now() 
    if type(pfechaNacimiento)==str:
        partes=pfechaNacimiento.split("/")
        dia=int(partes[0])
        mes=int(partes[1])
        anno=int(partes[2])
    else:
        dia=int(pfechaNacimiento[0])
        mes=int(pfechaNacimiento[1])
        anno=int(pfechaNacimiento[2])
    edad=fechaActual.year-anno
    if fechaActual.month<mes:
        edad-=1
    elif fechaActual.month==mes and fechaActual.day<dia:
        edad-=1
    return edad

def generarReporteRangoEdad(pbaseDatos,pedadInicial,pedadFinal):
    """
    Funcionamiento: Genera un reporte HTML de donadores activos dentro de un rango de edad.
    Entradas: pbaseDatos: matriz de donadores.
            pedadInicial: edad inicial del rango.
            pedadFinal: edad final del rango.
    Salidas: Mensaje indicando si el reporte fue generado.
    """
    if not str(pedadInicial).isdigit() or not str(pedadFinal).isdigit():
        return "Las edades deben ser números."
    edadInicial=int(pedadInicial)
    edadFinal=int(pedadFinal)
    if edadInicial<18 or edadInicial>65 or edadFinal<18 or edadFinal>65:
        return "Las edades deben estar entre 18 y 65 años."
    if edadInicial>edadFinal:
        return "La edad inicial no puede ser mayor que la edad final."
    filtrados=[]
    for donador in pbaseDatos:
        if donador[8]==1:
            edad=calcularEdad(donador[4])
            if edad>=edadInicial and edad<=edadFinal:
                filtrados.append(donador)
    try:
        fechaHora=str(datetime.datetime.now())
        html="<!DOCTYPE html>\n"
        html+="<html>\n<head>\n"
        html+='<meta charset="UTF-8">\n'
        html+="<title>Reporte por rango de edad</title>\n"
        html+="</head>\n<body>\n"
        html+="<h1>Reporte por rango de edad</h1>\n"
        html+="<p>Fecha y hora del sistema: "+fechaHora+"</p>\n"
        html+="<table border='1'>\n"
        html+="<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n"
        for donador in filtrados:
            nombre=donador[0][0]+" "+donador[0][1]+" "+donador[0][2]
            cedula=str(donador[1])
            fecha=str(donador[4][0])+"/"+str(donador[4][1])+"/"+str(donador[4][2])
            telefono=str(donador[7])
            correo=donador[6]
            html+="<tr>"
            html+="<td>"+cedula+"</td>"
            html+="<td>"+nombre+"</td>"
            html+="<td>"+fecha+"</td>"
            html+="<td>"+telefono+"</td>"
            html+="<td>"+correo+"</td>"
            html+="</tr>\n"
        html+="</table>\n"
        html+="</body>\n</html>"
        archivo=open("reporte_rango_edad.html","w",encoding="utf-8")
        archivo.write(html)
        archivo.close()
        return "Reporte creado satisfactoriamente."
    except:
        return "El reporte no fue creado. Vuelva a intentarlo."
    
def generarReporteListaCompleta(pbaseDatos,ptiposDeSangre):
    """
    Funcionamiento: Genera un reporte HTML con la lista completa de donadores.
    Entradas: pbaseDatos: matriz de donadores.
            ptiposDeSangre: tupla con los tipos de sangre.
    Salidas: Mensaje indicando si el reporte fue generado.
    """
    try:
        fechaHora=str(datetime.datetime.now())
        html="<!DOCTYPE html>\n"
        html+="<html>\n<head>\n"
        html+='<meta charset="UTF-8">\n'
        html+="<title>Lista completa de donadores</title>\n"
        html+="</head>\n<body>\n"
        html+="<h1>Lista completa de donadores</h1>\n"
        html+="<p>Fecha y hora del sistema: "+fechaHora+"</p>\n"
        html+="<table border='1'>\n"
        html+="<tr>"
        html+="<th>Cédula</th>"
        html+="<th>Nombre completo</th>"
        html+="<th>Tipo de sangre</th>"
        html+="<th>Fecha de nacimiento</th>"
        html+="<th>Peso</th>"
        html+="<th>Sexo</th>"
        html+="<th>Teléfono</th>"
        html+="<th>Correo</th>"
        html+="</tr>\n"
        for donador in pbaseDatos:
            nombre=donador[0][0]+" "+donador[0][1]+" "+donador[0][2]
            cedula=str(donador[1])
            tipoSangre=ptiposDeSangre[donador[2]]
            fecha=str(donador[4][0])+"/"+str(donador[4][1])+"/"+str(donador[4][2])
            peso=str(donador[5])
            if donador[3]:
                sexo="Masculino"
            else:
                sexo="Femenino"
            telefono=str(donador[7])
            correo=donador[6]
            html+="<tr>"
            html+="<td>"+cedula+"</td>"
            html+="<td>"+nombre+"</td>"
            html+="<td>"+tipoSangre+"</td>"
            html+="<td>"+fecha+"</td>"
            html+="<td>"+peso+"</td>"
            html+="<td>"+sexo+"</td>"
            html+="<td>"+telefono+"</td>"
            html+="<td>"+correo+"</td>"
            html+="</tr>\n"
        html+="</table>\n"
        html+="</body>\n</html>"
        archivo=open("reporte_lista_completa.html","w",encoding="utf-8")
        archivo.write(html)
        archivo.close()
        return "Reporte creado satisfactoriamente."
    except:
        return "Reporte no creado."
    
def obtenerCompatibilidadDonacion(ptipoSangre):
    """
    Funcionamiento: Obtiene los tipos de sangre a los que puede donar una persona.
    Entradas: ptipoSangre: tipo de sangre del donador.
    Salidas: Lista con los tipos de sangre compatibles.
    """
    compatibilidad={
        "O-":["O-","O+","A-","A+","B-","B+","AB-","AB+"],
        "O+":["O+","A+","B+","AB+"],
        "A-":["A-","A+","AB-","AB+"],
        "A+":["A+","AB+"],
        "B-":["B-","B+","AB-","AB+"],
        "B+":["B+","AB+"],
        "AB-":["AB-","AB+"],
        "AB+":["AB+"]
    }
    if ptipoSangre in compatibilidad:
        return compatibilidad[ptipoSangre]
    return []

def generarReporteAQuienPuedeDonar(pbaseDatos,ptipoSangre,ptiposDeSangre):
    """
    Funcionamiento: Genera un reporte HTML con los donadores activos que pueden donar a un tipo de sangre indicado.
    Entradas: pbaseDatos: matriz de donadores.
            ptipoSangre: tipo de sangre consultado.
            ptiposDeSangre: tupla con los tipos de sangre.
    Salidas: Mensaje indicando si el reporte fue generado.
    """
    if ptipoSangre not in ptiposDeSangre:
        return "Tipo de sangre inválido."
    filtrados=[]
    for donador in pbaseDatos:
        if donador[8]==1:
            tipoDonador=ptiposDeSangre[donador[2]]
            compatibles=obtenerCompatibilidadDonacion(tipoDonador)
            if ptipoSangre in compatibles:
                filtrados.append(donador)
    try:
        fechaHora=str(datetime.datetime.now())
        html="<!DOCTYPE html>\n"
        html+="<html>\n<head>\n"
        html+='<meta charset="UTF-8">\n'
        html+="<title>Reporte a quién puede donar</title>\n"
        html+="</head>\n<body>\n"
        html+="<h1>Reporte: ¿A quién puede donar?</h1>\n"
        html+="<p>Fecha y hora del sistema: "+fechaHora+"</p>\n"
        html+="<p>Tipo de sangre solicitado: "+ptipoSangre+"</p>\n"
        html+="<table border='1'>\n"
        html+="<tr>"
        html+="<th>Cédula</th>"
        html+="<th>Nombre completo</th>"
        html+="<th>Tipo de sangre</th>"
        html+="<th>Teléfono</th>"
        html+="<th>Correo</th>"
        html+="</tr>\n"
        for donador in filtrados:
            nombre=donador[0][0]+" "+donador[0][1]+" "+donador[0][2]
            cedula=str(donador[1])
            tipoSangre=ptiposDeSangre[donador[2]]
            telefono=str(donador[7])
            correo=donador[6]
            html+="<tr>"
            html+="<td>"+cedula+"</td>"
            html+="<td>"+nombre+"</td>"
            html+="<td>"+tipoSangre+"</td>"
            html+="<td>"+telefono+"</td>"
            html+="<td>"+correo+"</td>"
            html+="</tr>\n"
        html+="</table>\n"
        html+="</body>\n</html>"
        archivo=open("reporte_a_quien_puede_donar.html","w",encoding="utf-8")
        archivo.write(html)
        archivo.close()
        return "Reporte creado satisfactoriamente."
    except:
        return "Reporte no creado. Vuelva a intentarlo."
    
def generarReporteDonantesNoActivos(pbaseDatos,pjustificaciones,ptiposDeSangre):
    """
    Funcionamiento: Genera un reporte HTML con los donadores que se encuentran inactivos.
    Entradas: pbaseDatos: matriz de donadores.
            pjustificaciones: tupla con las justificaciones de inactividad.
            ptiposDeSangre: tupla con los tipos de sangre.
    Salidas: Mensaje indicando si el reporte fue generado.
    """
    try:
        fechaHora=str(datetime.datetime.now())
        html="<!DOCTYPE html>\n"
        html+="<html>\n<head>\n"
        html+='<meta charset="UTF-8">\n'
        html+="<title>Donantes no activos</title>\n"
        html+="</head>\n<body>\n"
        html+="<h1>Reporte de donantes no activos</h1>\n"
        html+="<p>Fecha y hora del sistema: "+fechaHora+"</p>\n"
        html+="<table border='1'>\n"
        html+="<tr>"
        html+="<th>Cédula</th>"
        html+="<th>Nombre completo</th>"
        html+="<th>Tipo de sangre</th>"
        html+="<th>Teléfono</th>"
        html+="<th>Correo</th>"
        html+="<th>Justificación</th>"
        html+="</tr>\n"
        for donador in pbaseDatos:
            if donador[8]==0:
                nombre=donador[0][0]+" "+donador[0][1]+" "+donador[0][2]
                cedula=str(donador[1])
                tipoSangre=ptiposDeSangre[donador[2]]
                telefono=str(donador[7])
                correo=donador[6]
                numeroJustificacion=donador[9]
                if numeroJustificacion>=0 and numeroJustificacion<len(pjustificaciones):
                    justificacion=pjustificaciones[numeroJustificacion]
                else:
                    justificacion="Justificación no registrada"
                html+="<tr>"
                html+="<td>"+cedula+"</td>"
                html+="<td>"+nombre+"</td>"
                html+="<td>"+tipoSangre+"</td>"
                html+="<td>"+telefono+"</td>"
                html+="<td>"+correo+"</td>"
                html+="<td>"+justificacion+"</td>"
                html+="</tr>\n"
        html+="</table>\n"
        html+="</body>\n</html>"
        archivo=open("reporte_donantes_no_activos.html","w",encoding="utf-8")
        archivo.write(html)
        archivo.close()
        return "Reporte creado satisfactoriamente."
    except:
        return "Reporte no creado. Vuelva a intentarlo."
#Inicio del programa principal
