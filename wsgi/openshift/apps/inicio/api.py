from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Compra

class CompraResource(ModelResource):
	class Meta:
		queryset = Compra.objects.all()
		resource_name = 'compra'
		always_return_data = True

	
