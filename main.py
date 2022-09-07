from flask import Flask
from flask_smorest import Api
from flask_cors import CORS
import json
from waitress import serve
from database import db
from blueprints import conductor_blueprint

def loadFileConfig():
    """Carga la Configuracion para waitress"""
    with open('config.json') as f:
        data = json.load(f)
    return data


def loaddbSettings():
    """Carga la configuracion para la conexion con Postgres"""
    with open('dbSettings.json') as f:
        data = json.load(f)
    data = f"""postgresql://{data["user"]}:{data["password"]}@localhost/{data["database"]}"""  # noqa: 501
    return data


def create_app():
    """Crear la Aplicacion"""
    app = Flask(__name__)
    CORS(app)

    # Configurar Base de Datos
    dbSettings = loaddbSettings()
    app.config['SQLALCHEMY_DATABASE_URI'] = dbSettings
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    #  Swagger
    app.config["API_TITLE"] = "Backend Ruta Central"
    app.config["API_VERSION"] = "0.1.0"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_JSON_PATH"] = "api-spec.json"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # noqa: 501

    # Registrar Blueprints
    api = Api(app)
    api.register_blueprint(conductor_blueprint.conductorBlueprint)
    # api.register_blueprint(partido_blueprint.partidosBlueprint)
    # api.register_blueprint(candidatos_blueprint.candidatosBlueprint)
    # api.register_blueprint(resultados_blueprint.resultadosBlueprint)

    return app


def set_up_db(app):
    """Crear todas las Tablas"""
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    app = create_app()
    app.app_context().push()
    set_up_db(app)
    with open('banner.txt') as f:
        print(f.read())
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
