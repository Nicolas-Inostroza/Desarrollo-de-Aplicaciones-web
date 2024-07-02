import re
import filetype
from database import db

error=""

def validate_nombre(nombre):
    if nombre is None:
        return False
    regex = r'^[a-zA-Z ]+$'
    if re.match(regex,nombre):
        if len(nombre)<81 and len(nombre)>2:
            return True
    global error 
    error ="Nombre invalido."
    return False


def validate_numero(numero):
    if numero is None or len(numero)==0:
        return True
    else:
        regex = r'^\+\d{2}-\d{3}-\d{3}-\d{3}$'

        if re.match(regex,numero):
            return True
    global error
    error="Numero Incorrecto."
    return False


def validate_email(mail):
    global error
    if mail is None:
        
        error="Email Incorrecto."
        return False
    
    regex= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex,mail):
        
        return True
    else:
        error="Email Incorrecto."
        return False

def validate_tipo(tipo):
    tipos=["fruta","verdura"]
    if(tipo in tipos):
        
        return True
    global error
    error="Tipo invalido."
    return False

def validate_Fruta_Verdura(seleccion):
    print(seleccion)
    if seleccion is None or len(seleccion)>5:
        return False
    for i in range(len(seleccion)):
        print(db.get_fruta_verdura_by_name(seleccion[i]))

        if db.get_fruta_verdura(seleccion[i]) is None:
            global error
            error="Producto seleccionado invalido"
            return False
    return True
    
def validate_region(region):
    print(region)
    algo = db.get_region_name(region)
    if algo is not None:
        return True
    else:
        global error
        error="Región Invalida"
        return False
    
def validate_comnuna(comuna):
    if db.get_comuna_name(comuna) is not None:
        return True
    else:
        global error
        error="Comuna Invalida."
        return False
    
def validate_fotos(fotos):
    
    if fotos is None:
        
        return False
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif", "image/jpg"}
    for foto in fotos:
        if foto is None or foto.filename =="":
            
            return False
        type_guess = filetype.guess(foto)
        try:
            if type_guess.extension not in ALLOWED_EXTENSIONS or type_guess.mime not in ALLOWED_MIMETYPES:
                
                return False
        except Exception as e:
            
            return False
    
    return True

def validate_producto(nombre,telefono,mail,region,comuna,fotos,tipo,fruta_verdura):
    if validate_nombre(nombre) and validate_numero(telefono) and validate_region(region) and validate_comnuna(comuna)\
    and validate_Fruta_Verdura(fruta_verdura) and validate_email(mail) and validate_fotos(fotos) and validate_tipo(tipo):
        return True
    else:
        return False
    
def validate_pedido(nombre,telefono,mail,region,comuna,tipo,fruta_verdura):
    if validate_nombre(nombre) and validate_numero(telefono) and validate_region(region) and validate_comnuna(comuna)\
    and validate_Fruta_Verdura(fruta_verdura) and validate_email(mail)and validate_tipo(tipo):
        return True,None
    else:
        return False,error
    
    


