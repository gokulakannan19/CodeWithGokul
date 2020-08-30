from django.contrib import admin
from .models import GokulaKannan, Projects, Services, Queries

# Register your models here.


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("project_name",)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ("service_name",)


class QueryAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_query")


admin.site.register(GokulaKannan)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Queries, QueryAdmin)
