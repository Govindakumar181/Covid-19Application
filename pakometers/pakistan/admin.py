from django.contrib import admin
from pakistan.models import world,pakistan,pakistan_hospitals
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(world)
admin.site.register(pakistan)
admin.site.register(pakistan_hospitals)

# @admin.register(world)
# class worldAdmin(ImportExportModelAdmin):
#     pass
# @admin.register(pakistan)
# class pakistanAdmin(ImportExportModelAdmin):
#     pass
# @admin.register(pakistan_hospitals)
# class pakistan_hospitalsdAdmin(ImportExportModelAdmin):
#     pass