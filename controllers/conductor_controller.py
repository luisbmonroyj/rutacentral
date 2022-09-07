from flask import jsonify
from database import db
from models.conductor import Conductor
from datetime import datetime

# tipos de datos comunes: int, str, date, datetime, float, boolean
def create(cedula: int, apellido: str, nombre: str, telefono: str) -> dict:  #...) -> dict:
    """Permite Crear un Conductor en la base de datos con los campos"""
    #se instancia un objeto Conductor con sus propiedades(campos)
    conductor_n = Conductor(cedula, apellido, nombre, telefono) #,...)
    db.session.add(conductor_n)
    db.session.commit()
    respuesta = {"Respuesta": f"Se Creó el Conductor {nombre} {apellido}, Telefono = {telefono}, cedula: {cedula}"}
    return respuesta

# def delete(pk: <tipo de dato>) -> dict:
def delete(cedula: int) -> dict:
    """Permite Eliminar Conductor a partir de su PK que debe ser un entero"""
    delete_conductor = Conductor.query.get(cedula)
    nombre = Conductor.query.get(cedula).nombre + " " +  Conductor.query.get(cedula).apellido
    db.session.delete(delete_conductor)
    db.session.commit()
    respuesta = {"Respuesta": f"Se elimina el Conductor {nombre}"}
    return respuesta


def get() -> dict:
    "Permite Listar los conductores creados"
    list_conductor = Conductor.query.all()
    return jsonify(Ejemplo=[i.serialize for i in list_conductor])

#
# def patch(campo1: int, campo2: str, campo3: datetime, ...) -> dict:
def patch(cedula: int, apellido: str, nombre: str, telefono: str) -> dict:
    """Permite Actualizar los datos del Conductor segun su cedula, la pk y es un entero"""
    patch_conductor = Conductor.query.get(cedula)
    #crea un objeto conductor con los datos de cedula
    patch_conductor.apellido = apellido
    patch_conductor.nombre = nombre
    patch_conductor.telefono = telefono
    #cambia los valores de las propiedades de conductor
    #...
    db.session.add(patch_conductor)
    db.session.commit()
    respuesta = {"Respuesta": f"Se actualizó el Conduuctor con cedula {cedula},"
                              f" apellido = {apellido},nombre = {nombre},telefono = {telefono}"}
  # noqa: 501
    return respuesta
