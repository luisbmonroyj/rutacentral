from database import db
import marshmallow as masmelo

class Conductor(db.Model):
    """Tabla para hacer un Conductor"""
    __tablename__ = "conductor"
    #este es el nombre que va a tener la tabla en la DB
    #el tipo de campo pueden ser los que tiene la DB, los que se muestran son un ejemplo
    #ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    # DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    # INTERVAL, JSON, JSONB, MACADDR, MONEY, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    # TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    # DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR

    cedula = db.Column(db.Integer, primary_key=True)
    apellido = db.Column(db.String)
    nombre = db.Column(db.String)
    telefono = db.Column(db.String)
    
    #campo3 = db.Column(db.DateTime)
    #... y los campos que vaya a tener la tabla
    #si alguno de los campos se usa en otra tabla como FK, se debe instanciar
    vehiculo_data = db.relationship("VehiculoData")

    def __init__(self, cedula: int, apellido: str, nombre: str, telefono: str):    #...):
        """Inicializar Modelo Conductor, con los campos de la tabla"""
        self.cedula= cedula
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        #...

    @property
    def serialize(self) -> dict:
        """Devuelve los datos del objeto en un formato serializable para el caso de un registro"""
        return {
            'cedula': self.cedula,
            'apellido': self.apellido,
            'nombre': self.nombre,
            'telefono':self.telefono 
            #...
        }

    @property
    def serialize_many2many(self) -> dict:
        """
        Devuelve los datos del objeto en un formato serializable
        Cuando son mas de 1 registros se utiliza el metodo many2many.
        """
        return [item.serialize for item in self.many2many]


class ConductorEsquema(masmelo.Schema):
    """Esquema de validacion para endpoint de Conductor: Create y Update
    estos datos son NECESARIOS para crear y actualizar el registro"""
    class Meta:
        ordered = True
    #poner aqui los campos que se necesitan para crear y actualizar
    cedula = masmelo.fields.Integer(required=True)
    apellido = masmelo.fields.String(required=True)
    nombre = masmelo.fields.String(required=True)
    telefono = masmelo.fields.String(required=True)
    #...

class ConductorEsquemaDelete(masmelo.Schema):
    """Esquema de validacion para endpoint de Candidato: Delete
    requiere la llave primaria para borrar"""

    class Meta:
        ordered = True

    # Este es el unico dato que se necesita para borrar, la PK
    cedula = masmelo.fields.Integer(required=True)

