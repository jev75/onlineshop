from django.contrib import admin
from .models import Profile
from django.contrib.admin import AdminSite


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)

class MyAdminSite(AdminSite):
    site_header = 'Parduotuvės administravimas'
    site_title = 'Administravimo panelė'
    index_title = 'Sveiki atvykę į administravimo panelę'

    def each_context(self, request):
        context = super().each_context(request)
        context['extra_css'] = 'css/custom_admin.css'
        context['extra_js'] = 'js/custom_admin.js'
        return context

admin_site = MyAdminSite(name='myadmin')
