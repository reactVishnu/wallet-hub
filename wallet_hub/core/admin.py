from django.contrib import admin
from django.contrib.auth import get_user_model
from service.models import TextDetail

# Register your models here.

admin.site.register(get_user_model())


class TextDetailAdmin(admin.ModelAdmin):
    readonly_fields = ['user']  # Make the user field read-only

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:  # Editing an existing object
            return readonly_fields + ['user']
        return readonly_fields

    # Optionally, include the user field in the list display
    list_display = ['__str__', 'user']


admin.site.register(TextDetail, TextDetailAdmin)
