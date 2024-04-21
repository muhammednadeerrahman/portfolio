from django.contrib import admin
from web.models import Skill, Contact


class SkillAdmin(admin.ModelAdmin):
    list_display = ["skill_name", "skill_type"]
admin.site.register(Skill,SkillAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email","phone"]
admin.site.register(Contact,ContactAdmin)

