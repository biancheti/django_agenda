from django.contrib import admin
from .models import Grupo, Contato

# Register your models here.
admin.site.site_header = "Projeto Agenda"
admin.site.site_title = "Projeto Agenda"
admin.site.site_url = "Bem Vindo ao Projeto Agenda"


admin.site.register(Grupo)
admin.site.register(Contato)
