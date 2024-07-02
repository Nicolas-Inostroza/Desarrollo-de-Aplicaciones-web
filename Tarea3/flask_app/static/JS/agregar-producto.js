
//-----------------------------------------------//

const createselectsregionComuna=()=>{
    const selectregion=document.getElementById("Región");
    const selectCom=document.getElementById("comuna1")
    const region=selectregion.value;
    var numero = selectRegion.selectedIndex;
    numero-=1;
    selectCom.innerHTML="";
    if (region == regiones[numero]) {
        for(var i=0;i<comunas[numero].length;i++){
          const option = document.createElement("option");
          option.innerText = comunas[numero][i];
          option.value = comunas[numero][i];
          selectCom.appendChild(option);
         }
    }else{
        const option = document.createElement("option");
        option.innerText = "Seleccione una Región";
        option.value = "";
        selectCom.appendChild(option);
    }
}
const createselectsTipoFrutVerd=()=>{
    const selectTipo=document.getElementById("tipo");
    const selectFrutVerd=document.getElementById("fruta_verdura")
    const Tipo=selectTipo.value;
    var numero = selectTipo.selectedIndex;
    numero-=1;
    selectFrutVerd.innerHTML="";
    if (Tipo == Tipos[numero]) {
        for(var i=0;i<FrutVerd[numero].length;i++){
            const option = document.createElement("option");
            option.innerText = FrutVerd[numero][i];
            option.value = FrutVerd[numero][i];
            selectFrutVerd.appendChild(option);
            }
    }else{
        const option = document.createElement("option");
        option.innerText = "Seleccione una Región";
        option.value = "";
        selectFrutVerd.appendChild(option);
    }
}
//----------------------------------------------------------//
var confirmDiv=document.getElementById("confirm");
const mostrarConfirm=()=>{
    confirmDiv.style.display="block";
    return;
}
const ocultarConfirm=()=>{
    confirmDiv.style.display="none";
    return;
}
const clickSi=()=>{
    ocultarConfirm();
    alert("Hemos recibido el registro de producto.")
    const form = document.getElementById("formulario")
    form.submit();
}
//Validaciones:

const amountOfThingsisValid=()=>{
    const seleccion=document.getElementById("fruta_verdura");
    const selectedOptions = Array.from(seleccion.selectedOptions);
    const cantidad = selectedOptions.length;
    if (cantidad >=1 && cantidad <= 5){
        return true
    }
    else{
        return false
    }
}

const emailisvalid= email =>{
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

const nombreisvalid=nombre =>{
    console.log(nombre.length);
    if(nombre.length<3 | nombre.length>80){
        return false;
    }
    else{
        return true;
    }
}

const numeroisvalid=numero=>{
    if(numero.length == 0){
        return true
    }
    const numeroregex=/^\+\d{2}-\d{3}-\d{3}-\d{3}$/;
    return numeroregex.test(numero);
}

const selectisValid = option =>{
    if(option.value!==""){
        return true;
    }
    else{
        return false;
    }
}
const fotosisValid=fotos=>{
    if(fotos.length<1 | fotos.length > 3){
        return false;
    }
    return true;
}
//-------------------------- Definicion de const-------------------------------------------//
const regiones=["Región de Tarapacá","Región de Antofagasta",
"Región de Atacama","Región de Coquimbo ","Región de Valparaíso",
"Región del Libertador Bernardo O'Higgins","Región del Maule","Región del Biobío",
"Región de La Araucanía","Región de Los Lagos","Región Aisén del General Carlos Ibáñez del Campo",
"Región de Magallanes y la Antártica Chilena","Región Metropolitana de Santiago ","Región de Los Ríos",
"Región Arica y Parinacota","Región del Ñuble"]


const comunas1=["Iquique","Alto Hospicio","Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
const comunas2=["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]
const comunas3=["Copiapó","Caldera","Tierra Amarilla", "Chañaral","Diego de Almagro","Vallenar","Alto del Carmen","Freirina", "Huasco"]
const comunas4=["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
const comunas5=["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
const comunas6=["Rancagua","Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
const comunas7=["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
const comunas8=["Concepción","Coronel","Chiguayante","Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío"]
const comunas9=["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"]
const comunas10=["Puerto Montt","Calbuco","Cochamó","Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas","Castro","Ancud","Chonchi","Curaco de Vélez","Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
const comunas11=["Coyhaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
const comunas12=["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
const comunas13=["Cerrillos","Cerro Navia","Conchalí","El Bosque","Estación Central","Huechuraba","Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "Santiago", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
const comunas14=["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
const comunas15=["Arica","Camarones","Putre","General Lagos"]
const comunas16=["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"]
const comunas=[comunas1,comunas2,comunas3,comunas4,comunas5,comunas6,comunas7,comunas8,comunas9,comunas10,comunas11,comunas12,comunas13,comunas14,comunas15,comunas16];
const fruits = ['Arándano', 'Frambuesa', 'Frutilla', 'Grosella', 'Mora', 'Limón', 'Mandarina', 'Naranja', 'Pomelo', 'Melón', 'Sandía', 'Palta', 'Chirimoya', 'Coco', 'Dátil', 'Kiwi', 'Mango', 'Papaya', 'Piña', 'Plátano', 'Damasco', 'Cereza', 'Ciruela', 'Higo', 'Kaki', 'Manzana', 'Durazno', 'Nectarin', 'Níspero', 'Pera', 'Uva', 'Almendra', 'Avellana', 'Maní', 'Castaña', 'Nuez', 'Pistacho']
const vegetables = ['Brócoli', 'Repollo', 'Coliflor', 'Rábano', 'Alcachofa', 'Lechuga', 'Zapallo', 'Pepino', 'Haba', 'Maíz', 'Champiñón', 'Acelga', 'Apio', 'Espinaca', 'Perejil', 'Ajo', 'Cebolla', 'Espárrago', 'Puerro', 'Acelga', 'Remolacha', 'Berenjena', 'Papa', 'Pimiento', 'Tomate', 'Zanahoria']
const FrutVerd=[fruits,vegetables]
const Tipos=["fruta","verdura"]



const selectRegion=document.getElementById("Región");
const selectComuna=document.getElementById("comuna1");
const selectTipo=document.getElementById("tipo");
const selectFrutVerd=document.getElementById("fruta_verdura")
const Imagens=document.querySelector("#imagenes");
const descripProducto=document.getElementById("descripción-text-area");
const nombreProducto=document.getElementById("nombre-text-area");
const numeroProducto=document.getElementById("num-text-area");
const emailProducto=document.getElementById("email-text-area");

const addProduct=()=>{
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
    mostrarConfirm();
}

const bottonEnvio=document.getElementById("submit-btn");
const bottonSi=document.getElementById("si");
const bottonNo=document.getElementById("no");
bottonSi.addEventListener("click",clickSi);
bottonNo.addEventListener("click",ocultarConfirm);
bottonEnvio.addEventListener("click",addProduct);

window.onload=function() {
    //get the divs to show/hide
    for(var i=0;i<regiones.length;i++){

        const region=document.createElement("option");
        region.value=regiones[i];
        region.innerText=regiones[i];
        selectRegion.appendChild(region);
    }
    for(var i=0;i<Tipos.length;i++){

        const Tipo=document.createElement("option");
        Tipo.value=Tipos[i];
        Tipo.innerText=Tipos[i];
        selectTipo.appendChild(Tipo);
    }
    
    divsO = document.getElementById("formulario").getElementsByTagName('div');
    for(var i=0; i < divsO.length; i++) {
        divsO[i].style.display = 'none';
    }
    const mostrar=["divfruta","fotos","descripción","nombre","numero","email","divcomuna1"];
    for(var i=0;i<mostrar.length;i++){
        document.getElementById(mostrar[i]).style.display = 'block';
    }


}