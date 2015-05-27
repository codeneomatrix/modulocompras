from django.db import models
from datetime import datetime   




class Compra(models.Model):
	folio = models.CharField(max_length=50, blank=True)
	proveedor = models.CharField(max_length=50, blank=True)
	fechapedido = models.DateField(blank=True, null=True)
	fechapago = models.DateField(default="01-01-2000", blank=True, null=True)
	articulo1 = models.CharField(max_length=50, blank=True)	
	cantidad1 = models.IntegerField(default=0, blank=True, null=True)
	preciouni1 = models.IntegerField(default=0, blank=True, null=True)
	unidadmedida = models.CharField(default="metros", max_length=50, blank=True)	
	preciototal = models.IntegerField(default=0, blank=True, null=True)
	
	def __unicode__(self):
		return self.folio

def obj_create(self, bundle, **kwargs):
        return super(EnvironmentResource, self).obj_create(bundle, user=bundle.request.user)