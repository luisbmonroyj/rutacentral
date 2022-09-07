from flask_smorest import Blueprint
#from models import <modelo>
from models import conductor
#from controladores import controlador_<modelo>
from controllers import conductor_controller
from flask import make_response
from try_catch import try_catch


conductorBlueprint = Blueprint(
    'Administrar Conductor', 'Conductor', url_prefix='/conductor',
    description='Administrar Conductor'
)

#blueprint para crear un registro
@conductorBlueprint.route("/create", methods=['POST'])
@conductorBlueprint.arguments(conductor.ConductorEsquema, location='json')
#ConductorEsquema tiene los argumentos necesarios para hacer este metodo
#para create y update, los campos son parecidos por lo regular
@try_catch()
def create_conductor(data):
    """Permite crear un conductor"""
    cedula = data["cedula"]
    apellido = data["apellido"]
    nombre = data["nombre"]
    telefono = data["telefono"]
    #...
    crear = conductor_controller.create(cedula,apellido,nombre,telefono) #,...)
    return make_response(crear, 200)
# con esta linea se manda a la db y se entrega el reporte, si hay error, try_catch lo reporta

#blueprint para borrar un registro
@conductorBlueprint.route("/delete", methods=['DELETE'])
@conductorBlueprint.arguments(conductor.ConductorEsquemaDelete, location="json")
@try_catch()
def delete_conductor(data):
    """Permite Eliminar conductor"""
    #para borrar, usualmente se necesita la llave primaria, por ende campo1 deberia ser la PK
    cedula = data["cedula"]
    borrar = conductor_controller.delete(cedula)
    return make_response(borrar, 200)


@conductorBlueprint.route("/get", methods=['GET'])
@try_catch()
def get_conductor():
    """Permite Listar Conductores"""
    leer = conductor_controller.get()
    return make_response(leer, 200)

@conductorBlueprint.route("/update", methods=['PATCH'])
@conductorBlueprint.arguments(conductor.ConductorEsquema, location='json')
@try_catch()
def update_conductor(data):
    """Permite Actualizar conductor\n
    Esta linea aparece en los comentarios antes del ejemplo en el swagger\n
    Todos los datos son necesarios para actualizar"""
    cedula = data["cedula"]
    apellido = data["apellido"]
    nombre = data["nombre"]
    telefono = data["telefono"]
    # ...
    actualizar = controlador_ejemplo.patch(cedula,apellido,nombre,telefono)  # ,...)

    return make_response(actualizar, 200)





#documentacion general
# se deben crear estas lineas generales para cada metodo del CRUD
    # @ejemplo_createBlueprint.route("/<endpoint>", methods=['PATCH' or 'GET' or 'DELETE' or 'POST'])
    # @<modelo>Blueprint.arguments(<modelo>.EsquemaQueSeVaAUsar, location='json')
    # EsquemaQueSeVaAUsar ES UNA CLASE QUE ESTA AL FINAL DEL MODELO, SON LOS ARGUMENTOS
    # QUE SE REQUIEREN PARA EJECUTAR EL METODO CRUD
    #
    # EL DECORADOR try_catch ES UNA FUNCION QUE HACE EL TRY Y DEVUELVE EL ERROR A PYTHON
    # @try_catch()
    # def METHOD_<modelo>(data): 
    #  METHOD DEBE SER: PATCH, GET, DELETE, POST, en minusculas segun el caso
    #     """AQUI SE INGRESA LA DESCRIPCION DEL METODO Y SUS RESTRICCIONES DE LLAVES FORANEAS ETC
    #           ESTA INFORMACION APARECE EN LA PANTALLA DE PRUEBA DE SWAGGER"""
    #     data es un diccionario, de modo que se 
    #     dato1 = data["llave1"]
    #     dato2   = data["llave2"]
    #     mensaje_respuesta = controlador_<modelo>.METHOD(dato1, dato2, ...)


#     METHOD hace referencia a los metodos CRUD instanciados en el controlador
#     return make_response(mensaje_respuesta, 200)
#     preferiblemente se utiliza el codigo 200 para que se entregue la respuesta que se configuro en el controlador