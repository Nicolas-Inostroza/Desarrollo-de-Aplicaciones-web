var mostrada=0;
const agrandar=()=>{
    const imagengrande=document.getElementById("imagengrande");
    mostrada=1;
    imagengrande.style.display="block";
}

const ocultar=()=>{
    const imagen=document.getElementById("imagengrande");
    imagen.style.display="none";
}

const clickimg=document.getElementById("imageninicial");
clickimg.addEventListener("click",agrandar);
const clickimggrande=document.getElementById("imagengrande");

if(mostrada=1){
    clickimggrande.addEventListener("click",ocultar);
}

