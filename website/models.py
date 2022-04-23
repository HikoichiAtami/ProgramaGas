from werkzeug.wrappers.user_agent import UserAgentMixin
from . import db
from flask_login import UserMixin
from sqlalchemy import func

# Tabla de usuario para login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String)

# Tabla de choferes
class Chofer(db.Model):
    nombre = db.Column(db.String(150))
    id_chofer = db.Column(db.Integer, primary_key=True)
    numero_ventas = db.Column(db.Integer)

# Table de compra general
class Compra_General(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(150))
    valor_total = db.Column(db.Integer)
    cantidad_descuento = db.Column(db.Integer)
    cantidad_vales = db.Column(db.Integer)
    nota_credito = db.Column(db.Integer)
    deposito = db.Column(db.Integer)
    compra_5 = db.Column(db.Integer)
    compra_11 = db.Column(db.Integer)
    compra_15 = db.Column(db.Integer)
    compra_45 = db.Column(db.Integer)

# Tabla de Gastos Varios
class Gastos_Varios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150))
    valor = db.Column(db.Integer)
    fecha = db.Column(db.String(150))

# Tabla Inventario
class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    galon_5_vacio = db.Column(db.Integer)
    galon_11_vacio = db.Column(db.Integer)
    galon_15_vacio = db.Column(db.Integer)
    galon_45_vacio = db.Column(db.Integer)
    galon_5_lleno = db.Column(db.Integer)
    galon_11_lleno = db.Column(db.Integer)
    galon_15_lleno = db.Column(db.Integer)
    galon_45_lleno = db.Column(db.Integer)
    cantidad_vales = db.Column(db.Integer)
    ganancia = db.Column(db.Integer)

# Tabla modo de pago
class Modo_Pago(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True)
    efectivo = db.Column(db.Integer)
    debito = db.Column(db.Integer)
    vale = db.Column(db.Integer)

# Tabla tipo de compra
class Tipo_Compra(db.Model):
    id_compra = db.Column(db.Integer, primary_key=True)
    balon_5 = db.Column(db.Integer)
    balon_11 = db.Column(db.Integer)
    balon_15 = db.Column(db.Integer)
    balon_45 = db.Column(db.Integer)
    recarga_5 = db.Column(db.Integer)
    recarga_11 = db.Column(db.Integer)
    recarga_15 = db.Column(db.Integer)
    recarga_45 = db.Column(db.Integer)

# Tabla tipo de venta
class Tipo_Venta(db.Model):
    id_venta = db.Column(db.Integer,db.ForeignKey('venta.id_venta'), primary_key=True)
    balon_5 = db.Column(db.Integer)
    balon_11 = db.Column(db.Integer)
    balon_15 = db.Column(db.Integer)
    balon_45 = db.Column(db.Integer)
    recarga_5 = db.Column(db.Integer)
    recarga_11 = db.Column(db.Integer)
    recarga_15 = db.Column(db.Integer)
    recarga_45 = db.Column(db.Integer)

# Tabla valores compra
class Valores_Compra(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True)
    balon_5 = db.Column(db.Integer)
    balon_11 = db.Column(db.Integer)
    balon_15 = db.Column(db.Integer)
    balon_45 = db.Column(db.Integer)
    recarga_5 = db.Column(db.Integer)
    recarga_11 = db.Column(db.Integer)
    recarga_15 = db.Column(db.Integer)
    recarga_45 = db.Column(db.Integer)
    fecha_modificacion = db.Column(db.String(150))

# Tabla valores venta
class Valores_Venta(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True)
    balon_5 = db.Column(db.Integer)
    balon_11 = db.Column(db.Integer)
    balon_15 = db.Column(db.Integer)
    balon_45 = db.Column(db.Integer)
    recarga_5 = db.Column(db.Integer)
    recarga_11 = db.Column(db.Integer)
    recarga_15 = db.Column(db.Integer)
    recarga_45 = db.Column(db.Integer)
    fecha_modificacion = db.Column(db.String(150))

# Tabla venta
class Venta(db.Model):
    id_venta = db.Column(db.Integer, primary_key=True)
    id_chofer = db.Column(db.Integer, db.ForeignKey('chofer.id_chofer'))
    fecha_venta = db.Column(db.String(150))
    monto_venta_local = db.Column(db.Integer)
    descuento_caja_los_andes = db.Column(db.Integer)
    monto_vale = db.Column(db.Integer)
    valor_vale = db.Column(db.Integer)
