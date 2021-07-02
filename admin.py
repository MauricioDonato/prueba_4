from django.contrib import admin

from .models import Cliente, Comuna, Producto

admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(Producto)