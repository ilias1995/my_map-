from django.contrib import admin
from taxi.models import Registr_taxi, From_where, Where, Registration
# Register your models hers

admin.site.register(Registr_taxi)
admin.site.register(From_where)
admin.site.register(Where)
admin.site.register(Registration)