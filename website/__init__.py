from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Declaracion de la DB
db = SQLAlchemy()

# Nombre de la DB
db_name = 'gas.db'

# Funcion que ejecuta la aplicacion
def create_app():
    app = Flask(__name__)

    # Clave secreta
    app.config['SECRET_KEY'] = 'programa gas freddy'

    # Ubicacion de la DB
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'

    # Inicializacion de la DB en la app
    db.init_app(app)

    # Import de los archivos
    from .views import views
    from .auth import auth

    # Registro de paginas
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import de los objetos
    from .models import User

    create_database(app)

    # Acceso a vista cuando el usuario se logea
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Funcion que obtiene y carga el ID del usuario logeado
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Funcion que obtiene el id del usuario
def create_database(app):
    if not path.exists('website/' + db_name):
        db.create_all(app=app)
        print('Base de datos creada!!!')