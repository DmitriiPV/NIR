from django.contrib import admin
from .models import Pacient, Special, Skill, Employes, Diagnosis, DateOf

admin.site.register(Pacient)
admin.site.register(Special)
admin.site.register(Skill)
admin.site.register(Employes)
admin.site.register(Diagnosis)
admin.site.register(DateOf)
# Register your models here.
