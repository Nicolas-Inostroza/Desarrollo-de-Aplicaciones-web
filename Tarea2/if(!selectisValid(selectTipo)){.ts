if(!selectisValid(selectTipo)){
        selectTipo.style.borderColor="red"
        alert("Porfavor seleccione un Tipo.");
        return;
    }else selectTipo.style.borderColor=""
    if(!amountOfThingsisValid()){
        alert("Porfavor seleccione entre 1 y 5 "+selectTipo.value);
        return;
    }
    if(!fotosisValid(Imagens.files)){
        alert("Los archivos subidos deben ser imagenes con un maximo de 3");
        return;
    }
    if(!selectisValid(selectRegion)){
        selectRegion.style.borderColor="red"
        alert("Seleccione una Region.");
        return;
    }else selectRegion.style.borderColor=""

    if(!selectisValid(selectComuna)){
        selectComuna.style.borderColor="red"
        alert("Seleccione una comuna");
        return;
    }else selectComuna.style.borderColor=""

    console.log(nombreProducto.value.length);
    if(!nombreisvalid(nombreProducto.value)){
        nombreProducto.style.borderColor="red"
        alert("El nombre debe tener como minimo 3 caracteres y maximo 80");
        return;
    }else nombreProducto.style.borderColor=""

    if(!emailisvalid(emailProducto.value)){
        emailProducto.style.borderColor="red"
        alert("Formato/Tamaño de email incorrecto.");
        return;
    }else emailProducto.style.borderColor=""

    if(!numeroisvalid(numeroProducto.value)){
        numeroProducto.style.borderColor="red"
        alert("El numero no tiene el tamaño necesario.");
        return;
    }else numeroProducto.style.borderColor=""
    



    <label for="Región">Escoge una Región:</label><br>
    <select name = "Region" class="Tipo" id="Región" onchange="createselectsregionComuna()">
        <option value="">Seleccione una Región</option>
    </select><br>

    def validate_region(region):
    algo = db.get_region_name(region)
    if algo is not None:
        print("region true")
        return True
    else:
        print("region false")
        return False

    def get_region_name(region):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(QUERY_DICT["get_region"], (region,))
        region_name = cursor.fetchone()
        return region_name
    
    "get_region":"SELECT nombre FROM region WHERE nombre = %s"