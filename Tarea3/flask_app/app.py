from flask import Flask, request, render_template, redirect, url_for,jsonify
from flask_cors import cross_origin
from utils.validations import validate_producto,validate_pedido
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
import uuid
from PIL import Image
UPLOAD_FOLDER = 'static/uploads'

app= Flask(__name__)

app.secret_key = "s3cr3t_k3y"


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGHT'] = 16 * 1000 * 1000

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File exceeds the maximum file size allowed'



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/agregar-producto", methods=["GET","POST"])
def agregar_producto():
    if request.method=="POST":
        nombre = request.form.get("nombre")
        telefono = request.form.get("numero")
        mail = request.form.get("email")
        region = request.form.get("Region")
        comuna = request.form.get("comuna")
        descripcion = request.form.get("descripcion")
        fotos = request.files.getlist("fotossubidas[]")
        fruta_verdura = request.form.getlist("frutverd[]")
        tipo= request.form.get("tipo")
        if validate_producto(nombre,telefono,mail,region,comuna,fotos,tipo,fruta_verdura):
            comuna_id = db.get_comuna_id(comuna)
            #agregar producto a la base de datos.
            db.insert_producto(tipo,descripcion,comuna_id,nombre,mail,telefono)
            producto_id = db.get_producto_id_by_name(nombre)
            for frutverd in fruta_verdura:
                fruta_verdura_id = db.get_fruta_verdura_id(frutverd)
                db.insert_producto_verdura_fruta(producto_id,fruta_verdura_id)
            for foto in fotos:
                agregarfoto(foto,nombre)

            return redirect(url_for("index"))
    return render_template("agregar/agregar-producto.html")


@app.route("/agregar-pedido", methods=["GET","POST"])
def agregar_pedido():
    error=request.args.get('error',None)
    print(error)
    if request.method=="POST":
        nombre = request.form.get("nombre")
        telefono = request.form.get("numero")
        mail = request.form.get("email")
        region = request.form.get("Region")
        comuna = request.form.get("comuna")
        descripcion = request.form.get("descripcion")
        fruta_verdura = request.form.getlist("frutverd[]")
        tipo= request.form.get("tipo")
        valido,error=validate_pedido(nombre,telefono,mail,region,comuna,tipo,fruta_verdura)
        if valido:
            comuna_id = db.get_comuna_id(comuna)
            #agregar producto a la base de datos.
            db.insert_pedido(tipo,descripcion,comuna_id,nombre,mail,telefono)
            pedido_id = db.get_pedido_id_by_name(nombre)
            print(fruta_verdura)
            for frutverd in fruta_verdura:
                fruta_verdura_id = db.get_fruta_verdura_id(frutverd)
                print("Fruta agregada",frutverd)
                db.insert_pedido_verdura_fruta(pedido_id,fruta_verdura_id)
            return redirect(url_for("index"))
    return render_template("agregar/agregar-pedido.html",error=error)

@app.route("/ver-pedido", methods=["GET"])
def ver_pedido():
    page= (int(request.args.get('page',0))+1)*5
    offset = (int(request.args.get('page',0)))*5
    if request.method=="GET":
        datos=[]
        pedidos = db.get_pedidos(page,offset)
        paginas = (True if len(db.get_pedidos(10,0))>=6 else False)
        if pedidos is not None:
            for pedido in pedidos:
                id, tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_productor = pedido
                comuna, region_id = db.get_comuna_by_id(comuna_id)
                region = db.get_region_by_id(region_id)
                frut_verd =  db.get_fruta_verdura(id)
                nombre=nombre_comprador
                final=""
                for i in frut_verd:
                    final=(i[0])+" "+final
                datos.append({
                    "tipo":tipo,
                    "frut_verd":final,
                    "comuna":comuna,
                    "region": region[0],
                    "nombre": nombre,
                    "productor_id":id})
    return render_template("ver/pedidos.html",datos=datos,paginas=paginas)

@app.route("/ver-producto", methods=["GET"])
def ver_producto():
    page= (int(request.args.get('page',0))+1)*5
    offset = (int(request.args.get('page',0)))*5
    if request.method=="GET":
        datos=[]
        productos = db.get_productos(page,offset)
        paginas = (True if len(db.get_productos(10,0))>=6 else False)
        print(paginas)
        if productos is not None:
            for producto in productos:
                id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor = producto
                comuna, region_id = db.get_comuna_by_id(comuna_id)
                region = db.get_region_by_id(region_id)
                img_path,img_filename = db.get_fotos_producto(id)[0]
                frut_verd =  db.get_fruta_verdura(id)
                final=""
                for i in frut_verd:
                    final=(i[0])+" "+final
                img_filename="/"+img_path+"/"+img_filename
                datos.append({
                    "tipo":tipo,
                    "frut_verd":final,
                    "comuna":comuna,
                    "region": region[0],
                    "img_path": img_filename,
                    "productor_id":id})
    return render_template("ver/ver-producto.html",datos=datos, paginas=paginas)

@app.route("/informacion-producto/<int:producto_id>", methods=["GET"])
def informacion_producto(producto_id):
    datos=[]
    id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor = db.get_producto(producto_id)
    comuna, region_id = db.get_comuna_by_id(comuna_id)
    region = db.get_region_by_id(region_id)
    images = db.get_fotos_producto(producto_id)
    originales= []
    for foto in images:
        if not (foto[1].startswith("640x480_") or foto[1].startswith("1280x1024_")):
            originales.append(foto)
    producto_id = db.get_productos_id(producto_id)
    frut_verd =  db.get_fruta_verdura(id)
    final=""
    for i in frut_verd:
        final=(i[0])+" "+final
    datos.append({
        "tipo":tipo,
        "frut_verd":final,
        "comuna":comuna,
        "region": region[0],
        "imgs": originales,
        "productor_id":id,
        "nombre_productor":nombre_productor})
    return render_template("informacion/informacion-producto.html",producto_info=datos)

@app.route("/informacion-pedido/<int:comprador_id>", methods=["GET"])
def informacion_pedido(comprador_id):
    datos=[]
    id, tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador = db.get_pedido(comprador_id)
    comuna, region_id = db.get_comuna_by_id(comuna_id)
    region = db.get_region_by_id(region_id)
    comprador_id = db.get_productos_id(comprador_id)
    frut_verd =  db.get_fruta_verdura(id)
    final=""
    for i in frut_verd:
        final=(i[0])+" "+final
    datos.append({
        "tipo":tipo,
        "frut_verd":final,
        "comuna":comuna,
        "region": region[0],
        "comprador_id":id,
        "descripcion":descripcion,
        "nombre_comprador":nombre_comprador,
        "mail_comprador":email_comprador,
        "celular_comprador":celular_comprador})
    return render_template("informacion/informacion-pedido.html",comprador_info=datos)

# ----------- estadisticas--------------- #

@app.route("/estadisticas", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def estadisticas():
    return render_template("informacion/estadisticas.html")


@app.route("/get-estadisticas-producto", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_estadisticas_producto():
    stats = db.get_estadisticas_producto()
    data = [{"tipo": stat[0], "cantidad": stat[1]} for stat in stats]
    return jsonify(data)


@app.route("/get-estadisticas-pedido", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_estadisticas_pedido():
    stats = db.get_estadisticas_pedido()
    data = [{"region": stat[0], "cantidad": stat[1]} for stat in stats]
    return jsonify(data)


def agregarfoto(foto,name):
        # 1. generate random name for img
        _filename_hash = hashlib.sha256(
            secure_filename(foto.filename).encode("utf-8")
            ).hexdigest()
        _extension = filetype.guess(foto).extension
        img_filename = f"{_filename_hash}_{str(uuid.uuid4())}.{_extension}"
        #img_filename = f"{_filename}.{_extension}"
        
        # 2. save img as a file
        foto.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

        with Image.open(os.path.join(app.config["UPLOAD_FOLDER"], img_filename)) as img:
            imagen_640x480 = img.resize((640,480))
            imagen_640x480.save(os.path.join(app.config["UPLOAD_FOLDER"], "640x480_"+img_filename))
            imagen_1280x1024 = img.resize((1280,1024))
            imagen_1280x1024.save(os.path.join(app.config["UPLOAD_FOLDER"], "1280x1024_"+img_filename))
        # 3. save  in db
        producto_id= db.get_producto_id_by_name(name)
        filepath = "static/uploads"
        db.insert_fotos(filepath, img_filename, producto_id)
        db.insert_fotos(filepath, "640x480_"+img_filename, producto_id)
        db.insert_fotos(filepath, "1280x1024_"+img_filename, producto_id)


if __name__ == "__main__":
    app.run(debug=True)
