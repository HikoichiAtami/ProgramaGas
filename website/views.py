from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from .models import User, Inventario, Chofer, Modo_Pago, Venta, Tipo_Compra, Tipo_Venta, Compra_General, Valores_Compra, Valores_Venta, Gastos_Varios
from . import db 

# Registro de la vista
views = Blueprint('views', __name__)

# Pagina visible cuando el usuario se logea
@views.route('/stock', methods=['GET'])
@login_required
def stock():
    data = db.session.query(Inventario).all()
    return render_template("stock.html", user=current_user, data=data)