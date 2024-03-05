from django.contrib import admin
from migration.models import Category, Course
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class DescriptionAdmin(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id','name','created_date','updated_date','image']
    list_filter = ['name']
    search_fields = ['name']
    readonly_fields = ['avatar']

    def avatar  (self, instance):
        if instance:
            return mark_safe(f'<img src="/static/{instance.image.name}" width="120" />')


admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
