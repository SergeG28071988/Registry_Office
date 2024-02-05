from django.contrib import admin

# Register your models here.
from .models import Marriage, Divorce

class MarriageAdmin(admin.ModelAdmin):
    pass


class DivorceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Marriage, MarriageAdmin)
admin.site.register(Divorce, DivorceAdmin)
