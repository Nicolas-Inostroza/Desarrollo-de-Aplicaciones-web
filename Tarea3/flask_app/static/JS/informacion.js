
const pag_1=()=>{
    window.location.href = "/ver-productos?page_size=5&offset=0";

}

const pag_2=() => {
    window.location.href = "/ver-productos?page_size=10&offset=5";
}

const cambiodeImagen = (path, name) => {
    const imgdiv = document.getElementById("imagengrande");
    const imgpath = "/" + path + "/1280x1024_" + name;

    // Check if the image is already visible
    if (imgdiv.innerHTML.includes(imgpath)) {
        // If yes, hide the image
        imgdiv.innerHTML = "";
        imgdiv.style.display="none";
    } else {
        // If not, show the image
        imgdiv.innerHTML = "<img src='" + imgpath + "' class='foto' onclick='cambiodeImagen(\"" + path + "\", \"" + name + "\")'>";
        imgdiv.style.display="block";

    }
}

const anterior = document.getElementById("anterior")
anterior.addEventListener("click", pag_1)

const siguiente =document.getElementById("b2")
siguiente.addEventListener("click", pag_2) 

