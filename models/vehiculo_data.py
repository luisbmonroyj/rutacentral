from datetime import datetime
from database import db
import marshmallow as masmelo

def format_date(value):
    """Deserializa objetos datetime en un string para ser facilmente
        en un JSON."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d")
    #return value.strftime("%Y-%m-%d %H:%M:%S")
    

class VehiculoData(db.Model):
    """Tabla para hacer un Vehiculo"""
    __tablename__ = "vehiculo_data"
    #este es el nombre que va a tener la tabla en la DB
    #el tipo de campo pueden ser los que tiene la DB, los que se muestran son un ejemplo
    #ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    # DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    # INTERVAL, JSON, JSONB, MACADDR, MONEY, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    # TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    # DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR

    placa = db.Column(db.String, primary_key=True)
    marca = db.Column(db.String)
    linea = db.Column(db.String)
    matricula = db.Column(db.Date)
    poliza_soat = db.Column(db.Date)
    rtm = db.Column(db.Date)
    conductor = db.Column(db.Integer, db.ForeignKey("conductor.cedula"))#must be unique
    #... y los campos que vaya a tener la tabla
    #si alguno de los campos se usa en otra tabla como FK, se debe instanciar
    #vehiculo_data = db.relationship("vehiculo_data")
    #campoFK = db.Column(db.<Integer, String, etc>, db.ForeignKey("modelo.campo"))
    
    def __init__(self, placa: str, marca: str, linea: str, 
                matricula: datetime, poliza_soat: datetime, rtm: datetime, conductor: str):    #...):
        """Inicializar Modelo Vehiculo, con los campos de la tabla"""
        self.placa= placa
        self.marca = marca
        self.linea = linea
        self.matricula = matricula
        self.poliza_soat = poliza_soat
        self.rtm = rtm
        self.conductor = conductor#must be unique
        #...

    @property
    def serialize(self) -> dict:
        """Devuelve los datos del objeto en un formato serializable para el caso de un registro"""
        return {
            'placa':self.placa,
            'marca':self.marca, 
            'linea':self.linea, 
            'matricula':format_date(self.matricula), 
            'poliza_soat':format_date(self.poliza_soat), 
            'rtm':format_date(self.rtm), 
            'conductor':self.conductor, 
            #...
        }

    @property
    def serialize_many2many(self) -> dict:
        """
        Devuelve los datos del objeto en un formato serializable
        Cuando son mas de 1 registros se utiliza el metodo many2many.
        """
        return [item.serialize for item in self.many2many]


class VehiculoEsquema(masmelo.Schema):
    """Esquema de validacion para endpoint de vehiculo: Create y Update
    estos datos son NECESARIOS para crear y actualizar el registro"""
    class Meta:
        ordered = True
    #poner aqui los campos que se necesitan para crear y actualizar
    placa = masmelo.fields.String(required=True)
    marca = masmelo.fields.String(required=True)
    linea = masmelo.fields.String(required=True)
    matricula = masmelo.fields.Date(required=True)
    poliza_soat = masmelo.fields.Date(required=True)
    rtm = masmelo.fields.Date(required=True)
    conductor = masmelo.fields.String(required=True) #must be unique
    #...

class VehiculoEsquemaDelete(masmelo.Schema):
    """Esquema de validacion para endpoint de Candidato: Delete
    requiere la llave primaria para borrar"""

    class Meta:
        ordered = True
    # Este es el unico dato que se necesita para borrar, la PK
    placa = masmelo.fields.String(required=True)

