from import_export import resources
from .models import Tipo_pqrs, Estado

class PqrsResource(resources.ModelResource):
       class Meta:
              Model = Tipo_pqrs
              fields = ('id','Tipo_pqrs')
              
class EstadoResource(resources.ModelResource):
       class Meta:
              Model = Estado
              fields = ('id', 'Estado_pqrs')