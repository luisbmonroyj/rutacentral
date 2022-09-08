from flask import jsonify
from database import db
from models.vehiculo_data import VehiculoData
from datetime import datetime

# tipos de datos comunes: int, str, date, datetime, float, boolean
def create(placa: str, marca: str, linea: str, 
            matricula: datetime, poliza_soat: datetime, rtm: datetime, conductor: str) -> dict:  #...) -> dict:
    """Permite Crear un vehiculo en la base de datos con los campos"""
    #se instancia un objeto Vehiculo con sus propiedades(campos)
    vehiculo_i = VehiculoData(placa, marca, linea, matricula, poliza_soat, rtm, conductor) #,...)
    db.session.add(vehiculo_i)
    db.session.commit()
    respuesta = {"Respuesta": f"Se Creó el Vehiculo {marca} {linea}, con placa {placa}"}
    return respuesta

# def delete(pk: <tipo de dato>) -> dict:
def delete(placa: str) -> dict:
    """Permite Eliminar un vehiculo a partir de su PK (placa) que debe ser un string"""
    delete_vehiculo = VehiculoData.query.get(placa)
    nombre = VehiculoData.query.get(placa).marca + " " +  VehiculoData.query.get(placa).linea
    db.session.delete(delete_vehiculo)
    db.session.commit()
    respuesta = {"Respuesta": f"Se elimina el vehiculo {nombre} con placa {placa}"}
    return respuesta


def get() -> dict:
    "Permite Listar los vehiculos creados"
    list_vehiculo = VehiculoData.query.all()
    return jsonify(VehiculoData=[i.serialize for i in list_vehiculo])

#
# def patch(campo1: int, campo2: str, campo3: datetime, ...) -> dict:
def patch(placa: str, marca: str, linea: str, 
            matricula: datetime, poliza_soat: datetime, rtm: datetime, conductor: str) -> dict:
    """Permite Actualizar los datos del vehiculo segun su placa, la pk que es un string"""
    patch_vehiculo = VehiculoData.query.get(placa)
    #edita un objeto vehioulo con los datos de cedula
    patch_vehiculo.placa= placa
    patch_vehiculo.marca = marca
    patch_vehiculo.linea = linea
    patch_vehiculo.matricula = matricula
    patch_vehiculo.poliza_soat = poliza_soat
    patch_vehiculo.rtm = rtm
    patch_vehiculo.conductor = conductor

    #cambia los valores de las propiedades de conductor
    #...
    db.session.add(patch_vehiculo)
    db.session.commit()
    respuesta = {"Respuesta": f"Se actualizó el Vehiculo con placa {placa}"}
  # noqa: 501
    return respuesta
