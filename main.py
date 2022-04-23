from logging import debug 
from website import create_app

# Se obtiene la aplicacion Flask
app = create_app()

# Validacion para que la aplicacion solo se ejecute desde el archivo principal
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")