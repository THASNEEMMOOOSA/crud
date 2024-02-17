from django.contrib import admin

from poll.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','name','eid','email','mob')


# Register your models here.
admin.site.register(Person,PersonAdmin)