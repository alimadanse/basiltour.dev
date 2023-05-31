from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tour,TourRegistration



class TourAdmin(admin.ModelAdmin):
    list_display = ['title','created', 'id', ]


class TourRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'nat_id', 'phone_number')
    search_fields = ('first_name', 'last_name', 'nat_id')
    list_filter = ('age',)

admin.site.register(TourRegistration, TourRegistrationAdmin)

admin.site.register(Tour, TourAdmin)
