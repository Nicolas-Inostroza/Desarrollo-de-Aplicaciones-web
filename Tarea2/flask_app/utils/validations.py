import re
import filetype
from database import db


def validate_nombre(nombre):
    if nombre is None:
        return False
    regex = r'^[a-zA-Z ]+$'
    if re.match(regex,nombre):
        if len(nombre)<81 and len(nombre)>2:
            return True
    return False


def validate_numero(numero):
    if numero is None or len(numero)==0:
        return True
    else:
        regex = r'^\+\d{2}-\d{3}-\d{3}-\d{3}$'

        if re.match(regex,numero):
            return True
    return False


def validate_email(mail):
    if mail is None:
        return False
    
    regex= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex,mail):
        
        return True
    else:
        
        return False

def validate_tipo(tipo):
    tipos=["fruta","verdura"]
    if(tipo in tipos):
        
        return True
    
    return False

def validate_Fruta_Verdura(seleccion):
    
    if seleccion is None or len(seleccion)>5:
        return False
    for i in range(len(seleccion)):
        if db.get_fruta_verdura(seleccion[i]) is None:
            return False
    return True
    
def validate_region(region):
    algo = db.get_region_name(region)
    if algo is not None:
        return True
    else:
        return False
    
def validate_comnuna(comuna):
    if db.get_comuna_name(comuna) is not None:
        return True
    else:
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
    
    


