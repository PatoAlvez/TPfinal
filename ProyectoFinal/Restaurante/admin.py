from django.contrib import admin
from Restaurante.models import Entrada, PlatoPrincipal, Postre, Avatar

# Register your models here.

admin.site.register(Entrada)
admin.site.register(PlatoPrincipal)
admin.site.register(Postre)
admin.site.register(Avatar)