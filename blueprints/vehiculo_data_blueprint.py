from flask_smorest import Blueprint
#from models import <modelo>
from models import vehiculo_data
#from controladores import controlador_<modelo>
from controllers import vehiculo_data_controller
from flask import make_response
from try_catch import try_catch


vehiculo_dataBlueprint = Blueprint(
    'Administrar Vehiculo', 'Vehiculo', url_prefix='/vehiculo_data',
    description='Administrar Vehiculo'
)

#blueprint para crear un registro
@vehiculo_dataBlueprint.route("/create", methods=['POST'])
@vehiculo_dataBlueprint.arguments(vehiculo_data.VehiculoEsquema, location='json')
#vehiculo_dataEsquema tiene los argumentos necesarios para hacer este metodo
#para create y update, los campos son parecidos por lo regular
@try_catch()
def create_vehiculo_data(data):
    """Permite crear un Vehiculo\n
    Es necesario escoJer un conductor existente o haberlo creado antes"""
    placa = data['placa']
    marca = data['marca']
    linea = data['linea']
    matricula = data['matricula']
    poliza_soat = data['poliza_soat']
    rtm = data['rtm']
    conductor = data['conductor']
    #...
    crear = vehiculo_data_controller.create(placa, marca, linea, matricula, poliza_soat, rtm, conductor) #,...)
    return make_response(crear, 200)
# con esta linea se manda a la db y se entrega el reporte, si hay error, try_catch lo reporta

#blueprint para borrar un registro
@vehiculo_dataBlueprint.route("/delete", methods=['DELETE'])
@vehiculo_dataBlueprint.arguments(vehiculo_data.VehiculoEsquemaDelete, location="json")
@try_catch()
def delete_vehiculo_data(data):
    """Permite Eliminar Vehiculo"""
    #para borrar, usualmente se necesita la llave primaria, por ende campo1 deberia ser la PK
    placa = data['placa']
    borrar = vehiculo_data_controller.delete(placa)
    return make_response(borrar, 200)

@vehiculo_dataBlueprint.route("/get", methods=['GET'])
@try_catch()
def get_vehiculo_data():
    """Permite Listar Vehiculo"""
    leer = vehiculo_data_controller.get()
    return make_response(leer, 200)

@vehiculo_dataBlueprint.route("/update", methods=['PATCH'])
@vehiculo_dataBlueprint.arguments(vehiculo_data.VehiculoEsquema, location='json')
@try_catch()
def update_vehiculo_data(data):
    """Permite Actualizar Vehiculo\n
    Todos los datos son necesarios para actualizar"""
    placa = data['placa']
    marca = data['marca']
    linea = data['linea']
    matricula = data['matricula']
    poliza_soat = data['poliza_soat']
    rtm = data['rtm']
    conductor = data['conductor']
    # ...
    actualizar = vehiculo_data_controller.patch(placa, marca, linea, matricula, poliza_soat, rtm, conductor)  # ,...)

    return make_response(actualizar, 200)