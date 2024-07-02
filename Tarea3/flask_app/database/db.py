import pymysql
import json


# -- Config to access the database --
DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# -- querys --


def get_region_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_region_by_id"], (id,))
	region = cursor.fetchone()
	return region

def get_comuna_by_id(id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_by_id"], (id,))
	comuna = cursor.fetchone()
	return comuna

def get_comuna_id(comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna_id"], (comuna,))
	comuna_id = cursor.fetchone()
	return comuna_id

def get_comuna_name(comuna):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_comuna"], (comuna,))
	comuna_name = cursor.fetchone()
	return comuna_name

def get_region_name(region):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_region"], (region,))
	region_name = cursor.fetchone()
	return region_name

def get_fruta_verdura(fruta_verd):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_Fruta_Verdura"], (fruta_verd,))
	fruta_verd_amount = cursor.fetchone()
	return fruta_verd_amount

def get_producto_id_by_name(nombre):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_producto_id_by_name"], (nombre,))
	nombre_id = cursor.fetchone()
	return nombre_id

def get_productos(page_size,offset):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_productos"],(page_size,offset))
	fruta_verd_amount = cursor.fetchall()
	return fruta_verd_amount

def get_fruta_verdura_id(fruta_verdura):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_fruta_verdura_id"], (fruta_verdura,))
	fruta_verdura_id = cursor.fetchone()
	return fruta_verdura_id

def get_fotos_producto(id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_fotos_producto"], (id,))
	foto_by_id = cursor.fetchall()
	return foto_by_id

def get_productos_id(id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_productos_id"], (id,))
	productos_id = cursor.fetchone()
	return productos_id

def get_producto(id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_producto"], (id,))
	productos_id = cursor.fetchone()
	return productos_id


def get_fruta_verdura(id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_Fruta_Verdura"],(id,))
	frut_verd = cursor.fetchall()
	return frut_verd

def get_fruta_verdura_by_name(id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_fruta_verdura_by_name"],(id,))
	frut_verd = cursor.fetchone()
	return frut_verd

def get_cosas(cosa_id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_cosas"], (cosa_id,))
	frut_verd = cursor.fetchone()
	return frut_verd


def insert_fotos(filepath, img_filename, producto_id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insert_foto"], (filepath,img_filename,producto_id))
	conn.commit()

def insert_producto(tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor):
	conn=get_conn()
	cursor= conn.cursor()
	cursor.execute(QUERY_DICT["insert_producto"],(tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor))
	conn.commit()
	
def insert_producto_verdura_fruta(producto_id,fruta_verdura_id):
	conn=get_conn()
	cursor= conn.cursor()
	cursor.execute(QUERY_DICT["insert_fruta_verdura"],(producto_id,fruta_verdura_id))
	conn.commit()
# --------------------------------------------- QUERYS PEDIDO --------------------------------------------------- #

def insert_pedido(tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador):
	conn=get_conn()
	cursor= conn.cursor()
	cursor.execute(QUERY_DICT["insert_pedido"],(tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador))
	conn.commit()

def insert_pedido_verdura_fruta(producto_id,fruta_verdura_id):
	conn=get_conn()
	cursor= conn.cursor()
	cursor.execute(QUERY_DICT["insert_pedido_fruta_verdura"],(fruta_verdura_id,producto_id))
	conn.commit()
	
def get_pedidos(page_size,offset):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_pedidos"],(page_size,offset))
	fruta_verd_amount = cursor.fetchall()
	return fruta_verd_amount

def get_pedido(comprador_id):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_pedido"],(comprador_id))
	fruta_verd_amount = cursor.fetchone()
	return fruta_verd_amount

def get_pedido_id_by_name(nombre):
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_pedido_id_by_name"], (nombre,))
	nombre_id = cursor.fetchone()
	return nombre_id

# ------------------- estadisticas ----------------- #

def get_estadisticas_producto():
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_estadisticas_producto"])
	estadisticas = cursor.fetchall()
	return estadisticas


def get_estadisticas_pedido():
	conn=get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_estadisticas_pedido"])
	estadisticas = cursor.fetchall()
	return estadisticas